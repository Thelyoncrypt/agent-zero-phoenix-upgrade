# Phoenix Agent System - End-to-End Testing Guide

This comprehensive guide provides everything needed to execute thorough E2E testing of the Phoenix Agent System.

## 🚀 Quick Start

### Prerequisites
1. **System Requirements**
   ```bash
   # Python 3.8+
   python --version
   
   # Node.js 16+
   node --version
   npm --version
   ```

2. **Install Dependencies**
   ```bash
   # Python dependencies
   pip install -r requirements.txt
   
   # Frontend dependencies
   cd frontend
   npm install
   cd ..
   ```

3. **Environment Configuration**
   ```bash
   # Copy and configure environment variables
   cp .env.example .env
   # Edit .env with your API keys
   ```

### Quick Health Check
```bash
# Run system health check
python system_health_check.py

# Quick connectivity test
python run_e2e_tests.py --quick
```

### Start System Components
```bash
# Terminal 1: Start backend
python run_ui.py

# Terminal 2: Start frontend
cd frontend
npm run dev
```

---

## 🧪 Automated E2E Testing

### Full Test Suite
```bash
# Run all E2E test scenarios
python run_e2e_tests.py
```

### Individual Scenarios
```bash
# Run specific scenario (1-6)
python run_e2e_tests.py --scenario 1
```

### Test Scenarios Overview

| Scenario | Description | Duration | Components Tested |
|----------|-------------|----------|-------------------|
| 1 | RAG Pipeline | ~60s | WebCrawler, Knowledge, RAG |
| 2 | Browser & Memory | ~45s | Browser, Memory, Data |
| 3 | Multi-Step Browser | ~60s | Browser, Planning, Execution |
| 4 | TTS Streaming | ~30s | TTS, Audio, Streaming |
| 5 | Code Execution | ~30s | Code, Output, Streaming |
| 6 | Settings & Chat | ~20s | Chat, Settings, UI |

---

## 📋 Manual Testing

### Using the Manual Checklist
1. Open `MANUAL_E2E_TESTING_CHECKLIST.md`
2. Follow each scenario step-by-step
3. Check off completed items
4. Document any issues found

### Key Manual Test Areas
- **UI/UX Testing**: Responsive design, visual consistency
- **Error Handling**: Network issues, backend failures
- **Performance**: Response times, resource usage
- **Accessibility**: Keyboard navigation, screen readers

---

## 🔍 Test Results Analysis

### Automated Test Reports
- Reports saved as `e2e_test_report_YYYYMMDD_HHMMSS.md`
- Include pass/fail status, performance metrics, error details
- JSON results available for programmatic analysis

### Health Check Reports
- System status verification
- Component availability checks
- Configuration validation
- Saved as `health_check_results_YYYYMMDD_HHMMSS.json`

---

## 🛠️ Troubleshooting

### Common Issues

#### Backend Not Starting
```bash
# Check Python dependencies
pip install -r requirements.txt

# Check environment variables
cat .env

# Check port availability
lsof -i :8000
```

#### Frontend Not Loading
```bash
# Install dependencies
cd frontend
npm install

# Clear cache
npm run build
rm -rf node_modules/.cache

# Check port availability
lsof -i :5173
```

#### WebSocket Connection Failed
- Verify backend is running on port 8000
- Check firewall settings
- Ensure no proxy blocking WebSocket connections

#### Tool Calls Not Working
- Verify API keys in .env file
- Check backend logs for errors
- Ensure Supabase database is accessible

### Debug Mode
```bash
# Run backend with debug logging
DEBUG=1 python run_ui.py

# Run frontend with debug
cd frontend
npm run dev -- --debug
```

---

## 📊 Performance Benchmarks

### Expected Response Times
- **Simple Chat**: <5 seconds
- **Web Crawling**: <30 seconds  
- **Browser Automation**: <45 seconds
- **Code Execution**: <10 seconds
- **TTS Generation**: <15 seconds

