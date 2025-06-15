# run_ui.py - Agent Zero UI server with StreamProtocol WebSocket support
import asyncio
import json
import os
from flask import Flask, request, jsonify
from flask_sock import Sock
from werkzeug.serving import run_simple

# Mock imports for Agent Zero helpers (these would be real imports in actual Agent Zero)
class runtime:
    @staticmethod
    def initialize():
        print("Runtime initialized")
    
    @staticmethod
    def get_port():
        return int(os.environ.get('PORT', 8080))
    
    @staticmethod
    def get_host():
        return os.environ.get('HOST', '0.0.0.0')
    
    @staticmethod
    def is_development():
        return os.environ.get('FLASK_ENV') != 'production'

class dotenv:
    @staticmethod
    def load_dotenv():
        print("Environment variables loaded")

class settings:
    @staticmethod
    def initialize_settings():
        print("Settings initialized")

class api:
    @staticmethod
    def initialize_api_handlers(app):
        """Initialize API handlers - mock implementation"""
        @app.route('/api/message', methods=['POST'])
        def api_message():
            return jsonify({"status": "received", "message": "Mock API response"})
        
        @app.route('/api/poll', methods=['GET'])
        def api_poll():
            return jsonify({"status": "idle", "data": None})
        
        @app.route('/api/agui/run', methods=['POST'])
        async def api_agui_run():
            """Handle AG-UI RunAgentInput requests"""
            try:
                from python.agent import AgentContext, Agent
                from python.tools.stream_protocol_tool import StreamProtocolTool
                
                data = request.get_json()
                thread_id = data.get('threadId')
                user_id = data.get('userId')
                context_id = data.get('contextId', thread_id)
                
                # Get or create agent context
                context = AgentContext.get(id=context_id, thread_id=thread_id, user_id=user_id)
                context.set_custom_data('stream_transport_instance', app.stream_transport_global)
                
                # Create agent if not exists
                if not context.agent0:
                    context.agent0 = Agent(
                        agent_id=f"agent_{context_id}",
                        agent_name="StreamAgent",
                        context=context
                    )
                
                # Create StreamProtocolTool and handle input
                stream_tool = StreamProtocolTool(context.agent0)
                result = await stream_tool.execute(action="handle_input", input_data=data)
                
                return jsonify(result)
                
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        print("API handlers initialized")

# Import StreamProtocol components
from python.tools.stream_protocol_tool import StreamEvent, StreamEventType, RunAgentInput, StreamProtocolTool
from python.agent import AgentContext, Agent
import uuid
from datetime import datetime
from typing import Dict, Any, List, Optional

# Initialize Flask app
app = Flask("agent-zero-ui")
app.config["JSON_SORT_KEYS"] = False
sock = Sock(app)

