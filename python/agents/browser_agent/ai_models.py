# python/agents/browser_agent/ai_models.py
import asyncio
import json
from typing import Dict, Any, List, Optional
import os
import numpy as np
from openai import OpenAI, APIError, RateLimitError
from dotenv import load_dotenv
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

project_root = Path(__file__).resolve().parents[2]
dotenv_path = project_root / '.env'
load_dotenv(dotenv_path, override=True)

TASK_DECOMPOSITION_SYSTEM_PROMPT = """
You are an expert planner for web browser automation.
Given a high-level user goal, break it down into a sequence of specific, simple browser actions.
Each action in the sequence should be one of the following types: "navigate", "type", "fill", "click", "press", "extract", "scroll", "select_option".
For each action, provide the necessary parameters (e.g., 'url' for navigate, 'selector' and 'value' for type/fill, 'instructions' and 'schema' for extract).
The 'selector' should be a best-guess CSS selector.
The 'extract' action should define what information to get and optionally a JSON schema for the output.
The final step should usually be an 'extract' action to get the information needed to answer the user's goal, or a 'report_finding' action with the finding.

Respond with a JSON list of action objects. Example:
[
    {"action_type": "navigate", "url": "https://google.com"},
    {"action_type": "type", "selector": "textarea[name=q]", "value": "NVIDIA stock price"},
    {"action_type": "press", "selector": "textarea[name=q]", "key": "Enter"},
    {"action_type": "extract", "instructions": "Extract the current stock price for NVIDIA.", "schema": {"type": "object", "properties": {"stock_price": {"type": "string"}}}}
]

If the goal seems too complex for a short sequence or requires non-browser actions, indicate that.
If the goal is simple and can be achieved by a single action, output a list with that single action.
"""

