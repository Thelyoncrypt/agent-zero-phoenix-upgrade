# python/tools/browser_agent_tool.py
from python.helpers.tool import Tool, Response as ToolResponse
import json
import asyncio
import logging
from typing import Dict, Any, Optional

logger = logging.getLogger(__name__)

# Constants for robust agent execution
MAX_AGENT_EXECUTE_ITERATIONS = 7 # Max iterations of planning/execution for a single agent_execute call
MAX_SUB_ACTIONS_PER_PLAN_SEGMENT = 5 # Max sub-actions per single plan from LLM

# Import StreamProtocol components if available
try:
    from python.tools.stream_protocol_tool import StreamEventType
    STREAM_PROTOCOL_AVAILABLE = True
except ImportError:
    STREAM_PROTOCOL_AVAILABLE = False
    StreamEventType = None

# Import browser agent components - with actual BrowserManager
from python.agents.browser_agent.browser import BrowserManager
from python.agents.browser_agent.ai_models import AIModelProvider
from python.agents.browser_agent.actions import ActionExecutor

# Import Playwright errors if available
try:
    from playwright.async_api import Error as PlaywrightError, TimeoutError as PlaywrightTimeoutError, Page as PWPage
    PLAYWRIGHT_ERROR_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_ERROR_AVAILABLE = False
    PlaywrightError = Exception  # Fallback to generic exception
    PlaywrightTimeoutError = Exception
    PWPage = None