class StreamTransportGlobal:
    """
    Manages WebSocket connections and dispatches events to relevant clients.
    This instance is global to the server application.
    """
    def __init__(self):
        self.connections: Dict[str, List[Any]] = {}  # thread_id -> list of websocket objects
        self.connection_details: Dict[str, Dict[str, Any]] = {} # ws_connection_id -> details
        self.lock = asyncio.Lock()
        print("StreamTransportGlobal: Instance created.")

    async def register_connection(self, ws, thread_id: str, user_id: Optional[str] = None) -> str:
        connection_id = str(uuid.uuid4())
        async with self.lock:
            if thread_id not in self.connections:
                self.connections[thread_id] = []
            self.connections[thread_id].append(ws)
            self.connection_details[connection_id] = {
                "websocket": ws, "thread_id": thread_id, "user_id": user_id, "connected_at": datetime.utcnow()
            }
        print(f"StreamTransportGlobal: Registered WS connection {connection_id} for thread '{thread_id}'. Total for thread: {len(self.connections[thread_id])}")
        return connection_id

    async def unregister_connection(self, connection_id: str):
        async with self.lock:
            if connection_id in self.connection_details:
                connection_info = self.connection_details.pop(connection_id)
                ws_to_remove = connection_info["websocket"]
                thread_id = connection_info["thread_id"]
                
                if thread_id in self.connections:
                    try:
                        self.connections[thread_id].remove(ws_to_remove)
                        if not self.connections[thread_id]: # Is list empty?
                            del self.connections[thread_id]
                        print(f"StreamTransportGlobal: Unregistered WS connection {connection_id} from thread '{thread_id}'. Remaining: {len(self.connections.get(thread_id, []))}")
                    except ValueError:
                        print(f"StreamTransportGlobal: WS to remove not found in thread '{thread_id}' list.")

    async def emit_event_to_thread(self, event: StreamEvent):
        """Emit event to all clients connected to the specified event.thread_id."""
        if not event.thread_id or event.thread_id not in self.connections:
            # print(f"StreamTransportGlobal: No active connections for thread_id {event.thread_id} to emit event {event.type.value}")
            return

        event_data_str = json.dumps({
            "id": event.event_id, "type": event.type.value, "payload": event.payload,
            "timestamp": event.timestamp, "threadId": event.thread_id, "userId": event.user_id
        })
        
        disconnected_ws = []
        async with self.lock: # Protect access to self.connections list for the thread
            # Iterate over a copy of the list if modifications are made during iteration
            for ws in list(self.connections.get(event.thread_id, [])): 
                try:
                    if not ws.closed: # Check if websocket is still open
                        await ws.send(event_data_str)
                    else:
                        print(f"StreamTransportGlobal: WebSocket for thread {event.thread_id} was closed. Marking for removal.")
                        disconnected_ws.append(ws)
                except Exception as e:
                    print(f"StreamTransportGlobal: Error sending to WebSocket for thread {event.thread_id}: {e}. Marking for removal.")
                    disconnected_ws.append(ws)
        
        # Clean up disconnected WebSockets
        if disconnected_ws:
            async with self.lock:
                for ws in disconnected_ws:
                    try:
                        if event.thread_id in self.connections:
                            self.connections[event.thread_id].remove(ws)
                    except ValueError:
                        pass # Already removed
                if event.thread_id in self.connections and not self.connections[event.thread_id]:
                    del self.connections[event.thread_id]

# Create and store the global StreamTransport instance
app.stream_transport_global = StreamTransportGlobal()

# Modify ApiHandler to inject the transport instance into AgentContext
# This ensures that any AgentContext created through API requests has access to the global transport
try:
    from python.helpers.api import ApiHandler
    
    original_api_handler_get_context = ApiHandler.get_context
    def patched_get_context(api_handler_self, ctxid: Optional[str] = None, name: Optional[str] = None, 
                            thread_id: Optional[str] = None, user_id: Optional[str] = None) -> AgentContext:
        # Call original method to get/create context
        if hasattr(original_api_handler_get_context, '__func__'):
            # Handle bound method
            context = original_api_handler_get_context.__func__(api_handler_self, ctxid)
        else:
            # Handle unbound function
            context = original_api_handler_get_context(api_handler_self, ctxid)
        
        # Inject the global stream transport instance
        if 'stream_transport_instance' not in context.custom_data:
            context.set_custom_data('stream_transport_instance', app.stream_transport_global)
            print(f"Patched_get_context: Injected stream_transport_global into context {context.id}")
        return context
    
    ApiHandler.get_context = patched_get_context # Monkey-patch the method
    print("ApiHandler.get_context patched successfully")
    
except ImportError as e:
    print(f"Could not patch ApiHandler: {e}")

