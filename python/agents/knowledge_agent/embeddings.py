# python/agents/knowledge_agent/embeddings.py
import os
import time
import asyncio
import random
from typing import List, Optional
from openai import OpenAI, APIError, RateLimitError # Use new OpenAI client
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables from the project root .env file
project_root = Path(__file__).resolve().parents[2] # Adjusted to go up to project root
dotenv_path = project_root / '.env'
load_dotenv(dotenv_path, override=True)

class EmbeddingGenerator:
    """
    Generates embeddings for text using OpenAI API.
    """
    def __init__(self, model_name: Optional[str] = None, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model_name or os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

        if not self.api_key:
            raise ValueError("OpenAI API key must be provided via OPENAI_API_KEY environment variable or argument.")

        self.client = OpenAI(api_key=self.api_key)
        # Get embedding dimension dynamically if possible, or hardcode based on model
        # For "text-embedding-3-small", it's 1536. For "text-embedding-ada-002", it's also 1536.
        # For "text-embedding-3-large", it's 3072.
        # This is important if we allow model switching.
        if self.model == "text-embedding-3-large":
            self.embedding_dim = 3072
        else: # Default for ada-002 and 3-small
            self.embedding_dim = 1536
        print(f"EmbeddingGenerator: Initialized with OpenAI model '{self.model}', dimension {self.embedding_dim}.")

    def _create_zero_embedding(self) -> List[float]:
        return [0.0] * self.embedding_dim

    async def generate_single_embedding(self, text: str, max_retries: int = 3) -> List[float]:
        """Generates an embedding for a single text string with retry logic."""
        if not text or not text.strip():
            print("EmbeddingGenerator: Empty text provided, returning zero embedding.")
            return self._create_zero_embedding()

        # OpenAI's recommended replacement for newlines
        text = text.replace("\n", " ")

        # Max tokens for embedding models like text-embedding-ada-002 is 8191.
        # Truncate if necessary (though chunking should prevent overly long texts).
        # A simple character limit might be too naive due to tokenization differences.
        # For now, let's assume chunks are reasonably sized.

        for attempt in range(max_retries):
            try:
                response = await asyncio.to_thread(
                    self.client.embeddings.create, # Use asyncio.to_thread for sync SDK call
                    input=[text], # API expects a list of strings
                    model=self.model
                )
                return response.data[0].embedding
            except RateLimitError as rle:
                wait_time = (2 ** attempt) + random.random() # Exponential backoff
                print(f"EmbeddingGenerator: Rate limit hit (attempt {attempt+1}/{max_retries}). Retrying in {wait_time:.2f}s. Error: {rle}")
                await asyncio.sleep(wait_time)
            except APIError as apie:
                print(f"EmbeddingGenerator: OpenAI APIError (attempt {attempt+1}/{max_retries}): {apie}. Input text (first 100 chars): '{text[:100]}'")
                if "InvalidRequestError" in str(apie) and "maximum context length" in str(apie).lower():
                    print("Input text likely too long. Returning zero embedding.")
                    return self._create_zero_embedding() # Or handle by truncating text
                if attempt < max_retries - 1:
                     await asyncio.sleep((2 ** attempt) + random.random())
                else:
                    print("EmbeddingGenerator: All retry attempts failed due to APIError. Returning zero embedding.")
                    return self._create_zero_embedding()
            except Exception as e: # Catch other unexpected errors
                print(f"EmbeddingGenerator: Unexpected error (attempt {attempt+1}/{max_retries}): {e}. Input: '{text[:100]}'")
                if attempt < max_retries - 1:
                     await asyncio.sleep((2 ** attempt) + random.random())
                else:
                    print("EmbeddingGenerator: All retry attempts failed. Returning zero embedding.")
                    return self._create_zero_embedding()
        return self._create_zero_embedding() # Should be unreachable if max_retries > 0

    async def generate_embeddings(self, texts: List[str], batch_size: int = 20) -> List[List[float]]: # OpenAI batch limit often around 2048 items
        """Generates embeddings for a list of texts in batches."""
        if not texts:
            return []

        all_embeddings = []
        for i in range(0, len(texts), batch_size):
            batch_texts = texts[i:i+batch_size]
            batch_texts_processed = [text.replace("\n", " ") if text and text.strip() else " " for text in batch_texts] # Replace empty with space

            print(f"EmbeddingGenerator: Processing batch {i//batch_size + 1}/{(len(texts)-1)//batch_size + 1} with {len(batch_texts)} texts.")
            try:
                response = await asyncio.to_thread(
                    self.client.embeddings.create,
                    input=batch_texts_processed,
                    model=self.model
                )
                embeddings = [data.embedding for data in response.data]
                all_embeddings.extend(embeddings)
            except Exception as e:
                print(f"EmbeddingGenerator: Error embedding batch, processing individually. Error: {e}")
                # Fallback to individual processing for this batch on error
                for text in batch_texts: # Original batch_texts for individual processing
                    all_embeddings.append(await self.generate_single_embedding(text))
            await asyncio.sleep(0.1) # Small delay to respect potential rate limits even with batching

        return all_embeddings