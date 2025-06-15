# python/agents/knowledge_agent/agent.py
import os
import json
import numpy as np
from typing import List, Dict, Any, Optional
from openai import OpenAI, APIError, RateLimitError # For direct LLM calls
import asyncio
from dotenv import load_dotenv
from pathlib import Path
import logging

logger = logging.getLogger(__name__)

# Assuming these are correctly pathed for your project structure
from .database import DatabaseManager
from .embeddings import EmbeddingGenerator # We still need this for the retriever
from .retrieval import InformationRetriever
from .prompts import RAG_GENERATION_SYSTEM_PROMPT, format_rag_prompt

# Load environment variables
project_root = Path(__file__).resolve().parents[2]
dotenv_path = project_root / '.env'
load_dotenv(dotenv_path, override=True)

class KnowledgeRAGAgent:
    """
    RAG Agent logic, now with LLM-based answer generation.
    """
    def __init__(self,
                 database_manager: Optional[DatabaseManager] = None,
                 information_retriever: Optional[InformationRetriever] = None,
                 embedding_generator: Optional[EmbeddingGenerator] = None,
                 openai_api_key: Optional[str] = None,
                 llm_model_name: Optional[str] = None,
                 rag_llm_model_name: Optional[str] = None # Specific model for RAG generation
                ):

        self.db_manager = database_manager or DatabaseManager() # Uses Supabase
        self.embed_generator = embedding_generator or EmbeddingGenerator()
        self.retriever = information_retriever or InformationRetriever(self.db_manager, self.embed_generator)

        self.api_key = openai_api_key or os.getenv("OPENAI_API_KEY")
        # Use RAG_LLM_MODEL from .env for this specific task, fallback to OPENAI_MODEL
        self.rag_llm_model = rag_llm_model_name or os.getenv("RAG_LLM_MODEL", os.getenv("OPENAI_MODEL", "gpt-4o-mini"))

        if not self.api_key:
            raise ValueError("OpenAI API key is required for KnowledgeRAGAgent LLM generation.")

        self.llm_client = OpenAI(api_key=self.api_key)
        logger.info(f"KnowledgeRAGAgent: Initialized with RAG LLM '{self.rag_llm_model}'.")

    async def ingest_document_chunks(self, chunks_data: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Ingests pre-processed chunks. Assumes chunks_data items have:
        "id" (client-side unique ID for this batch of chunks),
        "text",
        "embedding" (List[float]),
        "metadata" (which MUST include "source_url" and "chunk_index" for the DB table)
        """
        logger.info(f"KnowledgeRAGAgent: Ingesting {len(chunks_data)} chunks via real DatabaseManager.")

        # Validate chunks_data structure for required metadata by DatabaseManager
        valid_chunks_for_db = []
        for i, chunk_d in enumerate(chunks_data):
            if not chunk_d.get("metadata") or \
               "source_url" not in chunk_d["metadata"] or \
               "chunk_index" not in chunk_d["metadata"]:
                logger.warning(f"Skipping chunk {i} (ID: {chunk_d.get('id')}) due to missing source_url or chunk_index in metadata.")
                continue
            if not chunk_d.get("text") or not chunk_d.get("embedding"):
                logger.warning(f"Skipping chunk {i} (ID: {chunk_d.get('id')}) due to missing text or embedding.")
                continue
            valid_chunks_for_db.append(chunk_d)

        if not valid_chunks_for_db:
            return {"status": "error", "message": "No valid chunks provided for ingestion.", "count": 0}

        stored_db_ids = await self.db_manager.store_chunks(valid_chunks_for_db)
        return {"status": "success", "ingested_supabase_ids": stored_db_ids, "count": len(stored_db_ids)}

    async def _generate_answer_from_context(self, query: str, retrieved_docs_with_metadata: List[Dict[str, Any]]) -> str:
        """Generates an answer using an LLM based on the query and retrieved document context."""

        if not retrieved_docs_with_metadata:
            logger.info("KnowledgeRAGAgent: No context retrieved, LLM will be prompted to answer from general knowledge or state inability.")
            # If no docs, system prompt guides LLM to say it couldn't find info in docs.
            # We can provide a simpler prompt or just the query.
            formatted_prompt = query # Or a specific prompt like "Answer based on general knowledge: {query}"
            messages = [
                {"role": "system", "content": RAG_GENERATION_SYSTEM_PROMPT}, # System prompt is key here
                {"role": "user", "content": f"User Query: \"{query}\"\n\nRetrieved Context from Knowledge Base:\n--- BEGIN CONTEXT ---\nNo relevant context was found in the knowledge base for this query.\n--- END CONTEXT ---\n\nBased ONLY on the \"Retrieved Context from Knowledge Base\" provided above, answer the \"User Query\".\nAnswer:"}
            ]
        else:
            # Pass the full doc dicts to format_rag_prompt so it can include metadata like source and similarity
            formatted_prompt = format_rag_prompt(query, retrieved_docs_with_metadata)
            messages = [
                {"role": "system", "content": RAG_GENERATION_SYSTEM_PROMPT},
                {"role": "user", "content": formatted_prompt}
            ]

        logger.debug(f"KnowledgeRAGAgent: LLM messages for RAG:\n{json.dumps(messages, indent=2)[:1000]}...") # Log truncated prompt

        max_retries = 2; answer = "I am currently unable to generate an answer."
        for attempt in range(max_retries + 1):
            try:
                completion = await asyncio.to_thread(
                    self.llm_client.chat.completions.create,
                    model=self.rag_llm_model,
                    messages=messages,
                    temperature=0.2, # Lower temp for more factual, less creative RAG answers
                    max_tokens=800  # Max length of the generated answer
                )
                answer = completion.choices[0].message.content.strip()
                logger.info(f"KnowledgeRAGAgent: LLM generated answer (length {len(answer)}): '{answer[:150]}...'")
                return answer
            except RateLimitError as rle:
                wait_time = (2 ** attempt) + np.random.rand() # type: ignore
                logger.warning(f"KnowledgeRAGAgent (LLM): Rate limit (attempt {attempt+1}/{max_retries+1}). Retrying in {wait_time:.2f}s. Error: {rle}")
                if attempt < max_retries: await asyncio.sleep(wait_time)
                else: answer = "I'm experiencing high demand. Please try again shortly."
            except APIError as apie: # Includes BadRequestError for context length issues
                logger.error(f"KnowledgeRAGAgent (LLM): APIError (attempt {attempt+1}/{max_retries+1}): {apie}. Query: '{query[:50]}...'", exc_info=True)
                if "context_length_exceeded" in str(apie).lower():
                    answer = "The information needed to answer your query is too extensive for me to process at once. Could you try a more specific question?"
                    break # No point retrying context length errors
                if attempt < max_retries: await asyncio.sleep((2 ** attempt) + np.random.rand()) # type: ignore
                else: answer = "I apologize, but I encountered an API issue while generating an answer."
            except Exception as e:
                logger.error(f"KnowledgeRAGAgent (LLM): Unexpected error (attempt {attempt+1}/{max_retries+1}): {e}. Query: '{query[:50]}...'", exc_info=True)
                if attempt < max_retries: await asyncio.sleep((2 ** attempt) + np.random.rand()) # type: ignore
                else: answer = "I am sorry, I couldn't process your request to generate an answer at this time."
        return answer

    async def query_knowledge_base(self, query: str, limit: int = 5, filter_metadata: Optional[Dict] = None) -> Dict[str, Any]:
        logger.info(f"KnowledgeRAGAgent: Received query: '{query}', limit: {limit}, filter: {filter_metadata}")

        # Step 1: Retrieve documents from DB (this is now real Supabase call)
        # retrieved_docs_from_db is List[Dict[str, Any]] where each dict has 'id', 'content', 'metadata', 'similarity'
        retrieved_docs_from_db = await self.retriever.retrieve_documents(query, limit, filter_metadata)

        context_contents_for_llm: List[str] = []
        sources_for_ui_response: List[Dict[str, Any]] = []

        if retrieved_docs_from_db:
            logger.info(f"KnowledgeRAGAgent: Retrieved {len(retrieved_docs_from_db)} documents from DB for query '{query}'.")
            for doc in retrieved_docs_from_db:
                # The format_rag_prompt expects a list of dicts, where each dict has 'content' and 'metadata'
                # and 'metadata' ideally has 'source_url' and 'chunk_index', and 'similarity' is at top level of doc dict.
                context_item_for_prompt = {
                    "content": doc.get("content", ""),
                    "metadata": doc.get("metadata", {}),
                    "similarity": doc.get("similarity", 0.0) # Pass similarity to prompt formatter
                }
                # For LLM, we pass the full retrieved doc structure to format_rag_prompt
                # context_chunks_for_llm.append(doc.get("content", "")) # Old way, now pass full doc

                sources_for_ui_response.append({
                    "id": doc.get("id"),
                    "source": doc.get("metadata", {}).get("source_url", doc.get("url", "Unknown")),
                    "content_preview": doc.get("content", "")[:150]+"...", # Keep preview short
                    "similarity": doc.get("similarity", 0.0),
                    "metadata": doc.get("metadata", {})
                })
        else:
            logger.info(f"KnowledgeRAGAgent: No documents retrieved from DB for query '{query}'.")

        # Step 2: Generate the answer using the LLM with retrieved_docs_from_db (which includes metadata)
        llm_generated_answer = await self._generate_answer_from_context(query, retrieved_docs_from_db) # Pass full list of dicts

        return {
            "response": llm_generated_answer,
            "sources": sources_for_ui_response, # This is for UI display
            "retrieved_count": len(retrieved_docs_from_db)
        }