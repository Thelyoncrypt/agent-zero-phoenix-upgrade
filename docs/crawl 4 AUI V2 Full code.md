└── crawl4AI-agent-v2
    ├── .env.example
    ├── README.md
    ├── crawl4AI-examples
        ├── 1-crawl_single_page.py
        ├── 2-crawl_docs_sequential.py
        ├── 3-crawl_sitemap_in_parallel.py
        ├── 4-crawl_llms_txt.py
        └── 5-crawl_site_recursively.py
    ├── insert_docs.py
    ├── rag_agent.py
    ├── requirements.txt
    ├── streamlit_app.py
    └── utils.py


/crawl4AI-agent-v2/.env.example:
--------------------------------------------------------------------------------
1 | # Get your Open AI API Key by following these instructions -
2 | # https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key
3 | # You only need this environment variable set if you are using GPT (and not Ollama)
4 | OPENAI_API_KEY=
5 | 
6 | # The LLM you want to use from OpenAI. See the list of models here:
7 | # https://platform.openai.com/docs/models
8 | # Example: gpt-4.1-mini
9 | MODEL_CHOICE=


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/README.md:
--------------------------------------------------------------------------------
  1 | # Pydantic AI Documentation Crawler & RAG Agent
  2 | 
  3 | An intelligent documentation crawler and retrieval-augmented generation (RAG) system, powered by Crawl4AI and Pydantic AI. This project enables you to crawl, chunk, and vectorize documentation from any website, `.txt`/Markdown pages (llms.txt), or sitemap, and interact with the knowledge base using a Streamlit interface.
  4 | 
  5 | ---
  6 | 
  7 | ## Features
  8 | 
  9 | - **Flexible documentation crawling:** Handles regular websites, `.txt`/Markdown pages (llms.txt), and sitemaps.
 10 | - **Parallel and recursive crawling:** Efficiently gathers large doc sites with memory-adaptive batching.
 11 | - **Smart chunking:** Hierarchical Markdown chunking by headers, ensuring chunks are optimal for vector search.
 12 | - **Vector database integration:** Stores chunks and metadata in ChromaDB for fast semantic retrieval.
 13 | - **Streamlit RAG interface:** Query your documentation with LLM-powered semantic search.
 14 | - **Extensible examples:** Modular scripts for various crawling and RAG workflows.
 15 | 
 16 | ---
 17 | 
 18 | ## Prerequisites
 19 | 
 20 | - Python 3.11+
 21 | - OpenAI API key (for embeddings and LLM-powered search)
 22 | - Crawl4AI/Playwright and other dependencies in `requirements.txt`
 23 | - (Optional) Streamlit for the web interface
 24 | 
 25 | ---
 26 | 
 27 | ## Installation
 28 | 
 29 | 1. **Clone the repository:**
 30 |    ```bash
31 |    git clone https://github.com/coleam00/ottomator-agents.git
 32 |    cd ottomator-agents/crawl4AI-agent-v2
 33 |
```
 34 | 
 35 | 2. **Install dependencies:**
 36 |    ```bash
37 |    python -m venv venv
 38 |    source venv/bin/activate  # On Windows: venv\Scripts\activate
 39 |    pip install -r requirements.txt
 40 |    playwright install
 41 |
```
 42 | 
 43 | 3. **Set up environment variables:**
 44 |    - Copy `.env.example` to `.env`
 45 |    - Edit `.env` with your API keys and preferences:
 46 |      ```env
47 |      OPENAI_API_KEY=your_openai_api_key
 48 |      MODEL_CHOICE=gpt-4.1-mini  # or your preferred OpenAI model
 49 |
```
 50 | 
 51 | ---
 52 | 
 53 | ## Usage
 54 | 
 55 | ### 1. Crawling and Inserting Documentation
 56 | 
 57 | The main entry point for crawling and vectorizing documentation is [`insert_docs.py`](insert_docs.py):
 58 | 
 59 | #### Supported URL Types
 60 | 
 61 | - **Regular documentation sites:** Recursively crawls all internal links, deduplicates by URL (ignoring fragments).
 62 | - **Markdown or .txt pages (such as llms.txt):** Fetches and chunks Markdown content.
 63 | - **Sitemaps (`sitemap.xml`):** Batch-crawls all URLs listed in the sitemap.
 64 | 
 65 | #### Example Usage
 66 | 
 67 | ```bash
68 | python insert_docs.py <URL> [--collection mydocs] [--db-dir ./chroma_db] [--embedding-model all-MiniLM-L6-v2] [--chunk-size 1000] [--max-depth 3] [--max-concurrent 10] [--batch-size 100]
 69 |
```
 70 | 
 71 | **Arguments:**
 72 | - `URL`: The root URL, .txt file, or sitemap to crawl.
 73 | - `--collection`: ChromaDB collection name (default: `docs`)
 74 | - `--db-dir`: Directory for ChromaDB data (default: `./chroma_db`)
 75 | - `--embedding-model`: Embedding model for vector storage (default: `all-MiniLM-L6-v2`)
 76 | - `--chunk-size`: Maximum characters per chunk (default: `1000`)
 77 | - `--max-depth`: Recursion depth for regular URLs (default: `3`)
 78 | - `--max-concurrent`: Max parallel browser sessions (default: `10`)
 79 | - `--batch-size`: Batch size for ChromaDB insertion (default: `100`)
 80 | 
 81 | **Examples for each type (regular URL, .txt, sitemap):**
 82 | ```bash
83 | python insert_docs.py https://ai.pydantic.dev/
 84 | python insert_docs.py https://ai.pydantic.dev/llms-full.txt
 85 | python insert_docs.py https://ai.pydantic.dev/sitemap.xml
 86 |
```
 87 | 
 88 | #### Chunking Strategy
 89 | 
 90 | - Splits content first by `#`, then by `##`, then by `###` headers.
 91 | - If a chunk is still too large, splits by character count.
 92 | - All chunks are less than the specified `--chunk-size` (default: 1000 characters).
 93 | 
 94 | #### Metadata
 95 | 
 96 | Each chunk is stored with:
 97 | - Source URL
 98 | - Chunk index
 99 | - Extracted headers
100 | - Character and word counts
101 | 
102 | ---
103 | 
104 | ### 2. Example Scripts
105 | 
106 | The `crawl4AI-examples/` folder contains modular scripts illustrating different crawling and chunking strategies:
107 | 
108 | - **`3-crawl_sitemap_in_parallel.py`:** Batch-crawls a list of URLs from a sitemap in parallel with memory tracking.
109 | - **`4-crawl_llms_txt.py`:** Crawls a Markdown or `.txt` file, splits by headers, and prints chunks.
110 | - **`5-crawl_site_recursively.py`:** Recursively crawls all internal links from a root URL, deduplicating by URL (ignoring fragments).
111 | 
112 | You can use these scripts directly for experimentation or as templates for custom crawlers.
113 | 
114 | ---
115 | 
116 | ### 3. Running the Streamlit RAG Interface
117 | 
118 | After crawling and inserting docs, launch the Streamlit app for semantic search and question answering:
119 | 
120 | ```bash
121 | streamlit run streamlit_app.py
122 |
```
123 | 
124 | - The interface will be available at [http://localhost:8501](http://localhost:8501)
125 | - Query your documentation using natural language and get context-rich answers.
126 | 
127 | ---
128 | 
129 | ## Project Structure
130 | 
131 | ```
132 | crawl4AI-agent-v2/
133 | ├── crawl4AI-examples/
134 | │   ├── 3-crawl_docs_FAST.py
135 | │   ├── 4-crawl_and_chunk_markdown.py
136 | │   └── 5-crawl_recursive_internal_links.py
137 | ├── insert_docs.py
138 | ├── rag_agent.py
139 | ├── streamlit_app.py
140 | ├── utils.py
141 | ├── requirements.txt
142 | ├── .env.example
143 | └── README.md
144 |
```
145 | 
146 | ---
147 | 
148 | ## Advanced Usage & Customization
149 | 
150 | - **Chunking:** Tune `--chunk-size` for your retrieval use case.
151 | - **Embeddings:** Swap out the embedding model with `--embedding-model`.
152 | - **Crawling:** Adjust `--max-depth` and `--max-concurrent` for large sites.
153 | - **Vector DB:** Use your own ChromaDB directory or collection for multiple projects.
154 | 
155 | ---
156 | 
157 | ## Troubleshooting
158 | 
159 | - Ensure all dependencies are installed and environment variables are set.
160 | - For large sites, increase memory or decrease `--max-concurrent`.
161 | - If you encounter crawling issues, try running the example scripts for isolated debugging.


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/crawl4AI-examples/1-crawl_single_page.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | from crawl4ai import AsyncWebCrawler, BrowserConfig
 3 | 
 4 | async def main():
 5 |     async with AsyncWebCrawler() as crawler:
 6 |         result = await crawler.arun(
 7 |             url="https://ai.pydantic.dev/",
 8 |         )
 9 |         print(result.markdown)
10 | 
11 | if __name__ == "__main__":
12 |     asyncio.run(main())


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/crawl4AI-examples/2-crawl_docs_sequential.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | from typing import List
 3 | from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
 4 | from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
 5 | import requests
 6 | from xml.etree import ElementTree
 7 | 
 8 | async def crawl_sequential(urls: List[str]):
 9 |     print("\n=== Sequential Crawling with Session Reuse ===")
10 | 
11 |     browser_config = BrowserConfig(
12 |         headless=True,
13 |         # For better performance in Docker or low-memory environments:
14 |         extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
15 |     )
16 | 
17 |     crawl_config = CrawlerRunConfig(
18 |         markdown_generator=DefaultMarkdownGenerator()
19 |     )
20 | 
21 |     # Create the crawler (opens the browser)
22 |     crawler = AsyncWebCrawler(config=browser_config)
23 |     await crawler.start()
24 | 
25 |     try:
26 |         session_id = "session1"  # Reuse the same session across all URLs
27 |         for url in urls:
28 |             result = await crawler.arun(
29 |                 url=url,
30 |                 config=crawl_config,
31 |                 session_id=session_id
32 |             )
33 |             if result.success:
34 |                 print(f"Successfully crawled: {url}")
35 |                 # E.g. check markdown length
36 |                 print(f"Markdown length: {len(result.markdown.raw_markdown)}")
37 |             else:
38 |                 print(f"Failed: {url} - Error: {result.error_message}")
39 |     finally:
40 |         # After all URLs are done, close the crawler (and the browser)
41 |         await crawler.close()
42 | 
43 | def get_pydantic_ai_docs_urls():
44 |     """
45 |     Fetches all URLs from the Pydantic AI documentation.
46 |     Uses the sitemap (https://ai.pydantic.dev/sitemap.xml) to get these URLs.
47 |     
48 |     Returns:
49 |         List[str]: List of URLs
50 |     """            
51 |     sitemap_url = "https://ai.pydantic.dev/sitemap.xml"
52 |     try:
53 |         response = requests.get(sitemap_url)
54 |         response.raise_for_status()
55 |         
56 |         # Parse the XML
57 |         root = ElementTree.fromstring(response.content)
58 |         
59 |         # Extract all URLs from the sitemap
60 |         # The namespace is usually defined in the root element
61 |         namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
62 |         urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
63 |         
64 |         return urls
65 |     except Exception as e:
66 |         print(f"Error fetching sitemap: {e}")
67 |         return []
68 | 
69 | async def main():
70 |     urls = get_pydantic_ai_docs_urls()
71 |     if urls:
72 |         print(f"Found {len(urls)} URLs to crawl")
73 |         await crawl_sequential(urls)
74 |     else:
75 |         print("No URLs found to crawl")
76 | 
77 | if __name__ == "__main__":
78 |     asyncio.run(main())
79 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/crawl4AI-examples/3-crawl_sitemap_in_parallel.py:
--------------------------------------------------------------------------------
  1 | """
  2 | 3-crawl_docs_FAST.py
  3 | --------------------
  4 | Batch-crawls a list of documentation URLs in parallel using Crawl4AI's arun_many and a memory-adaptive dispatcher.
  5 | Tracks memory usage, prints a summary of successes/failures, and is suitable for large-scale doc scraping jobs.
  6 | Usage: Call main() or run as a script. Adjust max_concurrent for parallelism.
  7 | """
  8 | import os
  9 | import sys
 10 | import psutil
 11 | import asyncio
 12 | import requests
 13 | from typing import List
 14 | from xml.etree import ElementTree
 15 | from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, MemoryAdaptiveDispatcher
 16 | 
 17 | async def crawl_parallel(urls: List[str], max_concurrent: int = 10):
 18 |     print("\n=== Parallel Crawling with arun_many + Dispatcher ===")
 19 | 
 20 |     # Track the peak memory usage for observability
 21 |     peak_memory = 0
 22 |     process = psutil.Process(os.getpid())
 23 |     def log_memory(prefix: str = ""):
 24 |         nonlocal peak_memory
 25 |         current_mem = process.memory_info().rss  # in bytes
 26 |         if current_mem > peak_memory:
 27 |             peak_memory = current_mem
 28 |         print(f"{prefix} Current Memory: {current_mem // (1024 * 1024)} MB, Peak: {peak_memory // (1024 * 1024)} MB")
 29 | 
 30 |     # Configure the browser for headless operation and resource limits
 31 |     browser_config = BrowserConfig(
 32 |         headless=True,
 33 |         verbose=False,
 34 |         extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
 35 |     )
 36 |     # Set up crawl config and dispatcher for batch crawling
 37 |     crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, stream=False)
 38 |     dispatcher = MemoryAdaptiveDispatcher(
 39 |         memory_threshold_percent=70.0,  # Don't exceed 70% memory usage
 40 |         check_interval=1.0,             # Check memory every second
 41 |         max_session_permit=max_concurrent  # Max parallel browser sessions
 42 |     )
 43 | 
 44 |     async with AsyncWebCrawler(config=browser_config) as crawler:
 45 |         log_memory("Before crawl: ")
 46 |         # arun_many handles all URLs in parallel, batching and resource management handled by dispatcher
 47 |         results = await crawler.arun_many(
 48 |             urls=urls,
 49 |             config=crawl_config,
 50 |             dispatcher=dispatcher
 51 |         )
 52 |         success_count = 0
 53 |         fail_count = 0
 54 |         # Loop through all crawl results and tally success/failure
 55 |         for result in results:
 56 |             if result.success:
 57 |                 success_count += 1
 58 |             else:
 59 |                 print(f"Error crawling {result.url}: {result.error_message}")
 60 |                 fail_count += 1
 61 | 
 62 |         print(f"\nSummary:")
 63 |         print(f"  - Successfully crawled: {success_count}")
 64 |         print(f"  - Failed: {fail_count}")
 65 |         log_memory("After crawl: ")
 66 |         print(f"\nPeak memory usage (MB): {peak_memory // (1024 * 1024)}")
 67 | 
 68 | def get_pydantic_ai_docs_urls():
 69 |     """
 70 |     Fetches all URLs from the Pydantic AI documentation.
 71 |     Uses the sitemap (https://ai.pydantic.dev/sitemap.xml) to get these URLs.
 72 |     
 73 |     Returns:
 74 |         List[str]: List of URLs
 75 |     """            
 76 |     sitemap_url = "https://ai.pydantic.dev/sitemap.xml"
 77 |     try:
 78 |         response = requests.get(sitemap_url)
 79 |         response.raise_for_status()
 80 |         
 81 |         # Parse the XML
 82 |         root = ElementTree.fromstring(response.content)
 83 |         
 84 |         # Extract all URLs from the sitemap
 85 |         # The namespace is usually defined in the root element
 86 |         namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
 87 |         urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
 88 |         
 89 |         return urls
 90 |     except Exception as e:
 91 |         print(f"Error fetching sitemap: {e}")
 92 |         return []        
 93 | 
 94 | async def main():
 95 |     urls = get_pydantic_ai_docs_urls()
 96 |     if urls:
 97 |         print(f"Found {len(urls)} URLs to crawl")
 98 |         await crawl_parallel(urls, max_concurrent=10)
 99 |     else:
