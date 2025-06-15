# python/agents/browser_agent/browser.py
import asyncio
from typing import Dict, Optional, Union
import logging

# Try to import Playwright - fallback to mock if not available
try:
    from playwright.async_api import (
        async_playwright, Browser as PWBrowser, BrowserContext as PWBrowserContext,
        Page as PWPage, Playwright, Error as PlaywrightError, TimeoutError as PlaywrightTimeoutError
    )
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False
    PWBrowser = None
    PWBrowserContext = None
    PWPage = None
    Playwright = None
    PlaywrightError = Exception
    PlaywrightTimeoutError = Exception

logger = logging.getLogger(__name__)  # Use a dedicated logger

class BrowserManager:
    """
    Manages Playwright browser instances and contexts with robust error handling.
    Falls back to mock implementation if Playwright is not available.
    """
    _playwright_instance: Optional[Playwright] = None
    _browser_instance: Optional[PWBrowser] = None
    _contexts: Dict[str, PWBrowserContext] = {} # session_id -> BrowserContext
    _context_locks: Dict[str, asyncio.Lock] = {} # Lock per session_id for context/page operations
    _global_lock = asyncio.Lock() # Lock for playwright/browser instance creation/deletion

    def __init__(self, headless: bool = True, browser_type: str = "chromium",
                 playwright_timeout: int = 30000):
        self.headless = headless
        self.browser_type = browser_type # e.g., "chromium", "firefox", "webkit"
        self.playwright_timeout = playwright_timeout # ms
        self.is_mock = not PLAYWRIGHT_AVAILABLE

        if self.is_mock:
            logger.info(f"BrowserManager initialized (MOCK - Playwright not available): headless={headless}, browser={browser_type}")
            self._mock_contexts = {}
        else:
            logger.info(f"BrowserManager instance configured: headless={headless}, browser={browser_type}, timeout={playwright_timeout}ms")

    async def _ensure_playwright_and_browser(self):
        """Ensures Playwright is started and a browser instance is launched."""
        if self.is_mock:
            return

        async with BrowserManager._global_lock:
            if BrowserManager._playwright_instance is None:
                logger.info("BrowserManager: Starting Playwright...")
                try:
                    BrowserManager._playwright_instance = await async_playwright().start()
                    logger.info("BrowserManager: Playwright started successfully.")
                except Exception as e:
                    logger.error(f"BrowserManager: Failed to start Playwright: {e}")
                    raise RuntimeError("Failed to start Playwright") from e

            if BrowserManager._browser_instance is None or not BrowserManager._browser_instance.is_connected():
                logger.info(f"BrowserManager: Launching {self.browser_type} browser (headless: {self.headless})...")
                try:
                    pw_instance = BrowserManager._playwright_instance
                    if self.browser_type == "chromium":
                        BrowserManager._browser_instance = await pw_instance.chromium.launch(headless=self.headless)
                    elif self.browser_type == "firefox":
                        BrowserManager._browser_instance = await pw_instance.firefox.launch(headless=self.headless)
                    elif self.browser_type == "webkit":
                        BrowserManager._browser_instance = await pw_instance.webkit.launch(headless=self.headless)
                    else:
                        raise ValueError(f"Unsupported browser type: {self.browser_type}")
                    logger.info(f"BrowserManager: {self.browser_type} browser launched successfully.")
                except Exception as e:
                    logger.error(f"BrowserManager: Failed to launch {self.browser_type} browser: {e}")
                    # Attempt to clean up playwright if browser launch fails
                    if BrowserManager._playwright_instance:
                        await BrowserManager._playwright_instance.stop()
                        BrowserManager._playwright_instance = None
                    raise RuntimeError(f"Failed to launch browser {self.browser_type}") from e
    
    async def get_context(self, session_id: str = "default_context") -> PWBrowserContext:
        """Gets or creates a new browser context for a given session_id."""
        if self.is_mock:
            return await self._get_mock_context(session_id)

        await self._ensure_playwright_and_browser()

        # Ensure a lock exists for this session_id
        if session_id not in BrowserManager._context_locks:
            async with BrowserManager._global_lock: # Protect creation of new session locks
                if session_id not in BrowserManager._context_locks: # Double check
                     BrowserManager._context_locks[session_id] = asyncio.Lock()

        async with BrowserManager._context_locks[session_id]:
            context = BrowserManager._contexts.get(session_id)
            # Check if context is still valid (e.g., browser is connected and context not manually closed)
            is_context_valid = False
            if context:
                try:
                    # A simple check, more robust checks might involve trying a simple operation
                    if BrowserManager._browser_instance and BrowserManager._browser_instance.is_connected() and len(context.pages) >= 0: # len(pages) can be 0
                       is_context_valid = True
                except PlaywrightError: # Catches errors if context is already closed
                    logger.warning(f"BrowserManager: Context for session {session_id} seems invalid or closed.")
                    is_context_valid = False

            if not is_context_valid:
                logger.info(f"BrowserManager: Creating new browser context for session_id: {session_id}")
                if context: # If old context object exists but invalid, try to close it first
                    try: await context.close()
                    except Exception: pass
                try:
                    BrowserManager._contexts[session_id] = await BrowserManager._browser_instance.new_context(
                        # viewport={'width': 1280, 'height': 720}, # Example
                        # user_agent="Mozilla/5.0 ..."
                    )
                    logger.info(f"BrowserManager: New context created for session_id: {session_id}")
                except Exception as e:
                    logger.error(f"BrowserManager: Failed to create new context for {session_id}: {e}")
                    raise
            return BrowserManager._contexts[session_id]

    async def get_page(self, session_id: str = "default_context", page_index: int = 0, create_if_needed: bool = True) -> Optional[PWPage]:
        """
        Gets a specific page from a browser context, or creates one if none exist.
        If page_index is specified, returns that page. Otherwise, returns the first page or a new one.
        """
        if self.is_mock:
            return await self._get_mock_page(session_id, page_index)

        try:
            context = await self.get_context(session_id) # Ensures context exists
            async with BrowserManager._context_locks[session_id]:
                if page_index < 0: page_index = 0 # Default to first page for negative index

                if 0 <= page_index < len(context.pages) and not context.pages[page_index].is_closed():
                    return context.pages[page_index]
                elif create_if_needed:
                    logger.info(f"BrowserManager: Page at index {page_index} not found or closed for session {session_id}. Creating new page.")
                    new_page = await context.new_page()
                    # If we want to enforce a specific number of pages or manage page_index strictly,
                    # this logic would need to be more complex. For now, new_page adds to context.pages.
                    # The caller asking for page_index might get a *new* page that is now at a different index
                    # if other pages were closed. Simplest is to return the new page.
                    return new_page
                else:
                    logger.warning(f"BrowserManager: Page at index {page_index} not found for session {session_id} and create_if_needed is False.")
                    return None
        except Exception as e:
            logger.error(f"BrowserManager: Error getting page for session {session_id}, index {page_index}: {e}")
            return None

    async def new_page_in_context(self, session_id: str = "default_context") -> PWPage:
        """Creates and returns a new page within a specific browser context."""
        if self.is_mock:
            return await self._new_mock_page(session_id)

        context = await self.get_context(session_id)
        async with BrowserManager._context_locks[session_id]:
            page = await context.new_page()
            logger.info(f"BrowserManager: New page created in context {session_id}. URL: {page.url}. Total pages: {len(context.pages)}")
            return page

    async def close_page_in_context(self, session_id: str, page_index_or_page: Union[int, PWPage]):
        """Closes a specific page in a browser context."""
        if self.is_mock:
            # Handle mock page closing
            context = await self._get_mock_context(session_id)
            if isinstance(page_index_or_page, int):
                if 0 <= page_index_or_page < len(context.pages):
                    await context.pages[page_index_or_page].close()
                    context.pages.pop(page_index_or_page)
            return

        context = BrowserManager._contexts.get(session_id)
        if not context:
            logger.warning(f"BrowserManager: Context for session {session_id} not found for closing page.")
            return

        async with BrowserManager._context_locks[session_id]:
            page_to_close: Optional[PWPage] = None
            if isinstance(page_index_or_page, int):
                if 0 <= page_index_or_page < len(context.pages):
                    page_to_close = context.pages[page_index_or_page]
                else:
                    logger.warning(f"BrowserManager: Invalid page index {page_index_or_page} for closing in session {session_id}.")
                    return
            elif isinstance(page_index_or_page, PWPage):
                if page_index_or_page in context.pages:
                    page_to_close = page_index_or_page
                else:
                    logger.warning(f"BrowserManager: Provided page object not found in context {session_id} for closing.")
                    return

            if page_to_close and not page_to_close.is_closed():
                try:
                    await page_to_close.close()
                    logger.info(f"BrowserManager: Page closed in session {session_id}.")
                    # Playwright automatically removes closed pages from context.pages list
                except PlaywrightError as e:
                    logger.error(f"BrowserManager: Error closing page in session {session_id}: {e}")

    async def close_context(self, session_id: str = "default_context"):
        """Closes a browser context and cleans up resources."""
        if self.is_mock:
            return await self._close_mock_context(session_id)

        # Use global lock when modifying _contexts or _context_locks dicts themselves
        async with BrowserManager._global_lock:
            # Then acquire specific session lock for operations on that context
            session_lock = BrowserManager._context_locks.get(session_id)
            if session_lock: # Check if lock exists before trying to acquire
                async with session_lock:
                    if session_id in BrowserManager._contexts:
                        logger.info(f"BrowserManager: Closing browser context for session_id: {session_id}")
                        try:
                            await BrowserManager._contexts[session_id].close()
                        except PlaywrightError as e:
                            logger.error(f"BrowserManager: Error during context.close() for {session_id}: {e}")
                        finally: # Ensure removal from dicts
                            del BrowserManager._contexts[session_id]
                            del BrowserManager._context_locks[session_id] # Remove the lock as well
                            logger.info(f"BrowserManager: Browser context for session_id {session_id} removed from tracking.")
            else:
                 logger.info(f"BrowserManager: No active context or lock found for session_id {session_id} to close.")

    async def close_all_contexts_and_browser(self):
        """Closes all browser contexts and the browser instance."""
        if self.is_mock:
            logger.info("BrowserManager: Closing all mock contexts")
            self._mock_contexts.clear()
            return

        async with BrowserManager._global_lock:
            logger.info("BrowserManager: Closing all browser contexts...")
            for session_id in list(BrowserManager._contexts.keys()): # Iterate over a copy of keys
                # No need to call self.close_context which re-acquires global lock
                session_lock = BrowserManager._context_locks.get(session_id)
                if session_lock:
                    async with session_lock:
                        if session_id in BrowserManager._contexts:
                            try:
                                await BrowserManager._contexts[session_id].close()
                            except PlaywrightError as e:
                                logger.error(f"BrowserManager: Error closing context {session_id} during shutdown: {e}")
                            del BrowserManager._contexts[session_id]
                    if session_id in BrowserManager._context_locks: # Check again, might have been deleted
                        del BrowserManager._context_locks[session_id]

            BrowserManager._contexts.clear()
            BrowserManager._context_locks.clear()
            logger.info("BrowserManager: All contexts closed and cleared.")

            if BrowserManager._browser_instance and BrowserManager._browser_instance.is_connected():
                logger.info("BrowserManager: Closing browser instance...")
                try:
                    await BrowserManager._browser_instance.close()
                except PlaywrightError as e:
                    logger.error(f"BrowserManager: Error closing browser instance: {e}")
                BrowserManager._browser_instance = None
                logger.info("BrowserManager: Browser instance closed.")

            if BrowserManager._playwright_instance:
                logger.info("BrowserManager: Stopping Playwright...")
                try:
                    await BrowserManager._playwright_instance.stop()
                except Exception as e: # Playwright's stop can sometimes raise generic exceptions if already stopped
                    logger.error(f"BrowserManager: Error stopping Playwright: {e}")
                BrowserManager._playwright_instance = None
                logger.info("BrowserManager: Playwright stopped.")

    # Mock implementation methods
    async def _get_mock_context(self, session_id: str):
        """Mock context implementation"""
        if session_id not in self._mock_contexts:
            print(f"BrowserManager (Mock): Creating mock context for session_id: {session_id}")
            self._mock_contexts[session_id] = MockBrowserContext(session_id)
        return self._mock_contexts[session_id]

    async def _get_mock_page(self, session_id: str, page_index: int):
        """Mock page implementation"""
        context = await self._get_mock_context(session_id)
        if not context.pages or page_index >= len(context.pages):
            print(f"BrowserManager (Mock): No page at index {page_index} for session {session_id}, creating new page.")
            return await context.new_page()
        return context.pages[page_index]

    async def _new_mock_page(self, session_id: str):
        """Mock new page implementation"""
        context = await self._get_mock_context(session_id)
        page = await context.new_page()
        print(f"BrowserManager (Mock): New page created in context {session_id}. URL: {page.url}")
        return page

    async def _close_mock_context(self, session_id: str):
        """Mock close context implementation"""
        if session_id in self._mock_contexts:
            print(f"BrowserManager (Mock): Closing mock context for session_id: {session_id}")
            await self._mock_contexts[session_id].close()
            del self._mock_contexts[session_id]


