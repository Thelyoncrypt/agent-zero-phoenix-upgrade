# api.py - API helpers for Agent Zero with StreamProtocol support
from typing import Optional
from python.agent import AgentContext

try:
    from flask import current_app
    FLASK_AVAILABLE = True
except ImportError:
    FLASK_AVAILABLE = False
    current_app = None

class ApiHandler:
    """Handler for Agent Zero API operations"""
    
    def __init__(self):
        self.contexts = {}
    
    def get_context(self, ctxid: Optional[str] = None) -> AgentContext:
        """
        Get or create an AgentContext with Flask app integration
        When getting/creating a context, ensure it knows about the app instance
        if it's within a Flask request context.
        """
        context = AgentContext.get(ctxid)
        
        # Set Flask app instance in context if available
        if FLASK_AVAILABLE and current_app and 'flask_app_instance' not in context.custom_data:
            try:
                context.set_custom_data('flask_app_instance', current_app._get_current_object())
                
                # Also set the stream_transport_instance if available
                if hasattr(current_app, 'stream_transport_global'):
                    context.set_custom_data('stream_transport_instance', current_app.stream_transport_global)
            except RuntimeError:
                # Outside of Flask request context
                pass
        
        return context
    
    def create_context(self, name: str = None, thread_id: str = None, user_id: str = None) -> AgentContext:
        """Create a new context with optional parameters"""
        context = AgentContext.get(name=name, thread_id=thread_id, user_id=user_id)
        
        # Set Flask app integration if available
        if FLASK_AVAILABLE and current_app:
            try:
                context.set_custom_data('flask_app_instance', current_app._get_current_object())
                if hasattr(current_app, 'stream_transport_global'):
                    context.set_custom_data('stream_transport_instance', current_app.stream_transport_global)
            except RuntimeError:
                pass
        
        return context