class BrowserAgentTool(Tool):
    """
    BrowserAgent (Stagehand inspired) integration for Agent Zero.
    Provides AI-powered browser automation and computer use capabilities using Playwright.
    """
    
    _browser_manager_instance: Optional[BrowserManager] = None  # Class-level singleton for manager

    @classmethod
    def get_browser_manager(cls, headless: bool = True, browser_type: str = "chromium", playwright_timeout: int = 30000) -> BrowserManager:
        """Get or create a shared BrowserManager instance."""
        if cls._browser_manager_instance is None:
            cls._browser_manager_instance = BrowserManager(
                headless=headless,
                browser_type=browser_type,
                playwright_timeout=playwright_timeout
            )
        return cls._browser_manager_instance
    
    def __init__(self, agent, **kwargs):
        super().__init__(
            agent=agent, 
            name="browser_agent", 
            description="Controls a browser to navigate, interact with web pages, and extract information using AI.",
            args_schema={
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["navigate", "act", "extract", "agent_execute", "get_page_content", "new_page", "close_page", "close_context_session"],
                        "description": "The browser action to perform"
                    },
                    "url": {
                        "type": "string",
                        "description": "URL to navigate to (for navigate action)"
                    },
                    "instructions": {
                        "type": "string",
                        "description": "Instructions for AI actions or data extraction"
                    },
                    "schema": {
                        "type": "object",
                        "description": "JSON schema for structured data extraction"
                    },
                    "session_id": {
                        "type": "string",
                        "description": "Browser session identifier (optional, defaults to thread_id)"
                    },
                    "page_index": {
                        "type": "integer",
                        "description": "Page index within the browser context (default: 0)"
                    },
                    "model": {
                        "type": "string",
                        "description": "AI model to use for computer use actions"
                    }
                },
                "required": ["action"]
            },
            **kwargs
        )
        
        # Initialize browser agent components
        # Use a shared BrowserManager instance
        # Headless mode can be configured via agent.config later
        self.browser_manager = BrowserAgentTool.get_browser_manager(
            headless=getattr(self.agent, 'config', {}).get("browser_headless", True),
            browser_type=getattr(self.agent, 'config', {}).get("browser_type", "chromium"),
            playwright_timeout=getattr(self.agent, 'config', {}).get("playwright_timeout", 30000)
        )
        self.ai_provider = AIModelProvider()  # Remains mock for now
        self.action_executor = ActionExecutor()  # Remains mock for now
        logger.info(f"BrowserAgentTool initialized for agent {agent.agent_name} (context: {agent.context.id}) with enhanced BrowserManager.")

    async def _emit_browser_event(self, action_name: str, status: str, details: Optional[Dict[str, Any]] = None):
        """Helper to emit browser_action events via StreamProtocolTool."""
        if not STREAM_PROTOCOL_AVAILABLE:
            print(f"BrowserAgentTool: StreamProtocol not available, logging event: {action_name} - {status}")
            return
            
        payload = {"action": action_name, "status": status}
        if details:
            payload.update(details)
        
        # Access StreamProtocolTool through the agent
        if hasattr(self.agent, '_emit_stream_event'):
            await self.agent._emit_stream_event(StreamEventType.BROWSER_ACTION, payload)
        else:
            print(f"BrowserAgentTool: Agent does not have _emit_stream_event method. Cannot emit BROWSER_ACTION.")

    async def execute(self, **kwargs) -> ToolResponse:
        """
        Execute BrowserAgent operations.
        
        Args:
            action (str): The browser action to perform (e.g., "navigate", "act", "extract").
            **kwargs: Arguments specific to the action.
        """
        action = kwargs.get("action")
        if not action:
            return ToolResponse(
                success=False,
                error="Missing required 'action' parameter",
                message="Error: 'action' is required for BrowserAgent operations."
            )
        
        # Ensure session_id is determined. Fallback to thread_id, then a default.
        session_id = kwargs.get("session_id", self.agent.get_thread_id())
        if not session_id:
            session_id = f"agent0_browser_ctx_{self.agent.context.id}"  # Fallback if no thread_id
        
        # page_index allows targeting specific pages in a multi-page context (default to 0)
        page_index = kwargs.get("page_index", 0)

        try:
            if action == "navigate":
                url = kwargs.get("url")
                if not url:
                    return ToolResponse(
                        success=False,
                        error="Missing 'url' parameter",
                        message="Error: 'url' is required for navigate action."
                    )
                return await self._navigate(url, session_id, page_index)
                
            elif action == "act":
                instructions = kwargs.get("instructions")
                if not instructions:
                    return ToolResponse(
                        success=False,
                        error="Missing 'instructions' parameter",
                        message="Error: 'instructions' are required for act action."
                    )
                page = await self._get_page_robustly(session_id, page_index, action)
                if not page:
                    return ToolResponse(
                        success=False,
                        error=f"Could not get page for session {session_id}, index {page_index}.",
                        message=f"Could not get page for session {session_id}, index {page_index}."
                    )
                return await self._ai_act(page, instructions, session_id, page_index) # Pass page

            elif action == "extract":
                instructions = kwargs.get("instructions")
                schema = kwargs.get("schema")  # Optional
                if not instructions:
                    return ToolResponse(
                        success=False,
                        error="Missing 'instructions' parameter",
                        message="Error: 'instructions' are required for extract action."
                    )
                page = await self._get_page_robustly(session_id, page_index, action)
                if not page:
                    return ToolResponse(
                        success=False,
                        error=f"Could not get page for session {session_id}, index {page_index}.",
                        message=f"Could not get page for session {session_id}, index {page_index}."
                    )
                return await self._extract(page, instructions, schema, session_id, page_index) # Pass page
                
            elif action == "agent_execute":  # Computer use agent
                instructions = kwargs.get("instructions")
                model = kwargs.get("model", "computer-use-preview")
                if not instructions:
                    return ToolResponse(
                        success=False,
                        error="Missing 'instructions' parameter",
                        message="Error: 'instructions' are required for agent_execute action."
                    )
                return await self._agent_execute(instructions, model, session_id)
                
            elif action == "get_page_content":  # New action: Get current page's simplified DOM/content
                page = await self._get_page_robustly(session_id, page_index, action)
                if not page:
                    return ToolResponse(
                        success=False,
                        error=f"Could not get page for session {session_id}, index {page_index}.",
                        message=f"Could not get page for session {session_id}, index {page_index}."
                    )
                return await self._get_page_content(page, session_id, page_index) # Pass page

            elif action == "new_page":  # New action: Open a new page in the context
                return await self._new_page(session_id)

            elif action == "close_page":  # New action: Close a specific page (by index or current)
                return await self._close_page(session_id, page_index)
                
            elif action == "close_context_session":  # Renamed from close_session for clarity
                return await self._close_context_session(session_id)
                
            else:
                return ToolResponse(
                    success=False,
                    error=f"Unknown action: {action}",
                    message=f"Unknown BrowserAgent action: {action}"
                )
                
        except PlaywrightError as pe: # Catch-all for Playwright errors not caught deeper
            error_message = f"BrowserAgentTool Playwright error during action '{action}': {str(pe)}"
            logger.error(error_message, exc_info=True)
            await self._emit_browser_event(action, "error", {"error": str(pe), "type": "PlaywrightError"})
            return ToolResponse(
                success=False,
                error=str(pe),
                message=error_message
            )
        except Exception as e:
            # Handle generic errors
            import traceback
            error_message = f"BrowserAgentTool error during action '{action}': {str(e)}"
            logger.error(error_message, exc_info=True)
            await self._emit_browser_event(action, "error", {"error": str(e)})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_message
            )

    async def _get_page_robustly(self, session_id: str, page_index: int, action_name: str) -> Optional[PWPage]:
        """Helper to get a page and emit error event if it fails."""
        page = await self.browser_manager.get_page(session_id, page_index, create_if_needed=True)
        if not page:
            await self._emit_browser_event(action_name, "error", {"error": f"Failed to get/create page {page_index} for session {session_id}"})
        return page

    async def _navigate(self, url: str, session_id: str, page_index: int) -> ToolResponse:
        """Navigate to a URL in the specified browser session using Playwright."""
        await self._emit_browser_event("navigate", "starting", {"url": url, "session_id": session_id, "page_index": page_index})

        page = await self._get_page_robustly(session_id, page_index, "navigate")
        if not page:
            return ToolResponse(
                success=False,
                error=f"Navigation failed: could not obtain page for session {session_id}, index {page_index}.",
                message=f"Navigation failed: could not obtain page for session {session_id}, index {page_index}."
            )

        try:
            logger.info(f"Navigating page (session: {session_id}, index: {page_index}) to URL: {url}")
            response = await page.goto(url, timeout=self.browser_manager.playwright_timeout, wait_until="domcontentloaded")
            current_url = page.url
            title = await page.title()
            status_code = response.status if response else None

            result_payload = {
                "url": current_url, "title": title, "status_code": status_code,
                "session_id": session_id, "page_index": page_index,
                "details": f"Successfully navigated to {current_url}"
            }
            await self._emit_browser_event("navigate", "completed", result_payload)
            return ToolResponse(
                success=True,
                data=result_payload,
                message=json.dumps(result_payload)
            )
        except PlaywrightTimeoutError:
            error_msg = f"Navigation to {url} timed out after {self.browser_manager.playwright_timeout/1000}s."
            logger.warning(error_msg)
            await self._emit_browser_event("navigate", "error", {"url": url, "error": "Timeout", "session_id": session_id})
            return ToolResponse(
                success=False,
                error="Timeout",
                message=error_msg
            )
        except PlaywrightError as e:
            error_msg = f"Navigation to {url} failed: {str(e)}"
            logger.error(error_msg, exc_info=True)
            await self._emit_browser_event("navigate", "error", {"url": url, "error": str(e), "session_id": session_id})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_msg
            )

    async def _ai_act(self, page: PWPage, instructions: str, session_id: str, page_index: int) -> ToolResponse:
        """Perform AI-powered actions on the current page."""
        action_name = "ai_act"
        await self._emit_browser_event(action_name, "processing", {"instructions": instructions, "session_id": session_id, "page_index": page_index})

        try:
            # ActionExecutor now uses AI (OpenAI) to translate instructions into Playwright actions
            act_result = await self.action_executor.execute_ai_action(page, instructions)  # Uses the passed page

            status = act_result.get("status", "error")
            message = act_result.get("message", "Action processing finished.")
            data_to_return = act_result # Return the full result dict as data

            if status == "success":
                await self._emit_browser_event(action_name, "completed", {"result": act_result, "session_id": session_id, "page_index": page_index})
                return ToolResponse(message=act_result.get("action_taken", message), data=data_to_return)
            elif status == "clarification_needed":
                await self._emit_browser_event(action_name, "clarification_needed", {"message": message, "details": act_result.get("details"), "session_id": session_id})
                # The agent loop will need to handle this type of response, perhaps by asking the user.
                return ToolResponse(message=f"Clarification needed: {message}", data=data_to_return, error=False, success=False) # Special status for agent
            else: # Error
                await self.agent._emit_stream_event(StreamEventType.ERROR_EVENT, {"source_tool": self.name, "action": action_name, "error": message, "details": act_result})
                return ToolResponse(message=message, error=True, data=data_to_return, success=False)
        except Exception as e:
            error_msg = f"Unexpected error during {action_name}: {str(e)}"
            logger.error(error_msg, exc_info=True)
            await self.agent._emit_stream_event(StreamEventType.ERROR_EVENT, {
                "source_tool": self.name, "action": action_name, "error": str(e), "type": "GenericException"
            })
            return ToolResponse(success=False, message=error_msg, error=str(e))

    async def _extract(self, page: PWPage, instructions: str, schema: Optional[Dict], session_id: str, page_index: int) -> ToolResponse:
        """Extract structured data from the current page."""
        action_name = "extract_data"
        await self._emit_browser_event(action_name, "processing", {"instructions": instructions, "schema_provided": bool(schema), "session_id": session_id, "page_index": page_index})

        # ActionExecutor.extract_data now contains the real LLM-based logic
        extract_result_dict = await self.action_executor.extract_data(page, instructions, schema)

        status = extract_result_dict.get("status", "error")
        message = extract_result_dict.get("message", "Data extraction processed.")

        if status == "success":
            await self._emit_browser_event(action_name, "completed", {"result_summary": {"keys_extracted": list(extract_result_dict.get("extracted_data", {}).keys())}, "session_id": session_id, "page_index": page_index})
            return ToolResponse(message="Data extracted successfully.", data=extract_result_dict.get("extracted_data"))
        else: # Error or other non-success status
            logger.error(f"BrowserAgentTool ({action_name}): Failed - {message}. Raw output: {extract_result_dict.get('raw_output')}")
            await self.agent._emit_stream_event(StreamEventType.ERROR_EVENT, {"source_tool": self.name, "action": action_name, "error": message, "details": extract_result_dict})
            return ToolResponse(message=message, error=True, data=extract_result_dict) # Pass full result for debugging

    async def _execute_sub_action_on_page(self, sub_action: Dict[str, Any], page: PWPage, session_id: str, current_page_index: int) -> ToolResponse:
        """Enhanced sub-action execution that takes a page object directly."""
        action_type = sub_action.get("action_type")
        logger.info(f"BrowserAgentTool: Executing sub-action ON PAGE '{page.url}': {action_type} with args {sub_action}")
        response_data = None
        error_flag = False
        message = ""

        try:
            if action_type == "navigate":
                nav_resp = await self._navigate(sub_action.get("url", ""), session_id, current_page_index)
                message, response_data, error_flag = nav_resp.message, nav_resp.data, nav_resp.error
            elif action_type == "act":
                act_resp = await self._ai_act(page, sub_action.get("instructions", ""), session_id, current_page_index)
                message, response_data, error_flag = act_resp.message, act_resp.data, act_resp.error
            elif action_type in ["type", "fill", "click", "press", "scroll", "select_option"]:
                instruction_for_act = f"{action_type} "
                if sub_action.get("selector"): instruction_for_act += f"on element '{sub_action['selector']}'"
                if sub_action.get("value"): instruction_for_act += f" with value '{sub_action['value']}'"
                act_resp = await self._ai_act(page, instruction_for_act.strip(), session_id, current_page_index)
                message, response_data, error_flag = act_resp.message, act_resp.data, act_resp.error
            elif action_type == "extract":
                extract_resp = await self._extract(page, sub_action.get("instructions", ""), sub_action.get("schema"), session_id, current_page_index)
                message, response_data, error_flag = extract_resp.message, extract_resp.data, extract_resp.error
            elif action_type == "report_finding":
                message = "Planner reported a finding."
                response_data = sub_action.get("finding")
            else:
                message = f"Unsupported sub-action type: {action_type}"; error_flag = True
        except Exception as e:
            message = f"Error executing sub-action {action_type}: {e}"; error_flag = True
            logger.error(message, exc_info=True)

        return ToolResponse(message=message, data=response_data, error=error_flag)

    async def _execute_sub_action(self, sub_action: Dict[str, Any], session_id: str, page_index: int) -> ToolResponse:
        """Helper to execute a single sub-action dict from the plan."""
        action_type = sub_action.get("action_type")
        print(f"BrowserAgentTool: Executing sub-action: {action_type} with args {sub_action}")

        if action_type == "navigate":
            return await self._navigate(sub_action.get("url", ""), session_id, page_index)
        elif action_type in ["click", "type", "fill", "press", "scroll", "select_option"]:
            # Use _ai_act for these, but provide more structured input if possible,
            # or rely on _ai_act's own LLM call to interpret based on "selector" and "value".
            # For a more direct execution without a second LLM call in _ai_act for *these specific* sub-actions:
            # We'd need to refactor _ai_act or add more direct Playwright execution methods here.
            # Let's assume for now we pass a precise instruction to _ai_act.
            instruction_for_act = f"{action_type} "
            if sub_action.get("selector"):
                instruction_for_act += f"on element '{sub_action['selector']}'"
            if sub_action.get("value"):
                instruction_for_act += f" with value '{sub_action['value']}'"
            if sub_action.get("key"):
                instruction_for_act += f" the key '{sub_action['key']}'"
            if sub_action.get("option_value"):
                instruction_for_act += f" option '{sub_action['option_value']}'"
            if sub_action.get("scroll_direction"):
                 instruction_for_act += f" direction '{sub_action['scroll_direction']}'"

            # Get page for this sub-action
            page = await self._get_page_robustly(session_id, page_index, f"sub_action_{action_type}")
            if not page:
                return ToolResponse(
                    success=False,
                    error=f"Could not get page for sub-action {action_type}",
                    message=f"Could not get page for sub-action {action_type}"
                )
            return await self._ai_act(page, instruction_for_act.strip(), session_id, page_index)

        elif action_type == "extract":
            # Get page for this sub-action
            page = await self._get_page_robustly(session_id, page_index, f"sub_action_{action_type}")
            if not page:
                return ToolResponse(
                    success=False,
                    error=f"Could not get page for sub-action {action_type}",
                    message=f"Could not get page for sub-action {action_type}"
                )
            return await self._extract(
                page,
                sub_action.get("instructions", ""),
                sub_action.get("schema"),
                session_id,
                page_index
            )
        elif action_type == "report_finding": # A special action type for the planner to signal completion
            return ToolResponse(
                success=True,
                data=sub_action.get("finding"),
                message="Finding reported by planner."
            )
        else:
            return ToolResponse(
                success=False,
                error=f"Unsupported sub-action type: {action_type}",
                message=f"Unsupported sub-action type: {action_type}"
            )

    async def _agent_execute(self, instructions: str, model_for_planner: str, session_id: str) -> ToolResponse:
        """
        Enhanced agent_execute with robust loop and basic re-planning feedback.
        Executes a high-level computer use instruction by decomposing it into
        a sequence of browser actions and executing them with iterative re-planning.
        """
        await self._emit_browser_event("agent_execute", "starting", {"goal": instructions, "planner_model": model_for_planner, "session_id": session_id})

        planner = await self.ai_provider.get_computer_use_planner() # AIModelProvider provides ComputerUsePlanner

        execution_summary: List[Dict[str, Any]] = []
        final_extracted_data_or_finding: Any = None
        current_page_idx_for_plan = 0 # Assume operations on the first/primary page of the context

        # Enhanced feedback tracking for re-planning
        previous_actions_feedback = "" # To accumulate feedback for re-planning
        total_sub_actions_executed = 0 # Track total sub-actions across all iterations
        goal_achieved = False # Track if goal has been achieved

        logger.info(f"BrowserAgentTool._agent_execute: Starting robust execution loop for goal: '{instructions}'")

        for iteration in range(MAX_AGENT_EXECUTE_ITERATIONS):
            logger.info(f"BrowserAgentTool._agent_execute: Iteration {iteration + 1}/{MAX_AGENT_EXECUTE_ITERATIONS}")

            # Get current page context for planning
            page_for_context = await self._get_page_robustly(session_id, current_page_idx_for_plan, f"agent_execute_context_iteration_{iteration}")
            page_content_summary = "No current page context available."
            if page_for_context:
                try:
                    page_content_summary = await self.action_executor._get_page_summary_for_llm(page_for_context)
                except Exception as e:
                    logger.warning(f"Failed to get page summary: {e}")
                    page_content_summary = f"Page available but summary failed: {str(e)}"
            else:
                error_msg = f"Cannot proceed with planning: failed to obtain page (session: {session_id}, index: {current_page_idx_for_plan})."
                logger.error(error_msg)
                await self._emit_browser_event("agent_execute", "error", {"goal": instructions, "error": error_msg, "session_id": session_id})
                return ToolResponse(message=error_msg, data={"completed_sub_actions": execution_summary, "total_sub_actions": total_sub_actions_executed}, error=True)

            # Get plan from LLM with feedback from previous actions
            try:
                sub_actions_plan = await planner.decompose_task(instructions, page_content_summary, previous_actions_feedback)
            except Exception as e:
                error_msg = f"Planner failed to decompose task: {str(e)}"
                logger.error(error_msg, exc_info=True)
                await self._emit_browser_event("agent_execute", "error", {"goal": instructions, "error": error_msg, "session_id": session_id})
                return ToolResponse(message=error_msg, data={"completed_sub_actions": execution_summary, "total_sub_actions": total_sub_actions_executed}, error=True)

            # Handle empty plan (goal complete or cannot proceed)
            if not sub_actions_plan:
                msg = f"Planner returned empty plan on iteration {iteration + 1}. Goal may be complete or cannot proceed further."
                logger.info(f"BrowserAgentTool._agent_execute: {msg}")
                goal_achieved = True
                await self._emit_browser_event("agent_execute", "completed_empty_plan", {
                    "goal": instructions, "iteration": iteration + 1, "summary": execution_summary,
                    "final_data": final_extracted_data_or_finding, "session_id": session_id
                })
                break

            # Handle planner error
            if sub_actions_plan and sub_actions_plan[0].get("action_type") == "error":
                error_msg = sub_actions_plan[0].get("message", "Planner failed to decompose task.")
                logger.error(f"BrowserAgentTool._agent_execute: Planner error on iteration {iteration + 1} - {error_msg}")
                await self._emit_browser_event("agent_execute", "error", {"goal": instructions, "error": error_msg, "session_id": session_id})
                return ToolResponse(message=error_msg, data={"completed_sub_actions": execution_summary, "total_sub_actions": total_sub_actions_executed}, error=True)

            # Limit sub-actions per plan segment
            if len(sub_actions_plan) > MAX_SUB_ACTIONS_PER_PLAN_SEGMENT:
                logger.warning(f"Plan has {len(sub_actions_plan)} sub-actions, limiting to {MAX_SUB_ACTIONS_PER_PLAN_SEGMENT}")
                sub_actions_plan = sub_actions_plan[:MAX_SUB_ACTIONS_PER_PLAN_SEGMENT]

            await self._emit_browser_event("agent_execute", "plan_generated", {
                "goal": instructions, "iteration": iteration + 1, "plan": sub_actions_plan,
                "plan_size": len(sub_actions_plan), "session_id": session_id
            })

            # Execute the plan
            iteration_feedback = f"Iteration {iteration + 1} feedback:\n"
            plan_success = True

            for i, sub_action_spec in enumerate(sub_actions_plan):
                total_sub_actions_executed += 1
                step_number_overall = len(execution_summary) + 1

                # Safety check for total sub-actions
                if total_sub_actions_executed > MAX_AGENT_EXECUTE_ITERATIONS * MAX_SUB_ACTIONS_PER_PLAN_SEGMENT:
                    logger.warning("BrowserAgentTool._agent_execute: Exceeded maximum total sub-actions limit.")
                    await self._emit_browser_event("agent_execute", "error", {"goal": instructions, "error": "Max total sub-actions limit reached.", "session_id": session_id})
                    return ToolResponse(message="Max total sub-actions limit reached.", data={"summary": execution_summary, "total_sub_actions": total_sub_actions_executed}, error=True)

                await self._emit_browser_event("agent_execute_sub_action", "starting", {
                    "iteration": iteration + 1, "overall_step": step_number_overall, "plan_step_index": i,
                    "sub_action": sub_action_spec, "session_id": session_id
                })

                # Get page for sub-action execution
                page_for_sub_action = await self._get_page_robustly(session_id, current_page_idx_for_plan, f"agent_execute_sub_action_{step_number_overall}")
                if not page_for_sub_action:
                    error_msg = f"Sub-action failed: Could not get page for session {session_id}, index {current_page_idx_for_plan}."
                    iteration_feedback += f"  Step {step_number_overall} ({action_type}): Failed - {error_msg}\n"
                    execution_summary.append({"iteration": iteration + 1, "step": step_number_overall, "action_spec": sub_action_spec, "result_message": error_msg, "error": True})
                    await self._emit_browser_event("agent_execute_sub_action", "error", {"iteration": iteration + 1, "overall_step": step_number_overall, "error": error_msg, "session_id": session_id})
                    plan_success = False
                    continue # Continue with next sub-action

                # Execute the sub-action
                try:
                    sub_action_response = await self._execute_sub_action_on_page(sub_action_spec, page_for_sub_action, session_id, current_page_idx_for_plan)
                except Exception as e:
                    error_msg = f"Exception during sub-action execution: {str(e)}"
                    logger.error(error_msg, exc_info=True)
                    sub_action_response = ToolResponse(success=False, error=str(e), message=error_msg)

                # Record execution result
                current_step_summary = {
                    "iteration": iteration + 1,
                    "step": step_number_overall,
                    "action_spec": sub_action_spec,
                    "result_message": sub_action_response.message,
                    "error": sub_action_response.error,
                    "success": sub_action_response.success,
                    "data": sub_action_response.data
                }
                execution_summary.append(current_step_summary)

                # Build feedback for next iteration
                action_type = sub_action_spec.get("action_type", "unknown")
                result_status = "Success" if sub_action_response.success else "Failure"
                iteration_feedback += f"  Step {step_number_overall} ({action_type}): {result_status} - {sub_action_response.message}\n"

                # Handle sub-action results
                if sub_action_response.error:
                    error_msg = f"Sub-action step {step_number_overall} ('{action_type}') failed: {sub_action_response.message}"
                    logger.warning(f"BrowserAgentTool._agent_execute: {error_msg}")
                    await self._emit_browser_event("agent_execute_sub_action", "error", {
                        "iteration": iteration + 1, "overall_step": step_number_overall, "error": error_msg, "session_id": session_id
                    })
                    plan_success = False
                    # Continue with remaining sub-actions to gather more feedback
                elif sub_action_spec.get("action_type") == "report_finding":
                    # Goal achieved
                    final_extracted_data_or_finding = sub_action_response.data
                    goal_achieved = True
                    logger.info(f"BrowserAgentTool._agent_execute: Goal achieved with report_finding action.")
                else:
                    # Successful sub-action
                    await self._emit_browser_event("agent_execute_sub_action", "completed", {
                        "iteration": iteration + 1, "overall_step": step_number_overall,
                        "result_data": sub_action_response.data, "session_id": session_id
                    })
                    if sub_action_response.data:
                        final_extracted_data_or_finding = sub_action_response.data

            # Update feedback for next iteration
            previous_actions_feedback += iteration_feedback

            # Check if goal is achieved
            if goal_achieved:
                logger.info(f"BrowserAgentTool._agent_execute: Goal achieved after iteration {iteration + 1}")
                break

            # If this was the last iteration, break
            if iteration == MAX_AGENT_EXECUTE_ITERATIONS - 1:
                logger.warning(f"BrowserAgentTool._agent_execute: Reached maximum iterations ({MAX_AGENT_EXECUTE_ITERATIONS})")
                break

        # Final result compilation
        success_message = f"Agent execution for '{instructions}' completed after {len(execution_summary)} steps across {iteration + 1} iterations."
        if goal_achieved:
            success_message += " Goal achieved."
        else:
            success_message += " Maximum iterations reached."

        if final_extracted_data_or_finding:
            success_message += f" Final data: {json.dumps(final_extracted_data_or_finding) if isinstance(final_extracted_data_or_finding, (dict, list)) else str(final_extracted_data_or_finding)}"

        result_data = {
            "summary": execution_summary,
            "final_data": final_extracted_data_or_finding,
            "total_sub_actions": total_sub_actions_executed,
            "iterations_completed": iteration + 1,
            "goal_achieved": goal_achieved
        }

        await self._emit_browser_event("agent_execute", "completed", {
            "goal": instructions, "summary": execution_summary, "final_data": final_extracted_data_or_finding,
            "total_sub_actions": total_sub_actions_executed, "iterations": iteration + 1, "session_id": session_id
        })

        return ToolResponse(
            success=True,
            message=success_message,
            data=result_data
        )

    async def _get_page_content(self, page: PWPage, session_id: str, page_index: int) -> ToolResponse:
        """Gets the HTML content of the current page."""
        await self._emit_browser_event("get_page_content", "processing", {"session_id": session_id, "page_index": page_index})
        try:
            content = await page.content(timeout=10000)  # Increased timeout slightly
            title = await page.title()
            url = page.url
            # Simplified content for now, real parsing/markdown conversion would be more complex
            simplified_content = content[:2000] + ("..." if len(content) > 2000 else "")
            result_payload = {"url": url, "title": title, "content_snippet_html": simplified_content, "session_id": session_id, "page_index": page_index}
            await self._emit_browser_event("get_page_content", "completed", result_payload)
            return ToolResponse(
                success=True,
                data=result_payload,
                message=json.dumps(result_payload)
            )
        except PlaywrightError as e:
            error_msg = f"Failed to get page content: {str(e)}"
            logger.error(error_msg, exc_info=True)
            await self._emit_browser_event("get_page_content", "error", {"error": str(e), "session_id": session_id})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_msg
            )

    async def _new_page(self, session_id: str) -> ToolResponse:
        """Opens a new page in the specified browser context and returns its index."""
        await self._emit_browser_event("new_page", "processing", {"session_id": session_id})
        page = await self.browser_manager.new_page_in_context(session_id)
        context = await self.browser_manager.get_context(session_id)
        new_page_index = len(context.pages) - 1
        result_payload = {"session_id": session_id, "new_page_index": new_page_index, "url": page.url, "title": await page.title()}
        await self._emit_browser_event("new_page", "completed", result_payload)
        return ToolResponse(
            success=True,
            data=result_payload,
            message=json.dumps(result_payload)
        )

    async def _close_page(self, session_id: str, page_index: int) -> ToolResponse:
        """Closes a specific page in the browser context."""
        await self._emit_browser_event("close_page", "processing", {"session_id": session_id, "page_index": page_index})
        await self.browser_manager.close_page_in_context(session_id, page_index)
        # Note: After closing a page, page indices of subsequent pages in the context might shift.
        # The client or agent needs to be aware of this or always fetch pages by a unique ID if Playwright provided one.
        # For now, we assume a simple list-based indexing.
        await self._emit_browser_event("close_page", "completed", {"session_id": session_id, "closed_page_index": page_index})
        return ToolResponse(
            success=True,
            data={"session_id": session_id, "closed_page_index": page_index},
            message=f"Page at index {page_index} in session {session_id} closed request processed."
        )

    async def _close_context_session(self, session_id: str) -> ToolResponse:
        """Close a browser context session."""
        await self._emit_browser_event("close_context_session", "processing", {"session_id": session_id})
        await self.browser_manager.close_context(session_id)
        await self._emit_browser_event("close_context_session", "completed", {"session_id": session_id})
        return ToolResponse(
            success=True,
            data={"session_id": session_id},
            message=f"Browser context session {session_id} closed."
        )