100 |         print("No URLs found to crawl")    
101 | 
102 | if __name__ == "__main__":
103 |     asyncio.run(main())
104 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/crawl4AI-examples/4-crawl_llms_txt.py:
--------------------------------------------------------------------------------
 1 | """
 2 | 4-crawl_and_chunk_markdown.py
 3 | -----------------------------
 4 | Scrapes a Markdown (.md or .txt) page using Crawl4AI, then splits the content into chunks based on # and ## headers.
 5 | Prints each chunk for further processing or inspection.
 6 | Usage: Set the target URL in main(), then run as a script.
 7 | """
 8 | import asyncio
 9 | from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
10 | import re
11 | 
12 | async def scrape_and_chunk_markdown(url: str):
13 |     """
14 |     Scrape a Markdown page and split into chunks by # and ## headers.
15 |     """
16 |     browser_config = BrowserConfig(headless=True)
17 |     crawl_config = CrawlerRunConfig()
18 |     async with AsyncWebCrawler(config=browser_config) as crawler:
19 |         result = await crawler.arun(url=url, config=crawl_config)
20 |         if not result.success:
21 |             print(f"Failed to crawl {url}: {result.error_message}")
22 |             return
23 |         markdown = result.markdown
24 |         # Split by headers (#, ##)
25 |         # Find all # and ## headers to use as chunk boundaries
26 |         header_pattern = re.compile(r'^(# .+|## .+)
#39;, re.MULTILINE)
27 |         headers = [m.start() for m in header_pattern.finditer(markdown)] + [len(markdown)]
28 |         chunks = []
29 |         # Split the markdown into chunks between headers
30 |         for i in range(len(headers)-1):
31 |             chunk = markdown[headers[i]:headers[i+1]].strip()
32 |             if chunk:
33 |                 chunks.append(chunk)
34 |         print(f"Split into {len(chunks)} chunks:")
35 |         for idx, chunk in enumerate(chunks):
36 |             print(f"\n--- Chunk {idx+1} ---\n{chunk}\n")
37 | 
38 | if __name__ == "__main__":
39 |     url = "https://ai.pydantic.dev/llms-full.txt"
40 |     asyncio.run(scrape_and_chunk_markdown(url))
41 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/crawl4AI-examples/5-crawl_site_recursively.py:
--------------------------------------------------------------------------------
 1 | """
 2 | 5-crawl_recursive_internal_links.py
 3 | ----------------------------------
 4 | Recursively crawls a site starting from a root URL, using Crawl4AI's arun_many and a memory-adaptive dispatcher.
 5 | At each depth, all internal links are discovered and crawled in parallel, up to a specified depth, with deduplication.
 6 | Usage: Set the start URL and max_depth in main(), then run as a script.
 7 | """
 8 | import asyncio
 9 | from urllib.parse import urldefrag
10 | from crawl4ai import (
11 |     AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode,
12 |     MemoryAdaptiveDispatcher
13 | )
14 | 
15 | async def crawl_recursive_batch(start_urls, max_depth=3, max_concurrent=10):
16 |     browser_config = BrowserConfig(headless=True, verbose=False)
17 |     run_config = CrawlerRunConfig(
18 |         cache_mode=CacheMode.BYPASS,
19 |         stream=False
20 |     )
21 |     dispatcher = MemoryAdaptiveDispatcher(
22 |         memory_threshold_percent=70.0,      # Don't exceed 70% memory usage
23 |         check_interval=1.0,                 # Check memory every second
24 |         max_session_permit=max_concurrent   # Max parallel browser sessions
25 |     )
26 | 
27 |     # Track visited URLs to prevent revisiting and infinite loops (ignoring fragments)
28 |     visited = set()
29 |     def normalize_url(url):
30 |         # Remove fragment (part after #)
31 |         return urldefrag(url)[0]
32 |     current_urls = set([normalize_url(u) for u in start_urls])
33 | 
34 |     async with AsyncWebCrawler(config=browser_config) as crawler:
35 |         for depth in range(max_depth):
36 |             print(f"\n=== Crawling Depth {depth+1} ===")
37 |             # Only crawl URLs we haven't seen yet (ignoring fragments)
38 |             urls_to_crawl = [normalize_url(url) for url in current_urls if normalize_url(url) not in visited]
39 | 
40 |             if not urls_to_crawl:
41 |                 break
42 | 
43 |             # Batch-crawl all URLs at this depth in parallel
44 |             results = await crawler.arun_many(
45 |                 urls=urls_to_crawl,
46 |                 config=run_config,
47 |                 dispatcher=dispatcher
48 |             )
49 | 
50 |             next_level_urls = set()
51 | 
52 |             for result in results:
53 |                 norm_url = normalize_url(result.url)
54 |                 visited.add(norm_url)  # Mark as visited (no fragment)
55 |                 if result.success:
56 |                     print(f"[OK] {result.url} | Markdown: {len(result.markdown) if result.markdown else 0} chars")
57 |                     # Collect all new internal links for the next depth
58 |                     for link in result.links.get("internal", []):
59 |                         next_url = normalize_url(link["href"])
60 |                         if next_url not in visited:
61 |                             next_level_urls.add(next_url)
62 |                 else:
63 |                     print(f"[ERROR] {result.url}: {result.error_message}")
64 |                     
65 |             # Move to the next set of URLs for the next recursion depth
66 |             current_urls = next_level_urls
67 | 
68 | if __name__ == "__main__":
69 |     asyncio.run(crawl_recursive_batch(["https://ai.pydantic.dev/"], max_depth=3, max_concurrent=10))
70 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/insert_docs.py:
--------------------------------------------------------------------------------
  1 | """
  2 | insert_docs.py
  3 | --------------
  4 | Command-line utility to crawl any URL using Crawl4AI, detect content type (sitemap, .txt, or regular page),
  5 | use the appropriate crawl method, chunk the resulting Markdown into <1000 character blocks by header hierarchy,
  6 | and insert all chunks into ChromaDB with metadata.
  7 | 
  8 | Usage:
  9 |     python insert_docs.py <URL> [--collection ...] [--db-dir ...] [--embedding-model ...]
 10 | """
 11 | import argparse
 12 | import sys
 13 | import re
 14 | import asyncio
 15 | from typing import List, Dict, Any
 16 | from urllib.parse import urlparse, urldefrag
 17 | from xml.etree import ElementTree
 18 | from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, MemoryAdaptiveDispatcher
 19 | import requests
 20 | from utils import get_chroma_client, get_or_create_collection, add_documents_to_collection
 21 | 
 22 | def smart_chunk_markdown(markdown: str, max_len: int = 1000) -> List[str]:
 23 |     """Hierarchically splits markdown by #, ##, ### headers, then by characters, to ensure all chunks < max_len."""
 24 |     def split_by_header(md, header_pattern):
 25 |         indices = [m.start() for m in re.finditer(header_pattern, md, re.MULTILINE)]
 26 |         indices.append(len(md))
 27 |         return [md[indices[i]:indices[i+1]].strip() for i in range(len(indices)-1) if md[indices[i]:indices[i+1]].strip()]
 28 | 
 29 |     chunks = []
 30 | 
 31 |     for h1 in split_by_header(markdown, r'^# .+
#39;):
 32 |         if len(h1) > max_len:
 33 |             for h2 in split_by_header(h1, r'^## .+
#39;):
 34 |                 if len(h2) > max_len:
 35 |                     for h3 in split_by_header(h2, r'^### .+
#39;):
 36 |                         if len(h3) > max_len:
 37 |                             for i in range(0, len(h3), max_len):
 38 |                                 chunks.append(h3[i:i+max_len].strip())
 39 |                         else:
 40 |                             chunks.append(h3)
 41 |                 else:
 42 |                     chunks.append(h2)
 43 |         else:
 44 |             chunks.append(h1)
 45 | 
 46 |     final_chunks = []
 47 | 
 48 |     for c in chunks:
 49 |         if len(c) > max_len:
 50 |             final_chunks.extend([c[i:i+max_len].strip() for i in range(0, len(c), max_len)])
 51 |         else:
 52 |             final_chunks.append(c)
 53 | 
 54 |     return [c for c in final_chunks if c]
 55 | 
 56 | def is_sitemap(url: str) -> bool:
 57 |     return url.endswith('sitemap.xml') or 'sitemap' in urlparse(url).path
 58 | 
 59 | def is_txt(url: str) -> bool:
 60 |     return url.endswith('.txt')
 61 | 
 62 | async def crawl_recursive_internal_links(start_urls, max_depth=3, max_concurrent=10) -> List[Dict[str,Any]]:
 63 |     """Recursive crawl using logic from 5-crawl_recursive_internal_links.py. Returns list of dicts with url and markdown."""
 64 |     browser_config = BrowserConfig(headless=True, verbose=False)
 65 |     run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, stream=False)
 66 |     dispatcher = MemoryAdaptiveDispatcher(
 67 |         memory_threshold_percent=70.0,
 68 |         check_interval=1.0,
 69 |         max_session_permit=max_concurrent
 70 |     )
 71 | 
 72 |     visited = set()
 73 | 
 74 |     def normalize_url(url):
 75 |         return urldefrag(url)[0]
 76 | 
 77 |     current_urls = set([normalize_url(u) for u in start_urls])
 78 |     results_all = []
 79 | 
 80 |     async with AsyncWebCrawler(config=browser_config) as crawler:
 81 |         for depth in range(max_depth):
 82 |             urls_to_crawl = [normalize_url(url) for url in current_urls if normalize_url(url) not in visited]
 83 |             if not urls_to_crawl:
 84 |                 break
 85 | 
 86 |             results = await crawler.arun_many(urls=urls_to_crawl, config=run_config, dispatcher=dispatcher)
 87 |             next_level_urls = set()
 88 | 
 89 |             for result in results:
 90 |                 norm_url = normalize_url(result.url)
 91 |                 visited.add(norm_url)
 92 | 
 93 |                 if result.success and result.markdown:
 94 |                     results_all.append({'url': result.url, 'markdown': result.markdown})
 95 |                     for link in result.links.get("internal", []):
 96 |                         next_url = normalize_url(link["href"])
 97 |                         if next_url not in visited:
 98 |                             next_level_urls.add(next_url)
 99 | 
100 |             current_urls = next_level_urls
101 | 
102 |     return results_all
103 | 
104 | async def crawl_markdown_file(url: str) -> List[Dict[str,Any]]:
105 |     """Crawl a .txt or markdown file using logic from 4-crawl_and_chunk_markdown.py."""
106 |     browser_config = BrowserConfig(headless=True)
107 |     crawl_config = CrawlerRunConfig()
108 | 
109 |     async with AsyncWebCrawler(config=browser_config) as crawler:
110 |         result = await crawler.arun(url=url, config=crawl_config)
111 |         if result.success and result.markdown:
112 |             return [{'url': url, 'markdown': result.markdown}]
113 |         else:
114 |             print(f"Failed to crawl {url}: {result.error_message}")
115 |             return []
116 | 
117 | def parse_sitemap(sitemap_url: str) -> List[str]:
118 |     resp = requests.get(sitemap_url)
119 |     urls = []
120 | 
121 |     if resp.status_code == 200:
122 |         try:
123 |             tree = ElementTree.fromstring(resp.content)
124 |             urls = [loc.text for loc in tree.findall('.//{*}loc')]
125 |         except Exception as e:
126 |             print(f"Error parsing sitemap XML: {e}")
127 | 
128 |     return urls
129 | 
130 | async def crawl_batch(urls: List[str], max_concurrent: int = 10) -> List[Dict[str,Any]]:
131 |     """Batch crawl using logic from 3-crawl_sitemap_in_parallel.py."""
132 |     browser_config = BrowserConfig(headless=True, verbose=False)
133 |     crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, stream=False)
134 |     dispatcher = MemoryAdaptiveDispatcher(
135 |         memory_threshold_percent=70.0,
136 |         check_interval=1.0,
137 |         max_session_permit=max_concurrent
138 |     )
139 | 
140 |     async with AsyncWebCrawler(config=browser_config) as crawler:
141 |         results = await crawler.arun_many(urls=urls, config=crawl_config, dispatcher=dispatcher)
142 |         return [{'url': r.url, 'markdown': r.markdown} for r in results if r.success and r.markdown]
143 | 
144 | def extract_section_info(chunk: str) -> Dict[str, Any]:
145 |     """Extracts headers and stats from a chunk."""
146 |     headers = re.findall(r'^(#+)\s+(.+)
#39;, chunk, re.MULTILINE)
147 |     header_str = '; '.join([f'{h[0]} {h[1]}' for h in headers]) if headers else ''
148 | 
149 |     return {
150 |         "headers": header_str,
151 |         "char_count": len(chunk),
152 |         "word_count": len(chunk.split())
153 |     }
154 | 
155 | def main():
156 |     parser = argparse.ArgumentParser(description="Insert crawled docs into ChromaDB")
157 |     parser.add_argument("url", help="URL to crawl (regular, .txt, or sitemap)")
158 |     parser.add_argument("--collection", default="docs", help="ChromaDB collection name")
159 |     parser.add_argument("--db-dir", default="./chroma_db", help="ChromaDB directory")
160 |     parser.add_argument("--embedding-model", default="all-MiniLM-L6-v2", help="Embedding model name")
161 |     parser.add_argument("--chunk-size", type=int, default=1000, help="Max chunk size (chars)")
162 |     parser.add_argument("--max-depth", type=int, default=3, help="Recursion depth for regular URLs")
163 |     parser.add_argument("--max-concurrent", type=int, default=10, help="Max parallel browser sessions")
164 |     parser.add_argument("--batch-size", type=int, default=100, help="ChromaDB insert batch size")
165 |     args = parser.parse_args()
166 | 
167 |     # Detect URL type
168 |     url = args.url
169 |     if is_txt(url):
170 |         print(f"Detected .txt/markdown file: {url}")
171 |         crawl_results = asyncio.run(crawl_markdown_file(url))
172 |     elif is_sitemap(url):
173 |         print(f"Detected sitemap: {url}")
174 |         sitemap_urls = parse_sitemap(url)
175 |         if not sitemap_urls:
176 |             print("No URLs found in sitemap.")
177 |             sys.exit(1)
178 |         crawl_results = asyncio.run(crawl_batch(sitemap_urls, max_concurrent=args.max_concurrent))
179 |     else:
180 |         print(f"Detected regular URL: {url}")
181 |         crawl_results = asyncio.run(crawl_recursive_internal_links([url], max_depth=args.max_depth, max_concurrent=args.max_concurrent))
182 | 
183 |     # Chunk and collect metadata
184 |     ids, documents, metadatas = [], [], []
185 |     chunk_idx = 0
186 |     for doc in crawl_results:
187 |         url = doc['url']
188 |         md = doc['markdown']
189 |         chunks = smart_chunk_markdown(md, max_len=args.chunk_size)
190 |         for chunk in chunks:
191 |             ids.append(f"chunk-{chunk_idx}")
192 |             documents.append(chunk)
193 |             meta = extract_section_info(chunk)
194 |             meta["chunk_index"] = chunk_idx
195 |             meta["source"] = url
196 |             metadatas.append(meta)
197 |             chunk_idx += 1
198 | 
199 |     if not documents:
200 |         print("No documents found to insert.")
201 |         sys.exit(1)
202 | 
203 |     print(f"Inserting {len(documents)} chunks into ChromaDB collection '{args.collection}'...")
204 | 
205 |     client = get_chroma_client(args.db_dir)
206 |     collection = get_or_create_collection(client, args.collection, embedding_model_name=args.embedding_model)
207 |     add_documents_to_collection(collection, ids, documents, metadatas, batch_size=args.batch_size)
208 | 
209 |     print(f"Successfully added {len(documents)} chunks to ChromaDB collection '{args.collection}'.")
210 | 
211 | if __name__ == "__main__":
212 |     main()
213 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/rag_agent.py:
--------------------------------------------------------------------------------
  1 | """Pydantic AI agent that leverages RAG with a local ChromaDB for Pydantic documentation."""
  2 | 
  3 | import os
  4 | import sys
  5 | import argparse
  6 | from dataclasses import dataclass
  7 | from typing import Optional
  8 | import asyncio
  9 | import chromadb
 10 | 
 11 | import dotenv
 12 | from pydantic_ai import RunContext
 13 | from pydantic_ai.agent import Agent
 14 | from openai import AsyncOpenAI
 15 | 
 16 | from utils import (
 17 |     get_chroma_client,
 18 |     get_or_create_collection,
 19 |     query_collection,
 20 |     format_results_as_context
 21 | )
 22 | 
 23 | # Load environment variables from .env file
 24 | dotenv.load_dotenv()
 25 | 
 26 | # Check for OpenAI API key
 27 | if not os.getenv("OPENAI_API_KEY"):
 28 |     print("Error: OPENAI_API_KEY environment variable not set.")
 29 |     print("Please create a .env file with your OpenAI API key or set it in your environment.")
 30 |     sys.exit(1)
 31 | 
 32 | 
 33 | @dataclass
 34 | class RAGDeps:
 35 |     """Dependencies for the RAG agent."""
 36 |     chroma_client: chromadb.PersistentClient
 37 |     collection_name: str
 38 |     embedding_model: str
 39 | 
 40 | 
 41 | # Create the RAG agent
 42 | agent = Agent(
 43 |     os.getenv("MODEL_CHOICE", "gpt-4.1-mini"),
 44 |     deps_type=RAGDeps,
 45 |     system_prompt="You are a helpful assistant that answers questions based on the provided documentation. "
 46 |                   "Use the retrieve tool to get relevant information from the documentation before answering. "
 47 |                   "If the documentation doesn't contain the answer, clearly state that the information isn't available "
 48 |                   "in the current documentation and provide your best general knowledge response."
 49 | )
 50 | 
 51 | 
 52 | @agent.tool
 53 | async def retrieve(context: RunContext[RAGDeps], search_query: str, n_results: int = 5) -> str:
 54 |     """Retrieve relevant documents from ChromaDB based on a search query.
 55 |     
 56 |     Args:
 57 |         context: The run context containing dependencies.
 58 |         search_query: The search query to find relevant documents.
 59 |         n_results: Number of results to return (default: 5).
 60 |         
 61 |     Returns:
 62 |         Formatted context information from the retrieved documents.
 63 |     """
 64 |     # Get ChromaDB client and collection
 65 |     collection = get_or_create_collection(
 66 |         context.deps.chroma_client,
 67 |         context.deps.collection_name,
 68 |         embedding_model_name=context.deps.embedding_model
 69 |     )
 70 |     
 71 |     # Query the collection
 72 |     query_results = query_collection(
 73 |         collection,
 74 |         search_query,
 75 |         n_results=n_results
 76 |     )
 77 |     
 78 |     # Format the results as context
 79 |     return format_results_as_context(query_results)
 80 | 
 81 | 
 82 | async def run_rag_agent(
 83 |     question: str,
 84 |     collection_name: str = "docs",
 85 |     db_directory: str = "./chroma_db",
 86 |     embedding_model: str = "all-MiniLM-L6-v2",
 87 |     n_results: int = 5
 88 | ) -> str:
 89 |     """Run the RAG agent to answer a question about Pydantic AI.
 90 |     
 91 |     Args:
 92 |         question: The question to answer.
 93 |         collection_name: Name of the ChromaDB collection to use.
 94 |         db_directory: Directory where ChromaDB data is stored.
 95 |         embedding_model: Name of the embedding model to use.
 96 |         n_results: Number of results to return from the retrieval.
 97 |         
 98 |     Returns:
 99 |         The agent's response.
100 |     """
101 |     # Create dependencies
102 |     deps = RAGDeps(
103 |         chroma_client=get_chroma_client(db_directory),
104 |         collection_name=collection_name,
105 |         embedding_model=embedding_model
106 |     )
107 |     
108 |     # Run the agent
109 |     result = await agent.run(question, deps=deps)
110 |     
111 |     return result.data
112 | 
113 | 
114 | def main():
115 |     """Main function to parse arguments and run the RAG agent."""
116 |     parser = argparse.ArgumentParser(description="Run a Pydantic AI agent with RAG using ChromaDB")
117 |     parser.add_argument("--question", help="The question to answer about Pydantic AI")
118 |     parser.add_argument("--collection", default="docs", help="Name of the ChromaDB collection")
119 |     parser.add_argument("--db-dir", default="./chroma_db", help="Directory where ChromaDB data is stored")
120 |     parser.add_argument("--embedding-model", default="all-MiniLM-L6-v2", help="Name of the embedding model to use")
121 |     parser.add_argument("--n-results", type=int, default=5, help="Number of results to return from the retrieval")
122 |     
123 |     args = parser.parse_args()
124 |     
125 |     # Run the agent
126 |     response = asyncio.run(run_rag_agent(
127 |         args.question,
128 |         collection_name=args.collection,
129 |         db_directory=args.db_dir,
130 |         embedding_model=args.embedding_model,
131 |         n_results=args.n_results
132 |     ))
133 |     
134 |     print("\nResponse:")
135 |     print(response)
136 | 
137 | 
138 | if __name__ == "__main__":
139 |     main()
140 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/requirements.txt:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/coleam00/ottomator-agents/main/crawl4AI-agent-v2/requirements.txt


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/streamlit_app.py:
--------------------------------------------------------------------------------
  1 | from dotenv import load_dotenv
  2 | import streamlit as st
  3 | import asyncio
  4 | import os
  5 | 
  6 | # Import all the message part classes
  7 | from pydantic_ai.messages import (
  8 |     ModelMessage,
  9 |     ModelRequest,
 10 |     ModelResponse,
 11 |     SystemPromptPart,
 12 |     UserPromptPart,
 13 |     TextPart,
 14 |     ToolCallPart,
 15 |     ToolReturnPart,
 16 |     RetryPromptPart,
 17 |     ModelMessagesTypeAdapter
 18 | )
 19 | 
 20 | from rag_agent import agent, RAGDeps
 21 | from utils import get_chroma_client
 22 | 
 23 | load_dotenv()
 24 | 
 25 | async def get_agent_deps():
 26 |     return RAGDeps(
 27 |         chroma_client=get_chroma_client("./chroma_db"),
 28 |         collection_name="docs",
 29 |         embedding_model="all-MiniLM-L6-v2"
 30 |     )
 31 | 
 32 | 
 33 | def display_message_part(part):
 34 |     """
 35 |     Display a single part of a message in the Streamlit UI.
 36 |     Customize how you display system prompts, user prompts,
 37 |     tool calls, tool returns, etc.
 38 |     """
 39 |     # user-prompt
 40 |     if part.part_kind == 'user-prompt':
 41 |         with st.chat_message("user"):
 42 |             st.markdown(part.content)
 43 |     # text
 44 |     elif part.part_kind == 'text':
 45 |         with st.chat_message("assistant"):
 46 |             st.markdown(part.content)             
 47 | 
 48 | async def run_agent_with_streaming(user_input):
 49 |     async with agent.run_stream(
 50 |         user_input, deps=st.session_state.agent_deps, message_history=st.session_state.messages
 51 |     ) as result:
 52 |         async for message in result.stream_text(delta=True):  
 53 |             yield message
 54 | 
 55 |     # Add the new messages to the chat history (including tool calls and responses)
 56 |     st.session_state.messages.extend(result.new_messages())
 57 | 
 58 | 
 59 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 60 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 61 | # ~~~~~~~~~~~~~~~~~~ Main Function with UI Creation ~~~~~~~~~~~~~~~~~~~~
 62 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 63 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 64 | 
 65 | async def main():
 66 |     st.title("ChromaDB Crawl4AI RAG AI Agent")
 67 | 
 68 |     # Initialize chat history in session state if not present
 69 |     if "messages" not in st.session_state:
 70 |         st.session_state.messages = []
 71 |     if "agent_deps" not in st.session_state:
 72 |         st.session_state.agent_deps = await get_agent_deps()  
 73 | 
 74 |     # Display all messages from the conversation so far
 75 |     # Each message is either a ModelRequest or ModelResponse.
 76 |     # We iterate over their parts to decide how to display them.
 77 |     for msg in st.session_state.messages:
 78 |         if isinstance(msg, ModelRequest) or isinstance(msg, ModelResponse):
 79 |             for part in msg.parts:
 80 |                 display_message_part(part)
 81 | 
 82 |     # Chat input for the user
 83 |     user_input = st.chat_input("What do you want to know?")
 84 | 
 85 |     if user_input:
 86 |         # Display user prompt in the UI
 87 |         with st.chat_message("user"):
 88 |             st.markdown(user_input)
 89 | 
 90 |         # Display the assistant's partial response while streaming
 91 |         with st.chat_message("assistant"):
 92 |             # Create a placeholder for the streaming text
 93 |             message_placeholder = st.empty()
 94 |             full_response = ""
 95 |             
 96 |             # Properly consume the async generator with async for
 97 |             generator = run_agent_with_streaming(user_input)
 98 |             async for message in generator:
 99 |                 full_response += message
100 |                 message_placeholder.markdown(full_response + "▌")
101 |             
102 |             # Final response without the cursor
103 |             message_placeholder.markdown(full_response)
104 | 
105 | 
106 | if __name__ == "__main__":
107 |     asyncio.run(main())
108 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/utils.py:
--------------------------------------------------------------------------------
  1 | """Utility functions for text processing and ChromaDB operations."""
  2 | 
  3 | import os
  4 | import pathlib
  5 | from typing import List, Dict, Any, Optional
  6 | 
  7 | import chromadb
  8 | from chromadb.utils import embedding_functions
  9 | from more_itertools import batched
 10 | 
 11 | 
 12 | def get_chroma_client(persist_directory: str) -> chromadb.PersistentClient:
 13 |     """Get a ChromaDB client with the specified persistence directory.
 14 |     
 15 |     Args:
 16 |         persist_directory: Directory where ChromaDB will store its data
 17 |         
 18 |     Returns:
 19 |         A ChromaDB PersistentClient
 20 |     """
 21 |     # Create the directory if it doesn't exist
 22 |     os.makedirs(persist_directory, exist_ok=True)
 23 |     
 24 |     # Return the client
 25 |     return chromadb.PersistentClient(persist_directory)
 26 | 
 27 | 
 28 | def get_or_create_collection(
 29 |     client: chromadb.PersistentClient,
 30 |     collection_name: str,
 31 |     embedding_model_name: str = "all-MiniLM-L6-v2",
 32 |     distance_function: str = "cosine",
 33 | ) -> chromadb.Collection:
 34 |     """Get an existing collection or create a new one if it doesn't exist.
 35 |     
 36 |     Args:
 37 |         client: ChromaDB client
 38 |         collection_name: Name of the collection
 39 |         embedding_model_name: Name of the embedding model to use
 40 |         distance_function: Distance function to use for similarity search
 41 |         
 42 |     Returns:
 43 |         A ChromaDB Collection
 44 |     """
 45 |     # Create embedding function
 46 |     embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
 47 |         model_name=embedding_model_name
 48 |     )
 49 |     
 50 |     # Try to get the collection, create it if it doesn't exist
 51 |     try:
 52 |         return client.get_collection(
 53 |             name=collection_name,
 54 |             embedding_function=embedding_func
 55 |         )
 56 |     except Exception:
 57 |         return client.create_collection(
 58 |             name=collection_name,
 59 |             embedding_function=embedding_func,
 60 |             metadata={"hnsw:space": distance_function}
 61 |         )
 62 | 
 63 | 
 64 | def add_documents_to_collection(
 65 |     collection: chromadb.Collection,
 66 |     ids: List[str],
 67 |     documents: List[str],
 68 |     metadatas: Optional[List[Dict[str, Any]]] = None,
 69 |     batch_size: int = 100,
 70 | ) -> None:
 71 |     """Add documents to a ChromaDB collection in batches.
 72 |     
 73 |     Args:
 74 |         collection: ChromaDB collection
 75 |         ids: List of document IDs
 76 |         documents: List of document texts
 77 |         metadatas: Optional list of metadata dictionaries for each document
 78 |         batch_size: Size of batches for adding documents
 79 |     """
 80 |     # Create default metadata if none provided
 81 |     if metadatas is None:
 82 |         metadatas = [{}] * len(documents)
 83 |     
 84 |     # Create document indices
 85 |     document_indices = list(range(len(documents)))
 86 |     
 87 |     # Add documents in batches
 88 |     for batch in batched(document_indices, batch_size):
 89 |         # Get the start and end indices for the current batch
 90 |         start_idx = batch[0]
 91 |         end_idx = batch[-1] + 1  # +1 because end_idx is exclusive
 92 |         
 93 |         # Add the batch to the collection
 94 |         collection.add(
 95 |             ids=ids[start_idx:end_idx],
 96 |             documents=documents[start_idx:end_idx],
 97 |             metadatas=metadatas[start_idx:end_idx],
 98 |         )
 99 | 
100 | 
101 | def query_collection(
102 |     collection: chromadb.Collection,
103 |     query_text: str,
104 |     n_results: int = 5,
105 |     where: Optional[Dict[str, Any]] = None,
106 | ) -> Dict[str, Any]:
107 |     """Query a ChromaDB collection for similar documents.
108 |     
109 |     Args:
110 |         collection: ChromaDB collection
111 |         query_text: Text to search for
112 |         n_results: Number of results to return
113 |         where: Optional filter to apply to the query
114 |         
115 |     Returns:
116 |         Query results containing documents, metadatas, distances, and ids
117 |     """
118 |     # Query the collection
119 |     return collection.query(
120 |         query_texts=[query_text],
121 |         n_results=n_results,
122 |         where=where,
123 |         include=["documents", "metadatas", "distances"]
124 |     )
125 | 
126 | 
127 | def format_results_as_context(query_results: Dict[str, Any]) -> str:
128 |     """Format query results as a context string for the agent.
129 |     
130 |     Args:
131 |         query_results: Results from a ChromaDB query
132 |         
133 |     Returns:
134 |         Formatted context string
135 |     """
136 |     context = "CONTEXT INFORMATION:\n\n"
137 |     
138 |     for i, (doc, metadata, distance) in enumerate(zip(
139 |         query_results["documents"][0],
140 |         query_results["metadatas"][0],
141 |         query_results["distances"][0]
142 |     )):
143 |         # Add document information
144 |         context += f"Document {i+1} (Relevance: {1 - distance:.2f}):\n"
145 |         
146 |         # Add metadata if available
147 |         if metadata:
148 |             for key, value in metadata.items():
149 |                 context += f"{key}: {value}\n"
150 |         
151 |         # Add document content
152 |         context += f"Content: {doc}\n\n"
153 |     
154 |     return context
155 | 


--------------------------------------------------------------------------------└── crawl4AI-agent-v2
    ├── .env.example
    ├── README.md
    ├── crawl4AI-examples
        ├── 1-crawl_single_page.py
        ├── 2-crawl_docs_sequential.py
        ├── 3-crawl_sitemap_in_parallel.py
        ├── 4-crawl_llms_txt.py
        └── 5-crawl_site_recursively.py
    ├── insert_docs.py
    ├── rag_agent.py
    ├── requirements.txt
    ├── streamlit_app.py
    └── utils.py


/crawl4AI-agent-v2/.env.example:
--------------------------------------------------------------------------------
1 | # Get your Open AI API Key by following these instructions -
2 | # https://help.openai.com/en/articles/4936850-where-do-i-find-my-openai-api-key
3 | # You only need this environment variable set if you are using GPT (and not Ollama)
4 | OPENAI_API_KEY=
5 | 
6 | # The LLM you want to use from OpenAI. See the list of models here:
7 | # https://platform.openai.com/docs/models
8 | # Example: gpt-4.1-mini
9 | MODEL_CHOICE=


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/README.md:
--------------------------------------------------------------------------------
  1 | # Pydantic AI Documentation Crawler & RAG Agent
  2 | 
  3 | An intelligent documentation crawler and retrieval-augmented generation (RAG) system, powered by Crawl4AI and Pydantic AI. This project enables you to crawl, chunk, and vectorize documentation from any website, `.txt`/Markdown pages (llms.txt), or sitemap, and interact with the knowledge base using a Streamlit interface.
  4 | 
  5 | ---
  6 | 
  7 | ## Features
  8 | 
  9 | - **Flexible documentation crawling:** Handles regular websites, `.txt`/Markdown pages (llms.txt), and sitemaps.
 10 | - **Parallel and recursive crawling:** Efficiently gathers large doc sites with memory-adaptive batching.
 11 | - **Smart chunking:** Hierarchical Markdown chunking by headers, ensuring chunks are optimal for vector search.
 12 | - **Vector database integration:** Stores chunks and metadata in ChromaDB for fast semantic retrieval.
 13 | - **Streamlit RAG interface:** Query your documentation with LLM-powered semantic search.
 14 | - **Extensible examples:** Modular scripts for various crawling and RAG workflows.
 15 | 
 16 | ---
 17 | 
 18 | ## Prerequisites
 19 | 
 20 | - Python 3.11+
 21 | - OpenAI API key (for embeddings and LLM-powered search)
 22 | - Crawl4AI/Playwright and other dependencies in `requirements.txt`
 23 | - (Optional) Streamlit for the web interface
 24 | 
 25 | ---
 26 | 
 27 | ## Installation
 28 | 
 29 | 1. **Clone the repository:**
 30 |    ```bash
 31 |    git clone https://github.com/coleam00/ottomator-agents.git
 32 |    cd ottomator-agents/crawl4AI-agent-v2
 33 |    ```
 34 | 
 35 | 2. **Install dependencies:**
 36 |    ```bash
 37 |    python -m venv venv
 38 |    source venv/bin/activate  # On Windows: venv\Scripts\activate
 39 |    pip install -r requirements.txt
 40 |    playwright install
 41 |    ```
 42 | 
 43 | 3. **Set up environment variables:**
 44 |    - Copy `.env.example` to `.env`
 45 |    - Edit `.env` with your API keys and preferences:
 46 |      ```env
 47 |      OPENAI_API_KEY=your_openai_api_key
 48 |      MODEL_CHOICE=gpt-4.1-mini  # or your preferred OpenAI model
 49 |      ```
 50 | 
 51 | ---
 52 | 
 53 | ## Usage
 54 | 
 55 | ### 1. Crawling and Inserting Documentation
 56 | 
 57 | The main entry point for crawling and vectorizing documentation is [`insert_docs.py`](insert_docs.py):
 58 | 
 59 | #### Supported URL Types
 60 | 
 61 | - **Regular documentation sites:** Recursively crawls all internal links, deduplicates by URL (ignoring fragments).
 62 | - **Markdown or .txt pages (such as llms.txt):** Fetches and chunks Markdown content.
 63 | - **Sitemaps (`sitemap.xml`):** Batch-crawls all URLs listed in the sitemap.
 64 | 
 65 | #### Example Usage
 66 | 
 67 | ```bash
 68 | python insert_docs.py <URL> [--collection mydocs] [--db-dir ./chroma_db] [--embedding-model all-MiniLM-L6-v2] [--chunk-size 1000] [--max-depth 3] [--max-concurrent 10] [--batch-size 100]
 69 | ```
 70 | 
 71 | **Arguments:**
 72 | - `URL`: The root URL, .txt file, or sitemap to crawl.
 73 | - `--collection`: ChromaDB collection name (default: `docs`)
 74 | - `--db-dir`: Directory for ChromaDB data (default: `./chroma_db`)
 75 | - `--embedding-model`: Embedding model for vector storage (default: `all-MiniLM-L6-v2`)
 76 | - `--chunk-size`: Maximum characters per chunk (default: `1000`)
 77 | - `--max-depth`: Recursion depth for regular URLs (default: `3`)
 78 | - `--max-concurrent`: Max parallel browser sessions (default: `10`)
 79 | - `--batch-size`: Batch size for ChromaDB insertion (default: `100`)
 80 | 
 81 | **Examples for each type (regular URL, .txt, sitemap):**
 82 | ```bash
 83 | python insert_docs.py https://ai.pydantic.dev/
 84 | python insert_docs.py https://ai.pydantic.dev/llms-full.txt
 85 | python insert_docs.py https://ai.pydantic.dev/sitemap.xml
 86 | ```
 87 | 
 88 | #### Chunking Strategy
 89 | 
 90 | - Splits content first by `#`, then by `##`, then by `###` headers.
 91 | - If a chunk is still too large, splits by character count.
 92 | - All chunks are less than the specified `--chunk-size` (default: 1000 characters).
 93 | 
 94 | #### Metadata
 95 | 
 96 | Each chunk is stored with:
 97 | - Source URL
 98 | - Chunk index
 99 | - Extracted headers
100 | - Character and word counts
101 | 
102 | ---
103 | 
104 | ### 2. Example Scripts
105 | 
106 | The `crawl4AI-examples/` folder contains modular scripts illustrating different crawling and chunking strategies:
107 | 
108 | - **`3-crawl_sitemap_in_parallel.py`:** Batch-crawls a list of URLs from a sitemap in parallel with memory tracking.
109 | - **`4-crawl_llms_txt.py`:** Crawls a Markdown or `.txt` file, splits by headers, and prints chunks.
110 | - **`5-crawl_site_recursively.py`:** Recursively crawls all internal links from a root URL, deduplicating by URL (ignoring fragments).
111 | 
112 | You can use these scripts directly for experimentation or as templates for custom crawlers.
113 | 
114 | ---
115 | 
116 | ### 3. Running the Streamlit RAG Interface
117 | 
118 | After crawling and inserting docs, launch the Streamlit app for semantic search and question answering:
119 | 
120 | ```bash
121 | streamlit run streamlit_app.py
122 | ```
123 | 
124 | - The interface will be available at [http://localhost:8501](http://localhost:8501)
125 | - Query your documentation using natural language and get context-rich answers.
126 | 
127 | ---
128 | 
129 | ## Project Structure
130 | 
131 | ```
132 | crawl4AI-agent-v2/
133 | ├── crawl4AI-examples/
134 | │   ├── 3-crawl_docs_FAST.py
135 | │   ├── 4-crawl_and_chunk_markdown.py
136 | │   └── 5-crawl_recursive_internal_links.py
137 | ├── insert_docs.py
138 | ├── rag_agent.py
139 | ├── streamlit_app.py
140 | ├── utils.py
141 | ├── requirements.txt
142 | ├── .env.example
143 | └── README.md
144 | ```
145 | 
146 | ---
147 | 
148 | ## Advanced Usage & Customization
149 | 
150 | - **Chunking:** Tune `--chunk-size` for your retrieval use case.
151 | - **Embeddings:** Swap out the embedding model with `--embedding-model`.
152 | - **Crawling:** Adjust `--max-depth` and `--max-concurrent` for large sites.
153 | - **Vector DB:** Use your own ChromaDB directory or collection for multiple projects.
154 | 
155 | ---
156 | 
157 | ## Troubleshooting
158 | 
159 | - Ensure all dependencies are installed and environment variables are set.
160 | - For large sites, increase memory or decrease `--max-concurrent`.
161 | - If you encounter crawling issues, try running the example scripts for isolated debugging.


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/crawl4AI-examples/1-crawl_single_page.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | from crawl4ai import AsyncWebCrawler, BrowserConfig
 3 | 
 4 | async def main():
 5 |     async with AsyncWebCrawler() as crawler:
 6 |         result = await crawler.arun(
 7 |             url="https://ai.pydantic.dev/",
 8 |         )
 9 |         print(result.markdown)
10 | 
11 | if __name__ == "__main__":
12 |     asyncio.run(main())


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/crawl4AI-examples/2-crawl_docs_sequential.py:
--------------------------------------------------------------------------------
 1 | import asyncio
 2 | from typing import List
 3 | from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
 4 | from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
 5 | import requests
 6 | from xml.etree import ElementTree
 7 | 
 8 | async def crawl_sequential(urls: List[str]):
 9 |     print("\n=== Sequential Crawling with Session Reuse ===")
10 | 
11 |     browser_config = BrowserConfig(
12 |         headless=True,
13 |         # For better performance in Docker or low-memory environments:
14 |         extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
15 |     )
16 | 
17 |     crawl_config = CrawlerRunConfig(
18 |         markdown_generator=DefaultMarkdownGenerator()
19 |     )
20 | 
21 |     # Create the crawler (opens the browser)
22 |     crawler = AsyncWebCrawler(config=browser_config)
23 |     await crawler.start()
24 | 
25 |     try:
26 |         session_id = "session1"  # Reuse the same session across all URLs
27 |         for url in urls:
28 |             result = await crawler.arun(
29 |                 url=url,
30 |                 config=crawl_config,
31 |                 session_id=session_id
32 |             )
33 |             if result.success:
34 |                 print(f"Successfully crawled: {url}")
35 |                 # E.g. check markdown length
36 |                 print(f"Markdown length: {len(result.markdown.raw_markdown)}")
37 |             else:
38 |                 print(f"Failed: {url} - Error: {result.error_message}")
39 |     finally:
40 |         # After all URLs are done, close the crawler (and the browser)
41 |         await crawler.close()
42 | 
43 | def get_pydantic_ai_docs_urls():
44 |     """
45 |     Fetches all URLs from the Pydantic AI documentation.
46 |     Uses the sitemap (https://ai.pydantic.dev/sitemap.xml) to get these URLs.
47 |     
48 |     Returns:
49 |         List[str]: List of URLs
50 |     """            
51 |     sitemap_url = "https://ai.pydantic.dev/sitemap.xml"
52 |     try:
53 |         response = requests.get(sitemap_url)
54 |         response.raise_for_status()
55 |         
56 |         # Parse the XML
57 |         root = ElementTree.fromstring(response.content)
58 |         
59 |         # Extract all URLs from the sitemap
60 |         # The namespace is usually defined in the root element
61 |         namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
62 |         urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
63 |         
64 |         return urls
65 |     except Exception as e:
66 |         print(f"Error fetching sitemap: {e}")
67 |         return []
68 | 
69 | async def main():
70 |     urls = get_pydantic_ai_docs_urls()
71 |     if urls:
72 |         print(f"Found {len(urls)} URLs to crawl")
73 |         await crawl_sequential(urls)
74 |     else:
75 |         print("No URLs found to crawl")
76 | 
77 | if __name__ == "__main__":
78 |     asyncio.run(main())
79 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/crawl4AI-examples/3-crawl_sitemap_in_parallel.py:
--------------------------------------------------------------------------------
  1 | """
  2 | 3-crawl_docs_FAST.py
  3 | --------------------
  4 | Batch-crawls a list of documentation URLs in parallel using Crawl4AI's arun_many and a memory-adaptive dispatcher.
  5 | Tracks memory usage, prints a summary of successes/failures, and is suitable for large-scale doc scraping jobs.
  6 | Usage: Call main() or run as a script. Adjust max_concurrent for parallelism.
  7 | """
  8 | import os
  9 | import sys
 10 | import psutil
 11 | import asyncio
 12 | import requests
 13 | from typing import List
 14 | from xml.etree import ElementTree
 15 | from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, MemoryAdaptiveDispatcher
 16 | 
 17 | async def crawl_parallel(urls: List[str], max_concurrent: int = 10):
 18 |     print("\n=== Parallel Crawling with arun_many + Dispatcher ===")
 19 | 
 20 |     # Track the peak memory usage for observability
 21 |     peak_memory = 0
 22 |     process = psutil.Process(os.getpid())
 23 |     def log_memory(prefix: str = ""):
 24 |         nonlocal peak_memory
 25 |         current_mem = process.memory_info().rss  # in bytes
 26 |         if current_mem > peak_memory:
 27 |             peak_memory = current_mem
 28 |         print(f"{prefix} Current Memory: {current_mem // (1024 * 1024)} MB, Peak: {peak_memory // (1024 * 1024)} MB")
 29 | 
 30 |     # Configure the browser for headless operation and resource limits
 31 |     browser_config = BrowserConfig(
 32 |         headless=True,
 33 |         verbose=False,
 34 |         extra_args=["--disable-gpu", "--disable-dev-shm-usage", "--no-sandbox"],
 35 |     )
 36 |     # Set up crawl config and dispatcher for batch crawling
 37 |     crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, stream=False)
 38 |     dispatcher = MemoryAdaptiveDispatcher(
 39 |         memory_threshold_percent=70.0,  # Don't exceed 70% memory usage
 40 |         check_interval=1.0,             # Check memory every second
 41 |         max_session_permit=max_concurrent  # Max parallel browser sessions
 42 |     )
 43 | 
 44 |     async with AsyncWebCrawler(config=browser_config) as crawler:
 45 |         log_memory("Before crawl: ")
 46 |         # arun_many handles all URLs in parallel, batching and resource management handled by dispatcher
 47 |         results = await crawler.arun_many(
 48 |             urls=urls,
 49 |             config=crawl_config,
 50 |             dispatcher=dispatcher
 51 |         )
 52 |         success_count = 0
 53 |         fail_count = 0
 54 |         # Loop through all crawl results and tally success/failure
 55 |         for result in results:
 56 |             if result.success:
 57 |                 success_count += 1
 58 |             else:
 59 |                 print(f"Error crawling {result.url}: {result.error_message}")
 60 |                 fail_count += 1
 61 | 
 62 |         print(f"\nSummary:")
 63 |         print(f"  - Successfully crawled: {success_count}")
 64 |         print(f"  - Failed: {fail_count}")
 65 |         log_memory("After crawl: ")
 66 |         print(f"\nPeak memory usage (MB): {peak_memory // (1024 * 1024)}")
 67 | 
 68 | def get_pydantic_ai_docs_urls():
 69 |     """
 70 |     Fetches all URLs from the Pydantic AI documentation.
 71 |     Uses the sitemap (https://ai.pydantic.dev/sitemap.xml) to get these URLs.
 72 |     
 73 |     Returns:
 74 |         List[str]: List of URLs
 75 |     """            
 76 |     sitemap_url = "https://ai.pydantic.dev/sitemap.xml"
 77 |     try:
 78 |         response = requests.get(sitemap_url)
 79 |         response.raise_for_status()
 80 |         
 81 |         # Parse the XML
 82 |         root = ElementTree.fromstring(response.content)
 83 |         
 84 |         # Extract all URLs from the sitemap
 85 |         # The namespace is usually defined in the root element
 86 |         namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
 87 |         urls = [loc.text for loc in root.findall('.//ns:loc', namespace)]
 88 |         
 89 |         return urls
 90 |     except Exception as e:
 91 |         print(f"Error fetching sitemap: {e}")
 92 |         return []        
 93 | 
 94 | async def main():
 95 |     urls = get_pydantic_ai_docs_urls()
 96 |     if urls:
 97 |         print(f"Found {len(urls)} URLs to crawl")
 98 |         await crawl_parallel(urls, max_concurrent=10)
 99 |     else:
100 |         print("No URLs found to crawl")    
101 | 
102 | if __name__ == "__main__":
103 |     asyncio.run(main())
104 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/crawl4AI-examples/4-crawl_llms_txt.py:
--------------------------------------------------------------------------------
 1 | """
 2 | 4-crawl_and_chunk_markdown.py
 3 | -----------------------------
 4 | Scrapes a Markdown (.md or .txt) page using Crawl4AI, then splits the content into chunks based on # and ## headers.
 5 | Prints each chunk for further processing or inspection.
 6 | Usage: Set the target URL in main(), then run as a script.
 7 | """
 8 | import asyncio
 9 | from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
10 | import re
11 | 
12 | async def scrape_and_chunk_markdown(url: str):
13 |     """
14 |     Scrape a Markdown page and split into chunks by # and ## headers.
15 |     """
16 |     browser_config = BrowserConfig(headless=True)
17 |     crawl_config = CrawlerRunConfig()
18 |     async with AsyncWebCrawler(config=browser_config) as crawler:
19 |         result = await crawler.arun(url=url, config=crawl_config)
20 |         if not result.success:
21 |             print(f"Failed to crawl {url}: {result.error_message}")
22 |             return
23 |         markdown = result.markdown
24 |         # Split by headers (#, ##)
25 |         # Find all # and ## headers to use as chunk boundaries
26 |         header_pattern = re.compile(r'^(# .+|## .+)
#39;, re.MULTILINE)
27 |         headers = [m.start() for m in header_pattern.finditer(markdown)] + [len(markdown)]
28 |         chunks = []
29 |         # Split the markdown into chunks between headers
30 |         for i in range(len(headers)-1):
31 |             chunk = markdown[headers[i]:headers[i+1]].strip()
32 |             if chunk:
33 |                 chunks.append(chunk)
34 |         print(f"Split into {len(chunks)} chunks:")
35 |         for idx, chunk in enumerate(chunks):
36 |             print(f"\n--- Chunk {idx+1} ---\n{chunk}\n")
37 | 
38 | if __name__ == "__main__":
39 |     url = "https://ai.pydantic.dev/llms-full.txt"
40 |     asyncio.run(scrape_and_chunk_markdown(url))
41 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/crawl4AI-examples/5-crawl_site_recursively.py:
--------------------------------------------------------------------------------
 1 | """
 2 | 5-crawl_recursive_internal_links.py
 3 | ----------------------------------
 4 | Recursively crawls a site starting from a root URL, using Crawl4AI's arun_many and a memory-adaptive dispatcher.
 5 | At each depth, all internal links are discovered and crawled in parallel, up to a specified depth, with deduplication.
 6 | Usage: Set the start URL and max_depth in main(), then run as a script.
 7 | """
 8 | import asyncio
 9 | from urllib.parse import urldefrag
10 | from crawl4ai import (
11 |     AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode,
12 |     MemoryAdaptiveDispatcher
13 | )
14 | 
15 | async def crawl_recursive_batch(start_urls, max_depth=3, max_concurrent=10):
16 |     browser_config = BrowserConfig(headless=True, verbose=False)
17 |     run_config = CrawlerRunConfig(
18 |         cache_mode=CacheMode.BYPASS,
19 |         stream=False
20 |     )
21 |     dispatcher = MemoryAdaptiveDispatcher(
22 |         memory_threshold_percent=70.0,      # Don't exceed 70% memory usage
23 |         check_interval=1.0,                 # Check memory every second
24 |         max_session_permit=max_concurrent   # Max parallel browser sessions
25 |     )
26 | 
27 |     # Track visited URLs to prevent revisiting and infinite loops (ignoring fragments)
28 |     visited = set()
29 |     def normalize_url(url):
30 |         # Remove fragment (part after #)
31 |         return urldefrag(url)[0]
32 |     current_urls = set([normalize_url(u) for u in start_urls])
33 | 
34 |     async with AsyncWebCrawler(config=browser_config) as crawler:
35 |         for depth in range(max_depth):
36 |             print(f"\n=== Crawling Depth {depth+1} ===")
37 |             # Only crawl URLs we haven't seen yet (ignoring fragments)
38 |             urls_to_crawl = [normalize_url(url) for url in current_urls if normalize_url(url) not in visited]
39 | 
40 |             if not urls_to_crawl:
41 |                 break
42 | 
43 |             # Batch-crawl all URLs at this depth in parallel
44 |             results = await crawler.arun_many(
45 |                 urls=urls_to_crawl,
46 |                 config=run_config,
47 |                 dispatcher=dispatcher
48 |             )
49 | 
50 |             next_level_urls = set()
51 | 
52 |             for result in results:
53 |                 norm_url = normalize_url(result.url)
54 |                 visited.add(norm_url)  # Mark as visited (no fragment)
55 |                 if result.success:
56 |                     print(f"[OK] {result.url} | Markdown: {len(result.markdown) if result.markdown else 0} chars")
57 |                     # Collect all new internal links for the next depth
58 |                     for link in result.links.get("internal", []):
59 |                         next_url = normalize_url(link["href"])
60 |                         if next_url not in visited:
61 |                             next_level_urls.add(next_url)
62 |                 else:
63 |                     print(f"[ERROR] {result.url}: {result.error_message}")
64 |                     
65 |             # Move to the next set of URLs for the next recursion depth
66 |             current_urls = next_level_urls
67 | 
68 | if __name__ == "__main__":
69 |     asyncio.run(crawl_recursive_batch(["https://ai.pydantic.dev/"], max_depth=3, max_concurrent=10))
70 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/insert_docs.py:
--------------------------------------------------------------------------------
  1 | """
  2 | insert_docs.py
  3 | --------------
  4 | Command-line utility to crawl any URL using Crawl4AI, detect content type (sitemap, .txt, or regular page),
  5 | use the appropriate crawl method, chunk the resulting Markdown into <1000 character blocks by header hierarchy,
  6 | and insert all chunks into ChromaDB with metadata.
  7 | 
  8 | Usage:
  9 |     python insert_docs.py <URL> [--collection ...] [--db-dir ...] [--embedding-model ...]
 10 | """
 11 | import argparse
 12 | import sys
 13 | import re
 14 | import asyncio
 15 | from typing import List, Dict, Any
 16 | from urllib.parse import urlparse, urldefrag
 17 | from xml.etree import ElementTree
 18 | from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, MemoryAdaptiveDispatcher
 19 | import requests
 20 | from utils import get_chroma_client, get_or_create_collection, add_documents_to_collection
 21 | 
 22 | def smart_chunk_markdown(markdown: str, max_len: int = 1000) -> List[str]:
 23 |     """Hierarchically splits markdown by #, ##, ### headers, then by characters, to ensure all chunks < max_len."""
 24 |     def split_by_header(md, header_pattern):
 25 |         indices = [m.start() for m in re.finditer(header_pattern, md, re.MULTILINE)]
 26 |         indices.append(len(md))
 27 |         return [md[indices[i]:indices[i+1]].strip() for i in range(len(indices)-1) if md[indices[i]:indices[i+1]].strip()]
 28 | 
 29 |     chunks = []
 30 | 
 31 |     for h1 in split_by_header(markdown, r'^# .+
#39;):
 32 |         if len(h1) > max_len:
 33 |             for h2 in split_by_header(h1, r'^## .+
#39;):
 34 |                 if len(h2) > max_len:
 35 |                     for h3 in split_by_header(h2, r'^### .+
#39;):
 36 |                         if len(h3) > max_len:
 37 |                             for i in range(0, len(h3), max_len):
 38 |                                 chunks.append(h3[i:i+max_len].strip())
 39 |                         else:
 40 |                             chunks.append(h3)
 41 |                 else:
 42 |                     chunks.append(h2)
 43 |         else:
 44 |             chunks.append(h1)
 45 | 
 46 |     final_chunks = []
 47 | 
 48 |     for c in chunks:
 49 |         if len(c) > max_len:
 50 |             final_chunks.extend([c[i:i+max_len].strip() for i in range(0, len(c), max_len)])
 51 |         else:
 52 |             final_chunks.append(c)
 53 | 
 54 |     return [c for c in final_chunks if c]
 55 | 
 56 | def is_sitemap(url: str) -> bool:
 57 |     return url.endswith('sitemap.xml') or 'sitemap' in urlparse(url).path
 58 | 
 59 | def is_txt(url: str) -> bool:
 60 |     return url.endswith('.txt')
 61 | 
 62 | async def crawl_recursive_internal_links(start_urls, max_depth=3, max_concurrent=10) -> List[Dict[str,Any]]:
 63 |     """Recursive crawl using logic from 5-crawl_recursive_internal_links.py. Returns list of dicts with url and markdown."""
 64 |     browser_config = BrowserConfig(headless=True, verbose=False)
 65 |     run_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, stream=False)
 66 |     dispatcher = MemoryAdaptiveDispatcher(
 67 |         memory_threshold_percent=70.0,
 68 |         check_interval=1.0,
 69 |         max_session_permit=max_concurrent
 70 |     )
 71 | 
 72 |     visited = set()
 73 | 
 74 |     def normalize_url(url):
 75 |         return urldefrag(url)[0]
 76 | 
 77 |     current_urls = set([normalize_url(u) for u in start_urls])
 78 |     results_all = []
 79 | 
 80 |     async with AsyncWebCrawler(config=browser_config) as crawler:
 81 |         for depth in range(max_depth):
 82 |             urls_to_crawl = [normalize_url(url) for url in current_urls if normalize_url(url) not in visited]
 83 |             if not urls_to_crawl:
 84 |                 break
 85 | 
 86 |             results = await crawler.arun_many(urls=urls_to_crawl, config=run_config, dispatcher=dispatcher)
 87 |             next_level_urls = set()
 88 | 
 89 |             for result in results:
 90 |                 norm_url = normalize_url(result.url)
 91 |                 visited.add(norm_url)
 92 | 
 93 |                 if result.success and result.markdown:
 94 |                     results_all.append({'url': result.url, 'markdown': result.markdown})
 95 |                     for link in result.links.get("internal", []):
 96 |                         next_url = normalize_url(link["href"])
 97 |                         if next_url not in visited:
 98 |                             next_level_urls.add(next_url)
 99 | 
100 |             current_urls = next_level_urls
101 | 
102 |     return results_all
103 | 
104 | async def crawl_markdown_file(url: str) -> List[Dict[str,Any]]:
105 |     """Crawl a .txt or markdown file using logic from 4-crawl_and_chunk_markdown.py."""
106 |     browser_config = BrowserConfig(headless=True)
107 |     crawl_config = CrawlerRunConfig()
108 | 
109 |     async with AsyncWebCrawler(config=browser_config) as crawler:
110 |         result = await crawler.arun(url=url, config=crawl_config)
111 |         if result.success and result.markdown:
112 |             return [{'url': url, 'markdown': result.markdown}]
113 |         else:
114 |             print(f"Failed to crawl {url}: {result.error_message}")
115 |             return []
116 | 
117 | def parse_sitemap(sitemap_url: str) -> List[str]:
118 |     resp = requests.get(sitemap_url)
119 |     urls = []
120 | 
121 |     if resp.status_code == 200:
122 |         try:
123 |             tree = ElementTree.fromstring(resp.content)
124 |             urls = [loc.text for loc in tree.findall('.//{*}loc')]
125 |         except Exception as e:
126 |             print(f"Error parsing sitemap XML: {e}")
127 | 
128 |     return urls
129 | 
130 | async def crawl_batch(urls: List[str], max_concurrent: int = 10) -> List[Dict[str,Any]]:
131 |     """Batch crawl using logic from 3-crawl_sitemap_in_parallel.py."""
132 |     browser_config = BrowserConfig(headless=True, verbose=False)
133 |     crawl_config = CrawlerRunConfig(cache_mode=CacheMode.BYPASS, stream=False)
134 |     dispatcher = MemoryAdaptiveDispatcher(
135 |         memory_threshold_percent=70.0,
136 |         check_interval=1.0,
137 |         max_session_permit=max_concurrent
138 |     )
139 | 
140 |     async with AsyncWebCrawler(config=browser_config) as crawler:
141 |         results = await crawler.arun_many(urls=urls, config=crawl_config, dispatcher=dispatcher)
142 |         return [{'url': r.url, 'markdown': r.markdown} for r in results if r.success and r.markdown]
143 | 
144 | def extract_section_info(chunk: str) -> Dict[str, Any]:
145 |     """Extracts headers and stats from a chunk."""
146 |     headers = re.findall(r'^(#+)\s+(.+)
#39;, chunk, re.MULTILINE)
147 |     header_str = '; '.join([f'{h[0]} {h[1]}' for h in headers]) if headers else ''
148 | 
149 |     return {
150 |         "headers": header_str,
151 |         "char_count": len(chunk),
152 |         "word_count": len(chunk.split())
153 |     }
154 | 
155 | def main():
156 |     parser = argparse.ArgumentParser(description="Insert crawled docs into ChromaDB")
157 |     parser.add_argument("url", help="URL to crawl (regular, .txt, or sitemap)")
158 |     parser.add_argument("--collection", default="docs", help="ChromaDB collection name")
159 |     parser.add_argument("--db-dir", default="./chroma_db", help="ChromaDB directory")
160 |     parser.add_argument("--embedding-model", default="all-MiniLM-L6-v2", help="Embedding model name")
161 |     parser.add_argument("--chunk-size", type=int, default=1000, help="Max chunk size (chars)")
162 |     parser.add_argument("--max-depth", type=int, default=3, help="Recursion depth for regular URLs")
163 |     parser.add_argument("--max-concurrent", type=int, default=10, help="Max parallel browser sessions")
164 |     parser.add_argument("--batch-size", type=int, default=100, help="ChromaDB insert batch size")
165 |     args = parser.parse_args()
166 | 
167 |     # Detect URL type
168 |     url = args.url
169 |     if is_txt(url):
170 |         print(f"Detected .txt/markdown file: {url}")
171 |         crawl_results = asyncio.run(crawl_markdown_file(url))
172 |     elif is_sitemap(url):
173 |         print(f"Detected sitemap: {url}")
174 |         sitemap_urls = parse_sitemap(url)
175 |         if not sitemap_urls:
176 |             print("No URLs found in sitemap.")
177 |             sys.exit(1)
178 |         crawl_results = asyncio.run(crawl_batch(sitemap_urls, max_concurrent=args.max_concurrent))
179 |     else:
180 |         print(f"Detected regular URL: {url}")
181 |         crawl_results = asyncio.run(crawl_recursive_internal_links([url], max_depth=args.max_depth, max_concurrent=args.max_concurrent))
182 | 
183 |     # Chunk and collect metadata
184 |     ids, documents, metadatas = [], [], []
185 |     chunk_idx = 0
186 |     for doc in crawl_results:
187 |         url = doc['url']
188 |         md = doc['markdown']
189 |         chunks = smart_chunk_markdown(md, max_len=args.chunk_size)
190 |         for chunk in chunks:
191 |             ids.append(f"chunk-{chunk_idx}")
192 |             documents.append(chunk)
193 |             meta = extract_section_info(chunk)
194 |             meta["chunk_index"] = chunk_idx
195 |             meta["source"] = url
196 |             metadatas.append(meta)
197 |             chunk_idx += 1
198 | 
199 |     if not documents:
200 |         print("No documents found to insert.")
201 |         sys.exit(1)
202 | 
203 |     print(f"Inserting {len(documents)} chunks into ChromaDB collection '{args.collection}'...")
204 | 
205 |     client = get_chroma_client(args.db_dir)
206 |     collection = get_or_create_collection(client, args.collection, embedding_model_name=args.embedding_model)
207 |     add_documents_to_collection(collection, ids, documents, metadatas, batch_size=args.batch_size)
208 | 
209 |     print(f"Successfully added {len(documents)} chunks to ChromaDB collection '{args.collection}'.")
210 | 
211 | if __name__ == "__main__":
212 |     main()
213 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/rag_agent.py:
--------------------------------------------------------------------------------
  1 | """Pydantic AI agent that leverages RAG with a local ChromaDB for Pydantic documentation."""
  2 | 
  3 | import os
  4 | import sys
  5 | import argparse
  6 | from dataclasses import dataclass
  7 | from typing import Optional
  8 | import asyncio
  9 | import chromadb
 10 | 
 11 | import dotenv
 12 | from pydantic_ai import RunContext
 13 | from pydantic_ai.agent import Agent
 14 | from openai import AsyncOpenAI
 15 | 
 16 | from utils import (
 17 |     get_chroma_client,
 18 |     get_or_create_collection,
 19 |     query_collection,
 20 |     format_results_as_context
 21 | )
 22 | 
 23 | # Load environment variables from .env file
 24 | dotenv.load_dotenv()
 25 | 
 26 | # Check for OpenAI API key
 27 | if not os.getenv("OPENAI_API_KEY"):
 28 |     print("Error: OPENAI_API_KEY environment variable not set.")
 29 |     print("Please create a .env file with your OpenAI API key or set it in your environment.")
 30 |     sys.exit(1)
 31 | 
 32 | 
 33 | @dataclass
 34 | class RAGDeps:
 35 |     """Dependencies for the RAG agent."""
 36 |     chroma_client: chromadb.PersistentClient
 37 |     collection_name: str
 38 |     embedding_model: str
 39 | 
 40 | 
 41 | # Create the RAG agent
 42 | agent = Agent(
 43 |     os.getenv("MODEL_CHOICE", "gpt-4.1-mini"),
 44 |     deps_type=RAGDeps,
 45 |     system_prompt="You are a helpful assistant that answers questions based on the provided documentation. "
 46 |                   "Use the retrieve tool to get relevant information from the documentation before answering. "
 47 |                   "If the documentation doesn't contain the answer, clearly state that the information isn't available "
 48 |                   "in the current documentation and provide your best general knowledge response."
 49 | )
 50 | 
 51 | 
 52 | @agent.tool
 53 | async def retrieve(context: RunContext[RAGDeps], search_query: str, n_results: int = 5) -> str:
 54 |     """Retrieve relevant documents from ChromaDB based on a search query.
 55 |     
 56 |     Args:
 57 |         context: The run context containing dependencies.
 58 |         search_query: The search query to find relevant documents.
 59 |         n_results: Number of results to return (default: 5).
 60 |         
 61 |     Returns:
 62 |         Formatted context information from the retrieved documents.
 63 |     """
 64 |     # Get ChromaDB client and collection
 65 |     collection = get_or_create_collection(
 66 |         context.deps.chroma_client,
 67 |         context.deps.collection_name,
 68 |         embedding_model_name=context.deps.embedding_model
 69 |     )
 70 |     
 71 |     # Query the collection
 72 |     query_results = query_collection(
 73 |         collection,
 74 |         search_query,
 75 |         n_results=n_results
 76 |     )
 77 |     
 78 |     # Format the results as context
 79 |     return format_results_as_context(query_results)
 80 | 
 81 | 
 82 | async def run_rag_agent(
 83 |     question: str,
 84 |     collection_name: str = "docs",
 85 |     db_directory: str = "./chroma_db",
 86 |     embedding_model: str = "all-MiniLM-L6-v2",
 87 |     n_results: int = 5
 88 | ) -> str:
 89 |     """Run the RAG agent to answer a question about Pydantic AI.
 90 |     
 91 |     Args:
 92 |         question: The question to answer.
 93 |         collection_name: Name of the ChromaDB collection to use.
 94 |         db_directory: Directory where ChromaDB data is stored.
 95 |         embedding_model: Name of the embedding model to use.
 96 |         n_results: Number of results to return from the retrieval.
 97 |         
 98 |     Returns:
 99 |         The agent's response.
100 |     """
101 |     # Create dependencies
102 |     deps = RAGDeps(
103 |         chroma_client=get_chroma_client(db_directory),
104 |         collection_name=collection_name,
105 |         embedding_model=embedding_model
106 |     )
107 |     
108 |     # Run the agent
109 |     result = await agent.run(question, deps=deps)
110 |     
111 |     return result.data
112 | 
113 | 
114 | def main():
115 |     """Main function to parse arguments and run the RAG agent."""
116 |     parser = argparse.ArgumentParser(description="Run a Pydantic AI agent with RAG using ChromaDB")
117 |     parser.add_argument("--question", help="The question to answer about Pydantic AI")
118 |     parser.add_argument("--collection", default="docs", help="Name of the ChromaDB collection")
119 |     parser.add_argument("--db-dir", default="./chroma_db", help="Directory where ChromaDB data is stored")
120 |     parser.add_argument("--embedding-model", default="all-MiniLM-L6-v2", help="Name of the embedding model to use")
121 |     parser.add_argument("--n-results", type=int, default=5, help="Number of results to return from the retrieval")
122 |     
123 |     args = parser.parse_args()
124 |     
125 |     # Run the agent
126 |     response = asyncio.run(run_rag_agent(
127 |         args.question,
128 |         collection_name=args.collection,
129 |         db_directory=args.db_dir,
130 |         embedding_model=args.embedding_model,
131 |         n_results=args.n_results
132 |     ))
133 |     
134 |     print("\nResponse:")
135 |     print(response)
136 | 
137 | 
138 | if __name__ == "__main__":
139 |     main()
140 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/requirements.txt:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/coleam00/ottomator-agents/main/crawl4AI-agent-v2/requirements.txt


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/streamlit_app.py:
--------------------------------------------------------------------------------
  1 | from dotenv import load_dotenv
  2 | import streamlit as st
  3 | import asyncio
  4 | import os
  5 | 
  6 | # Import all the message part classes
  7 | from pydantic_ai.messages import (
  8 |     ModelMessage,
  9 |     ModelRequest,
 10 |     ModelResponse,
 11 |     SystemPromptPart,
 12 |     UserPromptPart,
 13 |     TextPart,
 14 |     ToolCallPart,
 15 |     ToolReturnPart,
 16 |     RetryPromptPart,
 17 |     ModelMessagesTypeAdapter
 18 | )
 19 | 
 20 | from rag_agent import agent, RAGDeps
 21 | from utils import get_chroma_client
 22 | 
 23 | load_dotenv()
 24 | 
 25 | async def get_agent_deps():
 26 |     return RAGDeps(
 27 |         chroma_client=get_chroma_client("./chroma_db"),
 28 |         collection_name="docs",
 29 |         embedding_model="all-MiniLM-L6-v2"
 30 |     )
 31 | 
 32 | 
 33 | def display_message_part(part):
 34 |     """
 35 |     Display a single part of a message in the Streamlit UI.
 36 |     Customize how you display system prompts, user prompts,
 37 |     tool calls, tool returns, etc.
 38 |     """
 39 |     # user-prompt
 40 |     if part.part_kind == 'user-prompt':
 41 |         with st.chat_message("user"):
 42 |             st.markdown(part.content)
 43 |     # text
 44 |     elif part.part_kind == 'text':
 45 |         with st.chat_message("assistant"):
 46 |             st.markdown(part.content)             
 47 | 
 48 | async def run_agent_with_streaming(user_input):
 49 |     async with agent.run_stream(
 50 |         user_input, deps=st.session_state.agent_deps, message_history=st.session_state.messages
 51 |     ) as result:
 52 |         async for message in result.stream_text(delta=True):  
 53 |             yield message
 54 | 
 55 |     # Add the new messages to the chat history (including tool calls and responses)
 56 |     st.session_state.messages.extend(result.new_messages())
 57 | 
 58 | 
 59 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 60 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 61 | # ~~~~~~~~~~~~~~~~~~ Main Function with UI Creation ~~~~~~~~~~~~~~~~~~~~
 62 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 63 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 64 | 
 65 | async def main():
 66 |     st.title("ChromaDB Crawl4AI RAG AI Agent")
 67 | 
 68 |     # Initialize chat history in session state if not present
 69 |     if "messages" not in st.session_state:
 70 |         st.session_state.messages = []
 71 |     if "agent_deps" not in st.session_state:
 72 |         st.session_state.agent_deps = await get_agent_deps()  
 73 | 
 74 |     # Display all messages from the conversation so far
 75 |     # Each message is either a ModelRequest or ModelResponse.
 76 |     # We iterate over their parts to decide how to display them.
 77 |     for msg in st.session_state.messages:
 78 |         if isinstance(msg, ModelRequest) or isinstance(msg, ModelResponse):
 79 |             for part in msg.parts:
 80 |                 display_message_part(part)
 81 | 
 82 |     # Chat input for the user
 83 |     user_input = st.chat_input("What do you want to know?")
 84 | 
 85 |     if user_input:
 86 |         # Display user prompt in the UI
 87 |         with st.chat_message("user"):
 88 |             st.markdown(user_input)
 89 | 
 90 |         # Display the assistant's partial response while streaming
 91 |         with st.chat_message("assistant"):
 92 |             # Create a placeholder for the streaming text
 93 |             message_placeholder = st.empty()
 94 |             full_response = ""
 95 |             
 96 |             # Properly consume the async generator with async for
 97 |             generator = run_agent_with_streaming(user_input)
 98 |             async for message in generator:
 99 |                 full_response += message
100 |                 message_placeholder.markdown(full_response + "▌")
101 |             
102 |             # Final response without the cursor
103 |             message_placeholder.markdown(full_response)
104 | 
105 | 
106 | if __name__ == "__main__":
107 |     asyncio.run(main())
108 | 


--------------------------------------------------------------------------------
/crawl4AI-agent-v2/utils.py:
--------------------------------------------------------------------------------
  1 | """Utility functions for text processing and ChromaDB operations."""
  2 | 
  3 | import os
  4 | import pathlib
  5 | from typing import List, Dict, Any, Optional
  6 | 
  7 | import chromadb
  8 | from chromadb.utils import embedding_functions
  9 | from more_itertools import batched
 10 | 
 11 | 
 12 | def get_chroma_client(persist_directory: str) -> chromadb.PersistentClient:
 13 |     """Get a ChromaDB client with the specified persistence directory.
 14 |     
 15 |     Args:
 16 |         persist_directory: Directory where ChromaDB will store its data
 17 |         
 18 |     Returns:
 19 |         A ChromaDB PersistentClient
 20 |     """
 21 |     # Create the directory if it doesn't exist
 22 |     os.makedirs(persist_directory, exist_ok=True)
 23 |     
 24 |     # Return the client
 25 |     return chromadb.PersistentClient(persist_directory)
 26 | 
 27 | 
 28 | def get_or_create_collection(
 29 |     client: chromadb.PersistentClient,
 30 |     collection_name: str,
 31 |     embedding_model_name: str = "all-MiniLM-L6-v2",
 32 |     distance_function: str = "cosine",
 33 | ) -> chromadb.Collection:
 34 |     """Get an existing collection or create a new one if it doesn't exist.
 35 |     
 36 |     Args:
 37 |         client: ChromaDB client
 38 |         collection_name: Name of the collection
 39 |         embedding_model_name: Name of the embedding model to use
 40 |         distance_function: Distance function to use for similarity search
 41 |         
 42 |     Returns:
 43 |         A ChromaDB Collection
 44 |     """
 45 |     # Create embedding function
 46 |     embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
 47 |         model_name=embedding_model_name
 48 |     )
 49 |     
 50 |     # Try to get the collection, create it if it doesn't exist
 51 |     try:
 52 |         return client.get_collection(
 53 |             name=collection_name,
 54 |             embedding_function=embedding_func
 55 |         )
 56 |     except Exception:
 57 |         return client.create_collection(
 58 |             name=collection_name,
 59 |             embedding_function=embedding_func,
 60 |             metadata={"hnsw:space": distance_function}
 61 |         )
 62 | 
 63 | 
 64 | def add_documents_to_collection(
 65 |     collection: chromadb.Collection,
 66 |     ids: List[str],
 67 |     documents: List[str],
 68 |     metadatas: Optional[List[Dict[str, Any]]] = None,
 69 |     batch_size: int = 100,
 70 | ) -> None:
 71 |     """Add documents to a ChromaDB collection in batches.
 72 |     
 73 |     Args:
 74 |         collection: ChromaDB collection
 75 |         ids: List of document IDs
 76 |         documents: List of document texts
 77 |         metadatas: Optional list of metadata dictionaries for each document
 78 |         batch_size: Size of batches for adding documents
 79 |     """
 80 |     # Create default metadata if none provided
 81 |     if metadatas is None:
 82 |         metadatas = [{}] * len(documents)
 83 |     
 84 |     # Create document indices
 85 |     document_indices = list(range(len(documents)))
 86 |     
 87 |     # Add documents in batches
 88 |     for batch in batched(document_indices, batch_size):
 89 |         # Get the start and end indices for the current batch
 90 |         start_idx = batch[0]
 91 |         end_idx = batch[-1] + 1  # +1 because end_idx is exclusive
 92 |         
 93 |         # Add the batch to the collection
 94 |         collection.add(
 95 |             ids=ids[start_idx:end_idx],
 96 |             documents=documents[start_idx:end_idx],
 97 |             metadatas=metadatas[start_idx:end_idx],
 98 |         )
 99 | 
100 | 
101 | def query_collection(
102 |     collection: chromadb.Collection,
103 |     query_text: str,
104 |     n_results: int = 5,
105 |     where: Optional[Dict[str, Any]] = None,
106 | ) -> Dict[str, Any]:
107 |     """Query a ChromaDB collection for similar documents.
108 |     
109 |     Args:
110 |         collection: ChromaDB collection
111 |         query_text: Text to search for
112 |         n_results: Number of results to return
113 |         where: Optional filter to apply to the query
114 |         
115 |     Returns:
116 |         Query results containing documents, metadatas, distances, and ids
117 |     """
118 |     # Query the collection
119 |     return collection.query(
120 |         query_texts=[query_text],
121 |         n_results=n_results,
122 |         where=where,
123 |         include=["documents", "metadatas", "distances"]
124 |     )
125 | 
126 | 
127 | def format_results_as_context(query_results: Dict[str, Any]) -> str:
128 |     """Format query results as a context string for the agent.
129 |     
130 |     Args:
131 |         query_results: Results from a ChromaDB query
132 |         
133 |     Returns:
134 |         Formatted context string
135 |     """
136 |     context = "CONTEXT INFORMATION:\n\n"
137 |     
138 |     for i, (doc, metadata, distance) in enumerate(zip(
139 |         query_results["documents"][0],
140 |         query_results["metadatas"][0],
141 |         query_results["distances"][0]
142 |     )):
143 |         # Add document information
144 |         context += f"Document {i+1} (Relevance: {1 - distance:.2f}):\n"
145 |         
146 |         # Add metadata if available
147 |         if metadata:
148 |             for key, value in metadata.items():
149 |                 context += f"{key}: {value}\n"
150 |         
151 |         # Add document content
152 |         context += f"Content: {doc}\n\n"
153 |     
154 |     return context
155 | 


--------------------------------------------------------------------------------