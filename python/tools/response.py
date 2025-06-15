# response.py - Response tool for Agent Zero with StreamProtocol integration
from python.helpers.tool import Tool, Response as ToolResponse
from typing import Dict, Any

class ResponseTool(Tool):
    """Tool for providing final responses to users with StreamProtocol integration"""
    
    def __init__(self, agent, **kwargs):
        super().__init__(
            agent=agent,
            name="response",
            description="Provides the final response to the user and ends the conversation loop",
            args_schema={
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The final response text to send to the user"
                    }
                },
                "required": ["text"]
            },
            **kwargs
        )
    
    async def execute(self, **kwargs) -> ToolResponse:
        """Execute the response tool and emit appropriate events"""
        text_content = kwargs.get("text", "No response content provided.")
        
        print(f"ResponseTool: Providing final response: {text_content[:100]}...")
        
        # Create response object that signals loop completion
        response = ToolResponse(
            success=True,
            data={"message": text_content, "break_loop": True},
            message=text_content
        )
        
        # Add break_loop attribute for compatibility
        response.break_loop = True
        
        return response

# For backward compatibility and direct usage
class Response(ToolResponse):
    """Extended response class with break_loop support"""
    
    def __init__(self, message: str, break_loop: bool = False, **kwargs):
        super().__init__(success=True, message=message, **kwargs)
        self.break_loop = break_loop