# New WebSocket route for AG-UI streaming
@sock.route('/ws/agui/<string:thread_id>')
async def agui_websocket(ws, thread_id: str):
    """
    WebSocket endpoint for AG-UI protocol communication.
    Clients connect to ws://server/ws/agui/{thread_id}
    """
    user_id = request.args.get('userId')  # Optional user_id from query params
    context_id_for_agent = request.args.get('contextId', thread_id)  # Use thread_id as context_id if not specified

    # Get the global StreamTransport instance
    transport = app.stream_transport_global 
    
    connection_id = await transport.register_connection(ws, thread_id, user_id)
    print(f"WebSocket connection opened: id={connection_id}, thread_id={thread_id}, user_id={user_id}")

    try:
        # Get or create AgentContext. This ensures the context is aware of the thread_id and user_id.
        context = AgentContext.get(id=context_id_for_agent, thread_id=thread_id, user_id=user_id)
        context.set_custom_data('stream_transport_instance', transport)
        
        # Create agent if not exists
        if not context.agent0:
            context.agent0 = Agent(
                agent_id=f"agent_{context_id_for_agent}",
                agent_name="StreamAgent",
                context=context
            )

        # Send a session_start event to indicate WebSocket connection is ready
        initial_state_payload = {"threadId": thread_id, "userId": user_id, "status": "connected"}
        init_event = StreamEvent(StreamEventType.SESSION_START, initial_state_payload, thread_id=thread_id, user_id=user_id)
        await transport.emit_event_to_thread(init_event)

        while True:
            # This loop primarily listens for client messages (e.g., client-side pings, control messages)
            # Most AG-UI events are server-to-client, pushed via transport.emit_event()
            try:
                # Set a timeout to prevent blocking indefinitely if the client is silent
                message_str = await asyncio.wait_for(ws.receive(), timeout=60.0) 
                if message_str is None:  # Connection closed by client
                    print(f"WebSocket client for thread {thread_id} (conn: {connection_id}) sent None, closing.")
                    break 

                print(f"WebSocket (thread {thread_id}, conn: {connection_id}) received: {message_str[:200]}")
                
                # Handle incoming messages if the AG-UI protocol defines client-to-server messages
                try:
                    data = json.loads(message_str)
                    if data.get("type") == "ping":
                        await ws.send(json.dumps({"type": "pong"}))
                    elif data.get("action") == "run_agent_input_ws":
                        # Handle RunAgentInput directly over WebSocket
                        stream_tool = StreamProtocolTool(context.agent0)
                        await stream_tool.execute(action="handle_input", input_data=data.get("payload", {}))

                except json.JSONDecodeError:
                    print(f"WebSocket (thread {thread_id}, conn: {connection_id}) received invalid JSON: {message_str[:200]}")
                except Exception as e_inner:
                    print(f"WebSocket (thread {thread_id}, conn: {connection_id}) error processing message: {e_inner}")

            except asyncio.TimeoutError:
                # No message received in timeout period, check if connection is still alive
                if hasattr(ws, 'closed') and ws.closed:
                    print(f"WebSocket (thread {thread_id}, conn: {connection_id}) detected closed during timeout.")
                    break
                # Continue listening
                pass
            except Exception as e_outer:
                print(f"WebSocket (thread {thread_id}, conn: {connection_id}) receive error: {e_outer}")
                break

    except Exception as e:
        print(f"WebSocket error for thread {thread_id} (conn: {connection_id}): {e}")
    finally:
        await transport.unregister_connection(connection_id)
        print(f"WebSocket connection closed: id={connection_id}, thread_id={thread_id}")

# Health check endpoint
@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "websocket_endpoint": "/ws/agui/<thread_id>",
        "active_connections": len(app.stream_transport_global.connections)
    })

# Serve basic UI
@app.route('/')
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Agent Zero with StreamProtocol</title>
    </head>
    <body>
        <h1>Agent Zero StreamProtocol Server</h1>
        <p>WebSocket endpoint: <code>ws://localhost:8080/ws/agui/&lt;thread_id&gt;</code></p>
        <p>HTTP API endpoint: <code>POST /api/agui/run</code></p>
        <p>Health check: <a href="/health">/health</a></p>
        
        <script>
            // Simple WebSocket test
            function testWebSocket() {
                const threadId = 'test-thread-' + Date.now();
                const ws = new WebSocket(`ws://localhost:8080/ws/agui/${threadId}?userId=test-user`);
                
                ws.onopen = function() {
                    console.log('WebSocket connected');
                    ws.send(JSON.stringify({type: 'ping'}));
                };
                
                ws.onmessage = function(event) {
                    console.log('Received:', event.data);
                };
                
                ws.onclose = function() {
                    console.log('WebSocket closed');
                };
                
                ws.onerror = function(error) {
                    console.error('WebSocket error:', error);
                };
            }
            
            console.log('To test WebSocket, run: testWebSocket()');
        </script>
    </body>
    </html>
    """

if __name__ == "__main__":
    # Initialize runtime
    runtime.initialize()
    dotenv.load_dotenv()
    
    # Initialize settings and API handlers
    settings.initialize_settings()
    api.initialize_api_handlers(app)

    port = runtime.get_port()
    host = runtime.get_host()
    
    print(f"Agent Zero UI starting on http://{host}:{port}")
    print(f"WebSocket endpoint available at ws://{host}:{port}/ws/agui/<thread_id>")
    print(f"HTTP API endpoint available at http://{host}:{port}/api/agui/run")

    if runtime.is_development():
        # Flask's built-in server with flask-sock works well for dev
        app.run(host=host, port=port, debug=False, threaded=True)
    else:
        print("Production server setup would need specific configuration for WebSockets.")
        print("Running with Flask's development server for now.")
        app.run(host=host, port=port, debug=False, threaded=True)