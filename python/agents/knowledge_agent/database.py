# python/agents/knowledge_agent/database.py
from typing import List, Dict, Any, Optional

class DatabaseManager:
    """
    Manages interaction with the vector database (mocked).
    In a real implementation, this would interact with Supabase/pgvector.
    """
    def __init__(self):
        self.documents: List[Dict[str, Any]] = [] # In-memory store for mock
        print("DatabaseManager (Mock) initialized.")

    async def store_chunks(self, chunks_data: List[Dict[str, Any]]) -> List[str]:
        """Simulates storing chunks with their embeddings and metadata."""
        stored_ids = []
        for i, chunk_info in enumerate(chunks_data):
            # chunk_info expected to be like: {"text": str, "embedding": List[float], "metadata": Dict, "id": str}
            doc_id = chunk_info.get("id", f"mock_doc_{len(self.documents) + i}")
            self.documents.append({
                "id": doc_id,
                "content": chunk_info.get("text"),
                "embedding_vector": chunk_info.get("embedding"), # Store mock embedding
                "metadata": chunk_info.get("metadata", {})
            })
            stored_ids.append(doc_id)
            print(f"DatabaseManager (Mock): Stored chunk '{doc_id}': {chunk_info.get('text', '')[:50]}...")
        return stored_ids

    async def semantic_search(self, query_embedding: List[float], limit: int, filter_metadata: Optional[Dict] = None) -> List[Dict[str, Any]]:
        """Simulates semantic search."""
        print(f"DatabaseManager (Mock): Performing semantic search with limit {limit}, filter {filter_metadata}")
        # Mock search: return first few stored documents, ignoring embedding similarity for now
        results = []
        for doc in self.documents:
            if len(results) >= limit:
                break
            
            # Mock filtering
            passes_filter = True
            if filter_metadata:
                for key, value in filter_metadata.items():
                    if doc["metadata"].get(key) != value:
                        passes_filter = False
                        break
            
            if passes_filter:
                results.append({
                    "content": doc["content"],
                    "metadata": doc["metadata"],
                    "similarity_score": 0.85 + (0.1 * (len(results) % 2)) # Mock score
                })
        return results

    async def get_all_sources(self) -> List[str]:
        """Simulates fetching all unique source identifiers."""
        sources = set()
        for doc in self.documents:
            if doc["metadata"] and "source" in doc["metadata"]:
                sources.add(doc["metadata"]["source"])
        return list(sources)