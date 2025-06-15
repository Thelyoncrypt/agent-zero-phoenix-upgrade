# tool.py - Base tool class for Agent Zero tools
from typing import Optional, Dict, Any
from dataclasses import dataclass

@dataclass
class Response:
    """Standard response format for tool execution"""
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    message: Optional[str] = None
    break_loop: bool = False

class Tool:
    """Base class for all Agent Zero tools"""
    
    def __init__(self, agent, name: str, description: str, args_schema: Optional[Dict[str, Any]] = None, **kwargs):
        self.agent = agent
        self.name = name
        self.description = description
        self.args_schema = args_schema
        
    async def execute(self, *args, **kwargs) -> Response:
        """Execute the tool - to be implemented by subclasses"""
        raise NotImplementedError("Tool subclasses must implement the execute method")
        
    def __str__(self):
        return f"Tool({self.name}): {self.description}"
        
    def __repr__(self):
        return f"<Tool name='{self.name}' description='{self.description}'>"