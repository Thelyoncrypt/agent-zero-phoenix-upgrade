# Phoenix Agent System - Manual E2E Testing Checklist

This checklist provides a comprehensive guide for manually testing the Phoenix Agent System through the Svelte UI. Use this alongside the automated E2E tests for thorough validation.

## Pre-Testing Setup

### ✅ System Requirements
- [ ] Phoenix backend running (`python run_ui.py`)
- [ ] Svelte frontend running (`npm run dev` in frontend directory)
- [ ] Environment variables configured (`.env` file)
- [ ] Supabase database accessible
- [ ] Required API keys available (OpenAI, etc.)
- [ ] Browser with WebSocket support (Chrome, Firefox, Safari)

### ✅ Initial Connectivity
- [ ] Navigate to `http://localhost:5173`
- [ ] UI loads without JavaScript errors (check browser console)
- [ ] WebSocket connection established (check network tab)
- [ ] "Phoenix is ready" message appears

---

## Scenario 1: RAG Pipeline Test

### 🎯 Objective
Test web crawling, knowledge ingestion, and RAG-based question answering.

### 📋 Steps
1. **Web Crawling & Ingestion**
   - [ ] Send message: "Crawl and index the content from https://docs.python.org/3/tutorial/introduction.html"
   - [ ] Observe ToolCallCard for WebCrawlerTool appears
   - [ ] Check for CRAWL_PROGRESS events in browser console
   - [ ] Wait for crawl completion confirmation
   - [ ] Verify no errors in backend logs

2. **Knowledge Query**
   - [ ] Send message: "What does the Python tutorial say about using Python as a calculator?"
   - [ ] Observe ToolCallCard for knowledge retrieval tool
   - [ ] Check response contains relevant information about Python calculator usage
   - [ ] Verify response is sourced from crawled content

### ✅ Success Criteria
- [ ] Crawling completes without errors
- [ ] Knowledge ingestion successful
- [ ] Query returns accurate, sourced information
- [ ] UI displays all tool calls properly

---

## Scenario 2: Browser Automation & Memory

### 🎯 Objective
Test browser automation, data extraction, and memory operations.

### 📋 Steps
1. **Browser Data Extraction**
   - [ ] Send message: "Use the browser to go to https://example.com and tell me the page title"
   - [ ] Observe ToolCallCard for BrowserAgentTool
   - [ ] Check for BROWSER_ACTION_STEP events
   - [ ] Verify extracted page title is correct

2. **Memory Storage**
   - [ ] Send message: "Remember that I tested the browser functionality today"
   - [ ] Observe ToolCallCard for MemoryAgentTool
   - [ ] Check for MEMORY_UPDATE event
   - [ ] Verify memory storage confirmation

3. **Memory Retrieval**
   - [ ] Send message: "What did I tell you about testing today?"
   - [ ] Verify response includes browser testing information
   - [ ] Check memory retrieval tool usage

### ✅ Success Criteria
- [ ] Browser navigation successful
- [ ] Data extraction accurate
- [ ] Memory storage and retrieval working
- [ ] All tool calls display properly in UI

---

## Scenario 3: Multi-Step Browser Task

### 🎯 Objective
Test complex browser automation with agent_execute functionality.

### 📋 Steps
1. **Complex Browser Task**
   - [ ] Send message: "Use the browser to search for 'weather London' on Google and tell me what you find"
   - [ ] Observe multiple BrowserActionStepCards in ToolCallCard
   - [ ] Check for sequential browser actions (navigate, type, click, extract)
   - [ ] Verify task completion with weather information

2. **Re-planning (if applicable)**
   - [ ] Watch for any plan failures and re-planning attempts
   - [ ] Verify UI shows re-planning status updates
   - [ ] Check final task completion

### ✅ Success Criteria
- [ ] Multiple browser steps executed
- [ ] Task completed successfully
- [ ] Weather information extracted
- [ ] UI shows all browser action steps

---

## Scenario 4: TTS Streaming & Audio

### 🎯 Objective
Test text-to-speech generation and audio streaming playback.

### 📋 Steps
1. **Text Response Generation**
   - [ ] Send message: "Explain photosynthesis briefly"
   - [ ] Verify text response received
   - [ ] Check response quality and accuracy

2. **TTS Request**
   - [ ] Send message: "Read your last answer aloud"
   - [ ] Observe ToolCallCard for ChatterboxTTSTool
   - [ ] Check AudioPlaybackControl appears
   - [ ] Click anywhere on page to enable AudioContext (if needed)

3. **Audio Playback**
   - [ ] Verify status shows "Buffering audio..." then "Playing speech..."
   - [ ] Confirm audio plays through speakers/headphones
   - [ ] Test "Stop" button functionality
   - [ ] Check status updates to "Speech finished" when complete

### ✅ Success Criteria
- [ ] TTS generation successful
- [ ] Audio streaming works
- [ ] Playback controls functional
- [ ] Audio quality acceptable

