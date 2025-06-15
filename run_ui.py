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
                context.set_custom_data('stream_transport', app.stream_transport)
                
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
from python.tools.stream_protocol_tool import StreamTransport, RunAgentInput, StreamProtocolTool
from python.agent import AgentContext, Agent

# Initialize Flask app
app = Flask("agent-zero-ui")
app.config["JSON_SORT_KEYS"] = False
sock = Sock(app)

# Create and store the global StreamTransport instance
app.stream_transport = StreamTransport()

# New WebSocket route for AG-UI streaming
@sock.route('/ws/agui/<string:thread_id>')
async def agui_websocket(ws, thread_id: str):
    \"\"\"
    WebSocket endpoint for AG-UI protocol communication.
    Clients connect to ws://server/ws/agui/{thread_id}
    \"\"\"
    user_id = request.args.get('userId')  # Optional user_id from query params
    context_id_for_agent = request.args.get('contextId', thread_id)  # Use thread_id as context_id if not specified

    # Get the global StreamTransport instance
    transport = app.stream_transport 
    
    connection_id = await transport.register_connection(ws, thread_id, user_id)
    print(f"WebSocket connection opened: id={connection_id}, thread_id={thread_id}, user_id={user_id}")

    try:
        # Get or create AgentContext. This ensures the context is aware of the thread_id and user_id.
        context = AgentContext.get(id=context_id_for_agent, thread_id=thread_id, user_id=user_id)
        context.set_custom_data('stream_transport', transport)
        
        # Create agent if not exists
        if not context.agent0:
            context.agent0 = Agent(
                agent_id=f"agent_{context_id_for_agent}",
                agent_name="StreamAgent",
                context=context
            )

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
        "active_connections": len(app.stream_transport.connections)
    })

# Serve basic UI
@app.route('/')
def index():
    return \"\"\"
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
    \"\"\"

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