# Mock classes for when Playwright is not available
class MockPage:
    """A mock for a Playwright Page object."""
    def __init__(self, context_id: str, page_id: int, url="about:blank"):
        self.context_id = context_id
        self.page_id = page_id
        self.current_url = url
        self.current_title = "Mock Page"
        self.closed = False
        print(f"MockPage initialized for context {context_id}, page {page_id}, URL: {self.current_url}")

    async def goto(self, url: str, timeout: int = 60000):
        """Mock page navigation"""
        if self.closed:
            raise Exception("Page is closed")
        self.current_url = url
        self.current_title = f"Mock Page for {url.split('//')[-1].split('/')[0]}"
        print(f"MockPage: Navigated to {url}")
        await asyncio.sleep(0.1)  # Simulate network latency
        return {"status": "success", "url": self.current_url}

    async def title(self) -> str:
        """Get page title"""
        if self.closed:
            raise Exception("Page is closed")
        return self.current_title
    
    @property
    def url(self) -> str:
        """Get current URL"""
        return self.current_url

    async def content(self) -> str:
        """Get page HTML content"""
        if self.closed:
            raise Exception("Page is closed")
        return f"""<!DOCTYPE html>
<html>
<head><title>{self.current_title}</title></head>
<body>
<h1>Mock Page Content</h1>
<p>This is mock HTML content for URL: {self.current_url}</p>
<p>In a real implementation, this would be the actual page HTML.</p>
</body>
</html>"""

    def is_closed(self) -> bool:
        """Check if the page is closed"""
        return self.closed

    async def close(self):
        """Close the page"""
        if not self.closed:
            print(f"MockPage: Closed page {self.current_url}")
            self.closed = True


