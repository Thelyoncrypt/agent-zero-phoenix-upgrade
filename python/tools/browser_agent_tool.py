# python/tools/browser_agent_tool.py
from python.helpers.tool import Tool, Response as ToolResponse
import json
from typing import Dict, Any, Optional

# Import StreamProtocol components if available
try:
    from python.tools.stream_protocol_tool import StreamEventType
    STREAM_PROTOCOL_AVAILABLE = True
except ImportError:
    STREAM_PROTOCOL_AVAILABLE = False
    StreamEventType = None

# Import browser agent components
from python.agents.browser_agent.browser import BrowserManager
from python.agents.browser_agent.ai_models import AIModelProvider
from python.agents.browser_agent.actions import ActionExecutor

class BrowserAgentTool(Tool):
    """
    BrowserAgent (Stagehand inspired) integration for Agent Zero.
    Provides AI-powered browser automation and computer use capabilities.
    """
    
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
                        "enum": ["navigate", "act", "extract", "agent_execute", "close_session"],
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
                        "description": "Browser session identifier (optional)"
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
        self.browser_manager = BrowserManager()
        self.ai_provider = AIModelProvider()
        self.action_executor = ActionExecutor()
        print(f"BrowserAgentTool initialized for agent {agent.agent_name} (context: {agent.context.id})")

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
        
        session_id = kwargs.get("session_id", self.agent.get_thread_id() or "default_browser_session")

        try:
            if action == "navigate":
                url = kwargs.get("url")
                if not url:
                    return ToolResponse(
                        success=False,
                        error="Missing 'url' parameter",
                        message="Error: 'url' is required for navigate action."
                    )
                return await self._navigate(url, session_id)
                
            elif action == "act":
                instructions = kwargs.get("instructions")
                if not instructions:
                    return ToolResponse(
                        success=False,
                        error="Missing 'instructions' parameter",
                        message="Error: 'instructions' are required for act action."
                    )
                return await self._ai_act(instructions, session_id)
                
            elif action == "extract":
                instructions = kwargs.get("instructions")
                schema = kwargs.get("schema")  # Optional
                if not instructions:
                    return ToolResponse(
                        success=False,
                        error="Missing 'instructions' parameter",
                        message="Error: 'instructions' are required for extract action."
                    )
                return await self._extract(instructions, schema, session_id)
                
            elif action == "agent_execute":  # Computer use agent
                instructions = kwargs.get("instructions")
                model = kwargs.get("model", "computer-use-preview")
                if not instructions:
                    return ToolResponse(
                        success=False,
                        error="Missing 'instructions' parameter",
                        message="Error: 'instructions' are required for agent_execute action."
                    )
                return await self._agent_execute(instructions, model)
                
            elif action == "close_session":
                return await self._close_session(session_id)
                
            else:
                return ToolResponse(
                    success=False,
                    error=f"Unknown action: {action}",
                    message=f"Unknown BrowserAgent action: {action}"
                )
                
        except Exception as e:
            import traceback
            error_message = f"BrowserAgentTool error during action '{action}': {str(e)}"
            print(f"{error_message}\n{traceback.format_exc()}")
            await self._emit_browser_event(action, "error", {"error": str(e)})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_message
            )

    async def _navigate(self, url: str, session_id: str) -> ToolResponse:
        """Navigate to a URL in the specified browser session."""
        await self._emit_browser_event("navigate", "starting", {"url": url, "session_id": session_id})
        
        browser_mock = await self.browser_manager.get_browser(session_id)
        page_mock = await browser_mock.new_page()  # Ensure a fresh page context for navigation
        nav_result = await page_mock.goto(url)
        
        result_payload = {
            "url": page_mock.url, 
            "title": await page_mock.title(), 
            "session_id": session_id,
            "details": f"Mock navigation to {url} successful."
        }
        await self._emit_browser_event("navigate", "completed", result_payload)
        return ToolResponse(
            success=True,
            data=result_payload,
            message=json.dumps(result_payload)
        )

    async def _ai_act(self, instructions: str, session_id: str) -> ToolResponse:
        """Perform AI-powered actions on the current page."""
        await self._emit_browser_event("ai_act", "processing", {"instructions": instructions, "session_id": session_id})
        
        browser_mock = await self.browser_manager.get_browser(session_id)
        page_mock = browser_mock.page  # Get current page of the session
        
        act_result = await self.action_executor.execute_ai_action(page_mock, instructions)
        
        await self._emit_browser_event("ai_act", "completed", {"result": act_result, "session_id": session_id})
        return ToolResponse(
            success=True,
            data=act_result,
            message=json.dumps(act_result)
        )

    async def _extract(self, instructions: str, schema: Optional[Dict], session_id: str) -> ToolResponse:
        """Extract structured data from the current page."""
        await self._emit_browser_event("extract_data", "processing", {"instructions": instructions, "session_id": session_id})

        browser_mock = await self.browser_manager.get_browser(session_id)
        page_mock = browser_mock.page
        
        extract_result = await self.action_executor.extract_data(page_mock, instructions, schema)
        
        await self._emit_browser_event("extract_data", "completed", {"result": extract_result, "session_id": session_id})
        return ToolResponse(
            success=True,
            data=extract_result,
            message=json.dumps(extract_result)
        )

    async def _agent_execute(self, instructions: str, model: str) -> ToolResponse:
        """Execute computer use instructions using AI model."""
        session_id = self.agent.get_thread_id() or "default_computer_use_session"
        await self._emit_browser_event("agent_execute", "processing", {"instructions": instructions, "model": model, "session_id": session_id})

        # Use the AI model provider for computer use agent
        computer_agent_mock = await self.ai_provider.get_computer_use_agent(model)
        exec_result = await computer_agent_mock.execute(instructions)
        
        await self._emit_browser_event("agent_execute", "completed", {"result": exec_result, "session_id": session_id})
        return ToolResponse(
            success=True,
            data=exec_result,
            message=json.dumps(exec_result)
        )

    async def _close_session(self, session_id: str) -> ToolResponse:
        """Close a browser session."""
        await self._emit_browser_event("close_session", "processing", {"session_id": session_id})
        await self.browser_manager.close_browser(session_id)
        await self._emit_browser_event("close_session", "completed", {"session_id": session_id})
        return ToolResponse(
            success=True,
            data={"session_id": session_id},
            message=f"Browser session {session_id} closed."
        )