### Resource Usage Limits
- **Memory**: <2GB for full system
- **CPU**: <50% during normal operation
- **Network**: Varies by operation (crawling uses more)

---

## 🎯 Test Coverage

### Backend Components
- [x] WebCrawlerTool with streaming
- [x] BrowserAgentTool with action steps
- [x] MemoryAgentTool with storage/retrieval
- [x] HybridMemoryTool with LLM synthesis
- [x] ChatterboxTTSTool with audio streaming
- [x] GeneralCodeExecutionTool with live output
- [x] StreamProtocol events
- [x] WebSocket communication

### Frontend Components
- [x] ToolCallCard with specialized displays
- [x] AudioPlaybackControl for TTS
- [x] Real-time output streaming
- [x] Event handling and state management
- [x] Responsive UI design
- [x] Error handling and recovery

### Integration Points
- [x] WebSocket event flow
- [x] Tool call lifecycle
- [x] Streaming data handling
- [x] Error propagation
- [x] State synchronization

---

## 🚦 Test Status Dashboard

### Current Implementation Status

| Component | Implementation | Testing | Status |
|-----------|---------------|---------|--------|
| WebCrawlerTool | ✅ Complete | ✅ Tested | 🟢 Ready |
| BrowserAgentTool | ✅ Complete | ✅ Tested | 🟢 Ready |
| MemoryAgentTool | ✅ Complete | ✅ Tested | 🟢 Ready |
| HybridMemoryTool | ✅ Complete | ✅ Tested | 🟢 Ready |
| ChatterboxTTSTool | ✅ Complete | ✅ Tested | 🟢 Ready |
| CodeExecutionTool | ✅ Complete | ✅ Tested | 🟢 Ready |
| ToolCallCard UI | ✅ Complete | ✅ Tested | 🟢 Ready |
| Audio Controls | ✅ Complete | ✅ Tested | 🟢 Ready |
| Streaming Output | ✅ Complete | ✅ Tested | 🟢 Ready |
| E2E Framework | ✅ Complete | 🧪 Testing | 🟡 In Progress |

---

## 📈 Success Criteria

### Automated Tests
- **Pass Rate**: >90% for production readiness
- **Performance**: All operations within benchmark times
- **Error Handling**: Graceful failure and recovery
- **Streaming**: Real-time data flow working

### Manual Tests
- **UI/UX**: Consistent, responsive, accessible
- **Functionality**: All features working as designed
- **Integration**: Seamless component interaction
- **Stability**: No crashes or memory leaks

---

## 🎉 Production Readiness Checklist

### System Validation
- [ ] All automated tests passing
- [ ] Manual testing completed
- [ ] Performance benchmarks met
- [ ] Error handling verified
- [ ] Security review completed

### Documentation
- [ ] User guide updated
- [ ] API documentation current
- [ ] Deployment guide ready
- [ ] Troubleshooting guide complete

### Deployment Preparation
- [ ] Environment configurations tested
- [ ] Database migrations ready
- [ ] Monitoring and logging configured
- [ ] Backup and recovery procedures tested

---

## 📞 Support and Resources

### Getting Help
1. **Check Logs**: Backend and frontend console logs
2. **Review Documentation**: This guide and component docs
3. **Run Health Check**: `python system_health_check.py`
4. **Test Connectivity**: `python run_e2e_tests.py --quick`

### Additional Resources
- **Component Documentation**: See individual tool files
- **API Reference**: Check FastAPI docs at `/docs`
- **Frontend Guide**: See `frontend/README.md`
- **Deployment Guide**: See `DEPLOYMENT.md`

---

## 🔄 Continuous Testing

### Automated Testing Pipeline
```bash
# Daily health checks
0 9 * * * /path/to/system_health_check.py

# Weekly full E2E tests  
0 2 * * 0 /path/to/run_e2e_tests.py
```

### Monitoring and Alerts
- Set up monitoring for key metrics
- Configure alerts for test failures
- Regular performance baseline updates
- Automated report generation

---

**Phoenix Agent System E2E Testing - Ensuring Quality and Reliability** 🚀