class MockBrowserContext:
    """A mock for a Playwright BrowserContext object."""
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.pages = []
        self.closed = False
        print(f"MockBrowserContext {session_id} initialized.")

    async def new_page(self) -> MockPage:
        """Create a new page in this context"""
        if self.closed:
            raise Exception("Context is closed")
        page_id = len(self.pages)
        page = MockPage(self.session_id, page_id)
        self.pages.append(page)
        print(f"MockBrowserContext ({self.session_id}): New page {page_id} created.")
        return page

    async def close(self):
        """Close the context and all its pages"""
        if not self.closed:
            print(f"MockBrowserContext {self.session_id}: Closing all pages...")
            for page in self.pages:
                if not page.closed:
                    await page.close()
            self.pages.clear()
            self.closed = True
            print(f"MockBrowserContext {self.session_id} closed.")


# Legacy compatibility - keep old class names for backward compatibility
class PageMock(MockPage):
    def __init__(self, url="about:blank"):
        super().__init__("legacy", 0, url)

class BrowserMock:
    def __init__(self, session_id: str):
        self.session_id = session_id
        self.pages = []
        self._current_page: MockPage = None
        print(f"BrowserMock session {session_id} initialized.")

    async def new_page(self) -> MockPage:
        self._current_page = MockPage(self.session_id, len(self.pages)) 
        self.pages.append(self._current_page)
        print(f"BrowserMock ({self.session_id}): New page created/reset.")
        return self._current_page
    
    @property
    def page(self) -> MockPage:
        if not self._current_page:
            import asyncio
            loop = asyncio.get_event_loop()
            self._current_page = loop.run_until_complete(self.new_page())
        return self._current_page

    async def close(self):
        for page in self.pages:
            if not page.closed:
                await page.close()
        print(f"BrowserMock session {self.session_id} closed.")