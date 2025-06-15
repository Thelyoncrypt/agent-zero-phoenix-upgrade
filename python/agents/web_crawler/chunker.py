# python/agents/web_crawler/chunker.py
from typing import List, Dict, Any

class HierarchicalChunker:
    """
    Chunks markdown content (mocked).
    """
    def __init__(self, chunk_size: int = 1000):
        self.chunk_size = chunk_size
        print(f"HierarchicalChunker (Mock) initialized with chunk_size: {chunk_size}")

    async def chunk_document(self, processed_doc: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Simulates chunking a processed document."""
        markdown_content = processed_doc.get("markdown", "")
        url = processed_doc.get("url", "unknown_url")
        print(f"HierarchicalChunker (Mock): Chunking document: {url}")
        
        if not markdown_content:
            return []

        # Simple mock chunking: split by self.chunk_size
        num_chunks = (len(markdown_content) + self.chunk_size - 1) // self.chunk_size
        chunks = []
        for i in range(num_chunks):
            chunk_text = markdown_content[i*self.chunk_size : (i+1)*self.chunk_size]
            chunks.append({
                "text": chunk_text,
                "metadata": {
                    "source_url": url,
                    "chunk_index": i,
                    "original_title": processed_doc.get("title"),
                    # In real Crawl4AI, headers would be extracted here
                    "headers": f"Mock Header for Chunk {i}" if i==0 else "" 
                }
            })
        return chunks