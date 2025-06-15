# python/agents/knowledge_agent/embeddings.py
from typing import List, Any

class EmbeddingGenerator:
    """
    Generates embeddings for text (mocked).
    In a real implementation, this would use OpenAI or other embedding models.
    """
    def __init__(self, model_name: str = "text-embedding-3-small"):
        self.model_name = model_name
        self.embedding_dim = 1536 # Default for text-embedding-3-small
        print(f"EmbeddingGenerator (Mock) initialized with model: {model_name}")

    async def generate_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Simulates generating embeddings for a batch of texts."""
        print(f"EmbeddingGenerator (Mock): Generating embeddings for {len(texts)} texts.")
        # Return mock embeddings (list of lists of floats)
        return [[0.01 * i + 0.001 * j for j in range(self.embedding_dim)] for i in range(len(texts))]

    async def generate_single_embedding(self, text: str) -> List[float]:
        """Simulates generating an embedding for a single text."""
        print(f"EmbeddingGenerator (Mock): Generating embedding for text: {text[:50]}...")
        return [0.01 * (len(text) % 100) + 0.001 * j for j in range(self.embedding_dim)]