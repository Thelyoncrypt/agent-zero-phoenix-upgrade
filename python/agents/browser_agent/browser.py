# python/agents/browser_agent/browser.py
import asyncio
from typing import Dict

class PageMock:
    """A mock for a Playwright Page object."""
    def __init__(self, url="about:blank"):
        self.current_url = url
        self.current_title = "Mock Page"
        print(f"PageMock initialized for URL: {self.current_url}")

    async def goto(self, url: str):
        self.current_url = url
        self.current_title = f"Mock Page for {url.split('//')[-1].split('/')[0]}"
        print(f"PageMock: Navigated to {url}")
        await asyncio.sleep(0.1)  # Simulate network latency
        return {"status": "success", "url": self.current_url}

    async def title(self) -> str:
        return self.current_title
    
    @property
    def url(self) -> str:
        return self.current_url

    async def close(self):
        print(f"PageMock: Closed page {self.current_url}")

class BrowserMock:
    """A mock for a Playwright Browser object."""
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.pages = []
        self._current_page: PageMock = PageMock()  # Default page
        print(f"BrowserMock session {session_id} initialized.")

    async def new_page(self) -> PageMock:
        # For simplicity, let's reuse/reset a single mock page per browser mock instance
        self._current_page = PageMock() 
        print(f"BrowserMock ({self.session_id}): New page created/reset.")
        return self._current_page
    
    @property
    def page(self) -> PageMock:  # Convenience to get the "current" page
        if not self._current_page:
            # This should not happen in normal async flow
            self._current_page = PageMock()
        return self._current_page

    async def close(self):
        print(f"BrowserMock session {self.session_id} closed.")

class BrowserManager:
    """
    Manages browser instances (mocked for now).
    In a real implementation, this would handle Playwright browser contexts.
    """
    def __init__(self):
        self.browsers: Dict[str, BrowserMock] = {}
        print("BrowserManager (Mock) initialized.")

    async def get_browser(self, session_id: str = "default") -> BrowserMock:
        if session_id not in self.browsers:
            print(f"BrowserManager: Creating new mock browser session for {session_id}")
            self.browsers[session_id] = BrowserMock(session_id)
        return self.browsers[session_id]

    async def close_browser(self, session_id: str = "default"):
        if session_id in self.browsers:
            await self.browsers[session_id].close()
            del self.browsers[session_id]
            print(f"BrowserManager: Closed mock browser session for {session_id}")

    async def close_all_browsers(self):
        for session_id in list(self.browsers.keys()):
            await self.close_browser(session_id)
        print("BrowserManager: All mock browser sessions closed.")