---

## Scenario 5: Code Execution with Live Output

### 🎯 Objective
Test code execution with real-time output streaming.

### 📋 Steps
1. **Python Code Execution**
   - [ ] Send message: "Run this Python code: for i in range(3): import time; print(f'Count: {i}'); time.sleep(0.5)"
   - [ ] Observe ToolCallCard for code_execution tool
   - [ ] Check "Execution Output" section appears
   - [ ] Verify live output updates in real-time

2. **Output Verification**
   - [ ] Confirm output shows "Count: 0", "Count: 1", "Count: 2"
   - [ ] Check auto-scrolling works
   - [ ] Verify exit code displays (should be 0 for success)
   - [ ] Test copy output functionality

3. **Error Handling**
   - [ ] Send message: "Run this Python code: print('test'); raise ValueError('test error')"
   - [ ] Verify stderr output appears in red
   - [ ] Check exit code shows error (non-zero)

### ✅ Success Criteria
- [ ] Code executes successfully
- [ ] Live output streaming works
- [ ] Auto-scrolling functional
- [ ] Error handling proper
- [ ] Exit codes display correctly

---

## Scenario 6: Settings & Chat Management

### 🎯 Objective
Test settings viewing and chat management operations.

### 📋 Steps
1. **Basic Chat Functionality**
   - [ ] Send several test messages
   - [ ] Verify responses received
   - [ ] Check message history displays correctly

2. **Settings Access (if implemented)**
   - [ ] Open settings modal/panel
   - [ ] Verify settings display properly
   - [ ] Check no sensitive data exposed

3. **Chat Management (if implemented)**
   - [ ] Create new chat session
   - [ ] Switch between chat sessions
   - [ ] Test chat renaming
   - [ ] Test chat deletion

### ✅ Success Criteria
- [ ] Basic chat functionality works
- [ ] Settings accessible and secure
- [ ] Chat management operations successful

---

## UI/UX Testing

### 📱 Responsive Design
- [ ] Test on desktop (1920x1080)
- [ ] Test on tablet (768x1024)
- [ ] Test on mobile (375x667)
- [ ] Verify all components scale properly

### 🎨 Visual Design
- [ ] Neumorphic styling consistent
- [ ] Color scheme appropriate
- [ ] Typography readable
- [ ] Icons display correctly
- [ ] Animations smooth

### ⚡ Performance
- [ ] Page loads quickly (<3 seconds)
- [ ] Scrolling smooth
- [ ] No memory leaks during extended use
- [ ] WebSocket reconnection works

### ♿ Accessibility
- [ ] Keyboard navigation works
- [ ] Screen reader compatibility
- [ ] Color contrast sufficient
- [ ] Focus indicators visible

---

## Error Handling & Edge Cases

### 🚨 Network Issues
- [ ] Disconnect internet, verify graceful handling
- [ ] Reconnect, verify auto-reconnection
- [ ] Test with slow network conditions

### 🔧 Backend Issues
- [ ] Stop backend, verify error messages
- [ ] Restart backend, verify reconnection
- [ ] Test with backend errors

### 📱 Browser Issues
- [ ] Refresh page during operation
- [ ] Test with browser back/forward
- [ ] Test with multiple tabs

---

## Performance Benchmarks

### ⏱️ Response Times
- [ ] Simple message response: <5 seconds
- [ ] Web crawling: <30 seconds
- [ ] Browser automation: <45 seconds
- [ ] Code execution: <10 seconds
- [ ] TTS generation: <15 seconds

### 💾 Resource Usage
- [ ] Memory usage stable over time
- [ ] CPU usage reasonable
- [ ] Network usage appropriate
- [ ] No memory leaks detected

---

## Final Validation

### ✅ Overall System Health
- [ ] All scenarios completed successfully
- [ ] No critical errors in logs
- [ ] UI responsive and stable
- [ ] All features functional

### 📊 Test Results Summary
- **Total Scenarios**: 6
- **Passed**: ___/6
- **Failed**: ___/6
- **Critical Issues**: ___
- **Minor Issues**: ___

### 📝 Notes & Observations
```
[Add any additional observations, issues, or recommendations here]
```

---

## Troubleshooting Guide

### Common Issues
1. **WebSocket Connection Failed**
   - Check backend is running on correct port
   - Verify firewall settings
   - Check browser console for errors

2. **Tool Calls Not Appearing**
   - Verify StreamProtocol events in network tab
   - Check socketStore event handling
   - Verify ToolCallCard component

3. **Audio Not Playing**
   - Click page to enable AudioContext
   - Check browser audio permissions
   - Verify TTS model availability

4. **Code Execution Fails**
   - Check Python/Node.js installation
   - Verify execution permissions
   - Check backend logs for errors

### Getting Help
- Check browser console for JavaScript errors
- Review backend logs for Python exceptions
- Verify all environment variables set
- Ensure all dependencies installed
