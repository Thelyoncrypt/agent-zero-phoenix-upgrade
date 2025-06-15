# prompts/default/agent.system.tool.browser.md
### browser_agent:
# 
# subordinate agent controls playwright browser
# message argument talks to agent give clear instructions credentials task based
# reset argument spawns new agent
# do not reset if iterating
# be precise descriptive like: open google login and end task, log in using ... and end task
# when following up start: considering open pages
# dont use phrase wait for instructions use end task
# downloads default in /a0/tmp/downloads
# 
# Usage for specific actions:
# To navigate:
# {
#   "tool_name": "browser_agent",
#   "tool_args": { "action": "navigate", "url": "https://example.com", "session_id": "optional_session_name" }
# }
# To perform AI actions on the current page:
# {
#   "tool_name": "browser_agent",
#   "tool_args": { "action": "act", "instructions": "Click the 'Login' button and then type 'testuser' into the username field.", "session_id": "optional_session_name" }
# }
# To extract structured data:
# {
#   "tool_name": "browser_agent",
#   "tool_args": { 
#     "action": "extract", 
#     "instructions": "Extract the article title and author name.", 
#     "schema": { "type": "object", "properties": { "title": {"type": "string"}, "author": {"type": "string"} } },
#     "session_id": "optional_session_name" 
#   }
# }
# To use computer use agent for complex tasks:
# {
#   "tool_name": "browser_agent",
#   "tool_args": { "action": "agent_execute", "instructions": "Find the latest NVIDIA stock price and save it to a file named stock_price.txt." }
# }
# To close a browser session:
# {
#  "tool_name": "browser_agent",
#  "tool_args": { "action": "close_session", "session_id": "session_to_close" }
# }
#
# If session_id is omitted, a default session related to the current conversation/thread will be used.