class ComputerUsePlanner:
    def __init__(self, model_name: Optional[str] = None):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.llm_model = model_name or os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        if not self.api_key:
            raise ValueError("OpenAI API key required for ComputerUsePlanner.")
        self.llm_client = OpenAI(api_key=self.api_key)
        logger.info(f"ComputerUsePlanner: Initialized with OpenAI model '{self.llm_model}'.")

    async def decompose_task(self,
                             high_level_goal: str,
                             page_context_summary: Optional[str] = None,
                             previous_actions_feedback: Optional[str] = None # Renamed for clarity
                             ) -> List[Dict[str, Any]]:
        """
        Decomposes a high-level goal into a sequence of browser sub-actions using an LLM.
        """
        logger.info(f"ComputerUsePlanner: Decomposing task: '{high_level_goal}'.")
        if previous_actions_feedback:
            logger.info(f"ComputerUsePlanner: With previous actions feedback:\n{previous_actions_feedback}")

        context_info = f"Current Page Context:\n{page_context_summary}\n---\n" if page_context_summary else "No current page context available.\n---\n"
        if previous_actions_feedback:
            # Make it clear this is feedback, not just a summary of successful past actions
            context_info += f"Feedback from previously executed actions for this goal:\n{previous_actions_feedback}\n---\n"

        prompt = f"""
        {context_info}
        User's high-level goal: "{high_level_goal}"

        Based on the current page context and feedback from any previously executed actions for this goal, determine the next best sequence of specific browser sub-actions to achieve the goal.
        If previous actions failed, try to adjust the plan or suggest an alternative.
        If the goal seems complete based on previous actions, you can return an empty list or a single "report_finding" action with the consolidated result.
        If stuck or unable to proceed, use "action_type": "clarify" or "action_type": "error" with a descriptive message.
        Output a JSON list of action objects.
        """
        messages = [
            {"role": "system", "content": TASK_DECOMPOSITION_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]

        max_retries = 2
        for attempt in range(max_retries):
            try:
                response = await asyncio.to_thread(
                    self.llm_client.chat.completions.create,
                    model=self.llm_model,
                    messages=messages,
                    response_format={"type": "json_object"},
                    temperature=0.2
                )
                plan_json_str = response.choices[0].message.content
                # The LLM is asked to return a list directly, so we expect the "json_object" to be a list.
                # If it's wrapped in a dict like {"plan": [...]}, we need to adjust.
                # For now, assume it returns the list as the root JSON object.
                parsed_plan = json.loads(plan_json_str)
                if isinstance(parsed_plan, list): # Check if the root is a list
                    logger.info(f"ComputerUsePlanner: Decomposed plan: {parsed_plan}")
                    return parsed_plan
                elif isinstance(parsed_plan, dict) and "plan" in parsed_plan and isinstance(parsed_plan["plan"], list):
                    logger.info(f"ComputerUsePlanner: Decomposed plan (from dict): {parsed_plan['plan']}")
                    return parsed_plan["plan"] # Handle if LLM wraps it
                else:
                    logger.warning(f"ComputerUsePlanner: LLM returned unexpected JSON structure for plan: {parsed_plan}")
                    return [{"action_type": "error", "message": "LLM returned unexpected plan structure."}]
            except json.JSONDecodeError:
                logger.warning(f"ComputerUsePlanner: LLM returned invalid JSON for plan (attempt {attempt+1}): {plan_json_str}")
                if attempt == max_retries - 1:
                    return [{"action_type": "error", "message": "LLM failed to return valid JSON plan."}]
            except Exception as e:
                logger.error(f"ComputerUsePlanner: Error calling LLM for task decomposition (attempt {attempt+1}): {e}", exc_info=True)
                if attempt == max_retries - 1:
                    return [{"action_type": "error", "message": f"LLM error during task decomposition: {str(e)}"}]

            if attempt < max_retries - 1:
                 await asyncio.sleep((2**attempt) + np.random.rand())

        return [{"action_type": "error", "message": "Failed to decompose task after multiple attempts."}]

class AIModelProvider:
    """
    Manages AI models for browser automation.
    """
    def __init__(self):
        print("AIModelProvider: Initialized.")
        try:
            self.computer_use_planner = ComputerUsePlanner() # Initialize the planner
        except ValueError as e:
            print(f"AIModelProvider: Warning - {e}. ComputerUsePlanner will not be available.")
            self.computer_use_planner = None

    async def get_computer_use_agent(self, model_name: str = "computer-use-preview"):
        print(f"AIModelProvider: Mocking get_computer_use_agent for model {model_name}")
        return ComputerUseAgentMock(model_name)

    async def get_computer_use_planner(self) -> Optional[ComputerUsePlanner]:
        # In a real scenario, model_name might be passed to select different planner configurations
        if self.computer_use_planner is None:
            raise ValueError("ComputerUsePlanner is not available. Please ensure OpenAI API key is configured.")
        return self.computer_use_planner

class ComputerUseAgentMock:
    def __init__(self, model_name: str):
        self.model_name = model_name
        print(f"ComputerUseAgentMock initialized with model: {model_name}")

    async def execute(self, instructions: str) -> Dict[str, Any]:
        print(f"ComputerUseAgentMock: Executing instructions: '{instructions[:100]}...'")
        # Simulate some action
        if "login" in instructions.lower():
            return {"status": "success", "action_taken": "simulated login", "details": "Logged in to mock service."}
        elif "search" in instructions.lower():
            return {"status": "success", "action_taken": "simulated search", "results_summary": "Found 3 mock results."}
        else:
            return {"status": "success", "action_taken": "simulated generic action", "details": f"Processed: {instructions[:50]}"}

class ComputerUseAgentMock:
    def __init__(self, model_name: str):
        self.model_name = model_name
        print(f"ComputerUseAgentMock initialized with model: {model_name}")

    async def execute(self, instructions: str) -> Dict[str, Any]:
        print(f"ComputerUseAgentMock: Executing instructions: '{instructions[:100]}...'")
        # Simulate some action
        if "login" in instructions.lower():
            return {"status": "success", "action_taken": "simulated login", "details": "Logged in to mock service."}
        elif "search" in instructions.lower():
            return {"status": "success", "action_taken": "simulated search", "results_summary": "Found 3 mock results."}
        else:
            return {"status": "success", "action_taken": "simulated generic action", "details": f"Processed: {instructions[:50]}"}