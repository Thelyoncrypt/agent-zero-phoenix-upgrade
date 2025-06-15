# python/agents/browser_agent/actions.py
import asyncio
import re
from typing import Dict, Any, Optional, List
from playwright.async_api import Page as PWPage, Error as PlaywrightError
import json
import numpy as np

# For LLM calls (similar to KnowledgeAgent or EmbeddingGenerator)
import os
from openai import OpenAI, APIError, RateLimitError, BadRequestError
from dotenv import load_dotenv
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

project_root = Path(__file__).resolve().parents[2]
dotenv_path = project_root / '.env'
load_dotenv(dotenv_path, override=True)

ACTION_TRANSLATION_SYSTEM_PROMPT = """
You are an expert at translating natural language browser interaction commands into specific Playwright actions and CSS selectors.
Given current page context (like title and interactive elements) and a user instruction, identify the single, most direct browser action to perform.
Respond with a JSON object with the following fields:
- "action_type": Choose one from ["click", "fill", "type", "press", "navigate", "scroll", "select_option", "warn_user", "clarify"].
- "selector": (Required for most actions except navigate/global press/scroll/warn_user/clarify) A concise and robust CSS selector for the target element. If multiple good selectors exist, provide a comma-separated list, ordered by preference.
- "value": (Required for "fill", "type", "select_option") The text to type/fill or the value of the option to select.
- "key": (Required for "press") The key to press (e.g., "Enter", "ArrowDown", "Tab").
- "url": (Required for "navigate") The URL to navigate to.
- "scroll_direction": (Required for "scroll") One of ["down", "up", "bottom", "top", "into_view"]. If "into_view", "selector" is also required.
- "message": (Required for "warn_user" or "clarify") A message to the user if the instruction is ambiguous, requires information not present, or is unsafe.
- "reasoning": (Optional) A brief explanation of why you chose this action and selector.

Prioritize actions that directly address the instruction. If a selector is not obvious, provide a few good alternatives.
If the instruction is too vague (e.g., "do something"), or requires external knowledge not provided, use "clarify" and ask for more specific instructions.
If the instruction seems potentially harmful or impossible (e.g., "delete system files via browser"), use "warn_user".

Example Instruction: "Click the main login button."
Page Context: "Title: Login Page. Buttons: ['Login', 'Forgot Password']. Inputs: 2."
Example Response: {"action_type": "click", "selector": "button:has-text('Login'), input[type='submit'][value='Login']", "reasoning": "Identified 'Login' button as the most likely target."}

Example Instruction: "Type 'myusername' in the user field."
Page Context: "Title: Sign In. Inputs: ['Username', 'Password']."
Example Response: {"action_type": "fill", "selector": "input[name*='user'], input[id*='user'], input[placeholder*='User']", "value": "myusername", "reasoning": "Identified input field likely related to username."}
"""

DATA_EXTRACTION_SYSTEM_PROMPT = """
You are an expert at extracting structured information from web page content based on a user's instruction and an optional JSON schema.
You will be given a summary of the web page content, the user's instruction for what to extract, and optionally a JSON schema defining the desired output format.
Your goal is to populate the JSON schema with information extracted from the page content according to the instruction.
If a JSON schema is provided, your output MUST strictly conform to this schema.
If a schema is not provided, attempt to extract the information as a reasonably structured JSON object based on the instruction.
Focus ONLY on the provided page content. If information is not present in the content, indicate this appropriately (e.g., null values or empty strings for fields in the JSON).
Output ONLY the populated JSON object. Do not include any other text, explanations, or markdown formatting around the JSON.
If the page content is too limited or irrelevant to the instruction, return an empty JSON object {} or an object indicating no data found, like {"error": "No relevant data found"}.
If a field in the schema is an array and multiple items are found, populate the array. If only one is found, still use an array with one item. If none, use an empty array [].
"""

class ActionExecutor:
    def __init__(self, llm_model: Optional[str] = None, extraction_llm_model: Optional[str] = None):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.action_llm_model = llm_model or os.getenv("BROWSER_LLM_MODEL", "gpt-4o-mini")
        self.extraction_llm_model = extraction_llm_model or os.getenv("EXTRACTION_LLM_MODEL", self.action_llm_model) # Default to same model

        if not self.api_key:
            raise ValueError("OpenAI API key required for ActionExecutor.")
        self.llm_client = OpenAI(api_key=self.api_key)
        logger.info(f"ActionExecutor: Initialized. Action LLM: '{self.action_llm_model}', Extraction LLM: '{self.extraction_llm_model}'.")

    async def _get_page_summary_for_llm(self, page: PWPage, max_elements: int = 10, max_len_per_element: int = 50) -> str:
        """Gets a brief summary of the current page for LLM context."""
        try:
            page_title = await page.title()
            page_url = page.url

            # Get some interactive elements (buttons, inputs, links)
            interactive_elements_summary = []

            # Buttons
            buttons = await page.locator("button, input[type='submit'], input[type='button'], [role='button']").all()
            for i, btn in enumerate(buttons[:max_elements]):
                try:
                    text = (await btn.text_content(timeout=500) or await btn.get_attribute("value") or await btn.get_attribute("aria-label") or "Unnamed Button").strip()
                    if text: interactive_elements_summary.append(f"Button: '{text[:max_len_per_element]}'")
                except Exception: pass # Ignore if element disappears or text cannot be fetched quickly

            # Inputs
            inputs = await page.locator("input[type='text'], input[type='search'], input[type='email'], input[type='password'], input[type='number'], textarea, select").all()
            for i, inp in enumerate(inputs[:max_elements]):
                try:
                    name = (await inp.get_attribute("name") or await inp.get_attribute("id") or await inp.get_attribute("placeholder") or "Unnamed Input").strip()
                    if name: interactive_elements_summary.append(f"Input: '{name[:max_len_per_element]}'")
                except Exception: pass

            # Links
            links = await page.locator("a[href]").all()
            for i, link in enumerate(links[:max_elements]):
                try:
                    text = (await link.text_content(timeout=500) or await link.get_attribute("aria-label") or "Unnamed Link").strip()
                    if text: interactive_elements_summary.append(f"Link: '{text[:max_len_per_element]}'")
                except Exception: pass

            summary = f"Current URL: {page_url}\nPage Title: {page_title}\nVisible Interactive Elements:\n" + "\n".join(f"- {s}" for s in interactive_elements_summary)
            return summary
        except Exception as e:
            logger.warning(f"ActionExecutor: Error getting page summary for LLM: {e}")
            return f"Current URL: {page.url}\nPage Title: {await page.title()}\n(Could not retrieve detailed element summary)"

    async def _translate_instruction_to_action(self, page_context_summary: str, instruction: str) -> Optional[Dict[str, Any]]:
        """Uses LLM to translate natural language instruction to a structured action."""
        prompt = f"""
        Current Page Context:
        ---
        {page_context_summary}
        ---
        User Instruction: "{instruction}"

        Based on the page context and user instruction, determine the single, most direct browser action to perform.
        Respond with a JSON object following the specified schema.
        """
        messages = [
            {"role": "system", "content": ACTION_TRANSLATION_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
        logger.debug(f"ActionExecutor LLM Prompt for action translation:\nSystem: {ACTION_TRANSLATION_SYSTEM_PROMPT}\nUser: {prompt}")

        try:
            response = await asyncio.to_thread(
                self.llm_client.chat.completions.create,
                model=self.action_llm_model, messages=messages,
                response_format={"type": "json_object"}, temperature=0.1
            )
            action_json_str = response.choices[0].message.content
            action_dict = json.loads(action_json_str)
            logger.info(f"ActionExecutor LLM translation: '{instruction}' -> {action_dict}")
            return action_dict
        except json.JSONDecodeError as jde:
            logger.error(f"ActionExecutor: LLM returned invalid JSON for instruction '{instruction}': {action_json_str}. Error: {jde}")
        except BadRequestError as bre: # Often due to context length or bad input to OpenAI
             logger.error(f"ActionExecutor: OpenAI BadRequestError: {bre}. Instruction: '{instruction}'")
        except APIError as apie:
            logger.error(f"ActionExecutor: OpenAI APIError for instruction '{instruction}': {apie}")
        except Exception as e:
            logger.error(f"ActionExecutor: Unexpected error calling LLM for instruction translation: {e}", exc_info=True)
        return None

    async def execute_ai_action(self, page: PWPage, instruction: str) -> Dict[str, Any]:
        logger.info(f"ActionExecutor: Attempting AI action on page {page.url}. Instruction: '{instruction}'")

        page_context_summary = await self._get_page_summary_for_llm(page)
        parsed_action = await self._translate_instruction_to_action(page_context_summary, instruction)

        if not parsed_action or not isinstance(parsed_action, dict):
            return {"status": "error", "message": "LLM could not parse instruction into a valid action.", "original_instruction": instruction}

        action_type = parsed_action.get("action_type")
        if not action_type:
            return {"status": "error", "message": "LLM response missing 'action_type'.", "parsed_response": parsed_action}

        if action_type == "warn_user" or action_type == "clarify":
            return {"status": "clarification_needed", "message": parsed_action.get("message", "The LLM planner requires clarification or warns about the instruction."), "details": parsed_action}

        selector_str = parsed_action.get("selector")
        value = parsed_action.get("value")
        key_to_press = parsed_action.get("key")
        url_to_navigate = parsed_action.get("url")
        scroll_direction = parsed_action.get("scroll_direction")
        option_value = parsed_action.get("option_value") # For select_option

        action_details_log = {"type": action_type, "selector_input": selector_str, "value": value, "key": key_to_press, "url": url_to_navigate}

        try:
            target_locator = None
            final_selector_used = None
            if selector_str and action_type not in ["navigate", "scroll"]: # Scroll might use selector for "into_view"
                possible_selectors = [s.strip() for s in selector_str.split(',') if s.strip()]
                if not possible_selectors and action_type != "press": # Press can be global
                     raise PlaywrightError(f"LLM provided an empty or invalid selector string: '{selector_str}'")

                for sel_option in possible_selectors:
                    try:
                        locator = page.locator(sel_option)
                        # Check for visibility, and enabled for interactive elements. Timeout quickly.
                        await locator.wait_for(state="visible", timeout=1500)
                        if action_type in ["click", "fill", "type", "press", "select_option"]:
                            await locator.wait_for(state="enabled", timeout=1500)
                        target_locator = locator
                        final_selector_used = sel_option
                        logger.info(f"ActionExecutor: Using selector '{final_selector_used}' for action '{action_type}'.")
                        break
                    except Exception:
                        logger.debug(f"ActionExecutor: Selector option '{sel_option}' not visible/enabled within timeout.")
                        continue

                if not target_locator and action_type not in ["press"]: # Global press is allowed
                    raise PlaywrightError(f"None of the suggested selectors found or were ready: {possible_selectors}")

            action_taken_message = ""
            if action_type == "click":
                if not target_locator: raise PlaywrightError("No element found for click.")
                await target_locator.click(timeout=5000)
                action_taken_message = f"Clicked element: {final_selector_used}"
            elif action_type == "fill":
                if not target_locator: raise PlaywrightError("No element found for fill.")
                await target_locator.fill(value or "", timeout=5000)
                action_taken_message = f"Filled element '{final_selector_used}'."
            elif action_type == "type":
                if not target_locator: raise PlaywrightError("No element found for type.")
                await target_locator.type(value or "", delay=50, timeout=10000)
                action_taken_message = f"Typed into element '{final_selector_used}'."
            elif action_type == "press":
                if key_to_press is None: raise ValueError("'key' parameter is required for 'press' action.")
                if target_locator:
                    await target_locator.press(key_to_press, timeout=5000)
                    action_taken_message = f"Pressed key '{key_to_press}' on element '{final_selector_used}'."
                else: # Global key press
                    await page.keyboard.press(key_to_press)
                    action_taken_message = f"Pressed key '{key_to_press}' globally."
            elif action_type == "navigate":
                if not url_to_navigate: raise ValueError("URL required for navigate action.")
                await page.goto(url_to_navigate, timeout=60000, wait_until="domcontentloaded")
                action_taken_message = f"Navigated to {url_to_navigate}."
            elif action_type == "scroll":
                if scroll_direction == "into_view":
                    if not target_locator: raise PlaywrightError("Selector required for scroll 'into_view'.")
                    await target_locator.scroll_into_view_if_needed(timeout=5000)
                    action_taken_message = f"Scrolled element '{final_selector_used}' into view."
                elif scroll_direction == "down": await page.mouse.wheel(0, 800) # Increased scroll amount
                elif scroll_direction == "up": await page.mouse.wheel(0, -800)
                elif scroll_direction == "bottom": await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                elif scroll_direction == "top": await page.evaluate("window.scrollTo(0, 0)")
                else: raise ValueError(f"Invalid scroll_direction: {scroll_direction}")
                action_taken_message = f"Scrolled page {scroll_direction}."
            elif action_type == "select_option":
                if not target_locator: raise PlaywrightError("No element found for select_option.")
                if option_value is None: raise ValueError("'option_value' required for select_option.")
                await target_locator.select_option(value=option_value) # Can also select by label or index
                action_taken_message = f"Selected option '{option_value}' in '{final_selector_used}'."
            else: # Should have been caught by earlier check if action_type was invalid from LLM
                return {"status": "error", "message": f"Unsupported action_type: {action_type}", "parsed_action": parsed_action}

            await asyncio.sleep(0.2) # Short pause for page to settle after action
            # await page.wait_for_load_state("networkidle", timeout=3000) # Or networkidle if more stability needed

            logger.info(f"ActionExecutor: Successfully executed: {action_taken_message}")
            return {"status": "success", "action_taken": action_taken_message, "target_url": page.url, "final_selector_used": final_selector_used}

        except Exception as pte:
            error_msg = f"Playwright Timeout during '{action_type}' on '{final_selector_used or selector_str}': Target not ready or action took too long. {str(pte)}"
            logger.warning(error_msg)
            return {"status": "error", "message": error_msg, "details": action_details_log}
        except PlaywrightError as pe:
            error_msg = f"Playwright Error during '{action_type}' on '{final_selector_used or selector_str}': {str(pe)}"
            logger.warning(error_msg) # Log as warning as it might be due to bad selector from LLM
            return {"status": "error", "message": error_msg, "details": action_details_log}
        except Exception as e:
            error_msg = f"Unexpected error during '{action_type}': {str(e)}"
            logger.error(error_msg, exc_info=True)
            return {"status": "error", "message": error_msg, "details": action_details_log}

    async def _get_relevant_page_content_for_extraction(self, page: PWPage, instruction: str, max_chars: int = 8000) -> str:
        """
        Attempts to get relevant page content for extraction.
        Could be improved with LLM-guided snippet selection or by looking at elements matching parts of the instruction.
        For now, similar to _get_simplified_page_content_for_llm but potentially longer.
        """
        logger.info(f"Extraction: Getting page content for {page.url} based on instruction: '{instruction[:50]}...'")
        try:
            # A more advanced version might try to find a container element based on the instruction,
            # or use a visual model if Stagehand's full capabilities were being replicated.
            # For now, use a slightly more generous version of simplified content.

            # Try to get main content areas first
            main_content_selectors = ["article", "main", "[role='main']", "body"]
            content = ""
            for selector in main_content_selectors:
                try:
                    elements = await page.locator(selector).all()
                    if not elements: continue

                    # Get text from the first few matched main content elements
                    temp_content = []
                    for el in elements[:2]: # Limit to first 2 main-like elements
                         element_text = await el.inner_text(timeout=1500)
                         if element_text and element_text.strip():
                             temp_content.append(element_text.strip())

                    content = "\n\n".join(temp_content)
                    if content.strip():
                        logger.debug(f"ActionExecutor: Extracted content from selector '{selector}'. Initial length: {len(content)}")
                        break
                except Exception:
                    continue

            if not content or not content.strip():
                logger.info("ActionExecutor: Main content selectors yielded no text, falling back to body's full inner_text for extraction.")
                content = await page.locator("body").inner_text(timeout=5000) # Longer timeout for full body

            # Basic cleaning: replace multiple newlines/spaces with single space
            content = re.sub(r'\s\s+', ' ', content.replace('\n', ' ')).strip()

            if len(content) > max_chars:
                logger.warning(f"ActionExecutor: Page content for LLM extraction truncated from {len(content)} to {max_chars} chars.")
                # More intelligent truncation might be needed (e.g., summarize, or keep start/end)
                return content[:max_chars] + " ... (content truncated)"

            return content if content.strip() else "Page content appears to be empty or non-textual."
        except Exception as e:
            logger.error(f"ActionExecutor: Error getting page content for extraction: {e}", exc_info=True)
            return f"Error extracting page content: {e}"

    async def _get_simplified_page_content_for_llm(self, page: PWPage, max_chars: int = 4000) -> str:
        """
        Attempts to get a summarized or relevant portion of the page content for the LLM.
        This is a simplified version. Stagehand/Crawl4AI have more sophisticated methods.
        """
        try:
            # Try to get main content areas first
            main_content_selectors = ["article", "main", "[role='main']", "body"] # Add more as needed
            content = ""
            for selector in main_content_selectors:
                try:
                    element = page.locator(selector).first
                    await element.wait_for(state="attached", timeout=1000) # Wait briefly for element
                    content = await element.inner_text(timeout=2000) # Get text content
                    if content and content.strip():
                        print(f"ActionExecutor: Extracted content from selector '{selector}'. Length: {len(content)}")
                        break
                except PlaywrightError: # Element not found or timeout
                    continue
                except Exception: # Other errors
                    continue

            if not content or not content.strip(): # Fallback to full page text if main content is empty
                print("ActionExecutor: Main content selectors yielded no text, falling back to body's inner text.")
                content = await page.locator("body").inner_text(timeout=3000)

            # Clean up excessive newlines and whitespace
            content = re.sub(r'\s\s+', ' ', content.replace('\n', ' ')).strip()

            if len(content) > max_chars:
                print(f"ActionExecutor: Page content for LLM truncated from {len(content)} to {max_chars} chars.")
                return content[:max_chars] + "..."
            return content if content.strip() else "Page content seems to be empty or primarily non-textual."
        except Exception as e:
            print(f"ActionExecutor: Error getting simplified page content: {e}")
            return f"Error extracting page content: {e}"
    async def extract_data(self, page: PWPage, instruction: str, schema: Optional[Dict] = None) -> Dict[str, Any]:
        logger.info(f"ActionExecutor: Attempting data extraction. Instruction: '{instruction[:100]}...', Schema provided: {bool(schema)}")

        page_content = await self._get_relevant_page_content_for_extraction(page, instruction)

        if "Error extracting page content" in page_content or "Page content appears to be empty" in page_content:
            return {"status": "error", "message": "Could not retrieve sufficient page content for extraction.", "extracted_data": {}}

        prompt_parts = [
            f"Web Page Content:\n---\n{page_content}\n---\n",
            f"User Instruction for Extraction: {instruction}\n"
        ]
        if schema:
            prompt_parts.append(f"Desired JSON Schema (extract data strictly according to this schema):\n```json\n{json.dumps(schema, indent=2)}\n```\n")
        else:
            prompt_parts.append("No specific JSON schema provided. Extract the requested information into a logical JSON structure.\n")

        prompt_parts.append("Respond ONLY with the JSON object containing the extracted data. Do not include explanations or apologies if data is missing.")

        full_prompt = "".join(prompt_parts)

        messages = [
            {"role": "system", "content": DATA_EXTRACTION_SYSTEM_PROMPT},
            {"role": "user", "content": full_prompt}
        ]
        logger.debug(f"ActionExecutor LLM Prompt for data extraction (first 500 chars):\n{full_prompt[:500]}...")

        max_retries = 2
        for attempt in range(max_retries + 1):
            try:
                completion = await asyncio.to_thread(
                    self.llm_client.chat.completions.create,
                    model=self.extraction_llm_model, # Use dedicated model if configured
                    messages=messages,
                    response_format={"type": "json_object"},
                    temperature=0.0 # Low temp for factual extraction
                )
                extracted_json_str = completion.choices[0].message.content

                # Attempt to parse the JSON
                extracted_data = json.loads(extracted_json_str)
                logger.info(f"ActionExecutor: Successfully extracted data: {json.dumps(extracted_data, indent=2, ensure_ascii=False)}")
                return {"status": "success", "extracted_data": extracted_data, "schema_used": bool(schema)}
            except json.JSONDecodeError as jde:
                logger.warning(f"ActionExecutor: LLM returned invalid JSON for extraction (attempt {attempt+1}/{max_retries+1}): {extracted_json_str}. Error: {jde}")
                if attempt == max_retries:
                    return {"status": "error", "message": "LLM failed to return valid JSON after multiple attempts.", "raw_output": extracted_json_str}
            except BadRequestError as bre:
                 logger.error(f"ActionExecutor (Extract LLM): OpenAI BadRequestError: {bre}. Instruction: '{instruction}'")
                 return {"status": "error", "message": f"OpenAI API request error (likely input too long or malformed): {str(bre)}", "raw_output": None}
            except APIError as apie:
                logger.error(f"ActionExecutor (Extract LLM): OpenAI APIError: {apie}. Instruction: '{instruction}'")
                if attempt == max_retries:
                    return {"status": "error", "message": f"OpenAI APIError during extraction: {str(apie)}"}
            except Exception as e:
                logger.error(f"ActionExecutor: Unexpected error during extraction LLM call (attempt {attempt+1}): {e}", exc_info=True)
                if attempt == max_retries:
                    return {"status": "error", "message": f"Unexpected error during extraction: {str(e)}"}

            if attempt < max_retries:
                await asyncio.sleep((2**attempt) + np.random.rand()) # Exponential backoff

        return {"status": "error", "message": "Failed to extract data after multiple attempts (reached end of loop)."}