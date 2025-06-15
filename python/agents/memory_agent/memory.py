# python/agents/memory_agent/memory.py
import asyncio
from typing import List, Dict, Any, Optional
import uuid
import os
import json
import pickle
import numpy as np
from pathlib import Path
from openai import OpenAI, APIError, RateLimitError
import logging

logger = logging.getLogger(__name__)

# Import the real mem0 library
try:
    from mem0 import Memory as Mem0Client
    MEM0_AVAILABLE = True
    logger.info("Mem0MemorySystem: mem0 library successfully imported.")
except ImportError:
    logger.warning("MemoryAgentTool: mem0 library not found. MemoryAgentTool will not be fully functional.")
    MEM0_AVAILABLE = False
    # Define a comprehensive placeholder if mem0 is not available to avoid crashing imports
    class Mem0Client: # type: ignore
        def __init__(self, *args, **kwargs):
            logger.info("Mem0Client (Placeholder): mem0 library not installed, using fallback implementation.")
        async def add(self, *args, **kwargs):
            return [{"id": str(uuid.uuid4()), "status": "placeholder_add", "message": "Memory added (placeholder)"}]
        async def search(self, *args, **kwargs):
            return [{"id": str(uuid.uuid4()), "text": "placeholder_search_result", "score": 0.0, "metadata":{}}]
        async def update(self, *args, **kwargs):
            return {"id": kwargs.get("memory_id"), "status": "placeholder_update", "message": "Memory updated (placeholder)"}
        async def delete(self, *args, **kwargs):
            return {"id": kwargs.get("memory_id"), "status": "placeholder_delete", "message": "Memory deleted (placeholder)"}
        async def get_all(self, *args, **kwargs):
            return [{"id": str(uuid.uuid4()), "text": "placeholder_all_memories", "metadata": {}}]
        # Enhanced mock graph methods
        async def add_kg_triplets(self, *args, **kwargs):
            return {"status": "success", "triplets_added": len(kwargs.get("triplets", [])), "message": "KG triplets added (placeholder)"}
        async def search_kg(self, *args, **kwargs):
            return [{"head": "mock_entity", "relation": "mock_rel", "tail": "mock_value", "score": 0.1, "metadata": {}}]

try:
    import networkx as nx
    NETWORKX_AVAILABLE = True
except ImportError:
    NETWORKX_AVAILABLE = False
    print("Mem0MemorySystem: networkx library not found. Graph memory simulation will be very basic.")

class Mem0MemorySystem:
    """
    Wrapper around the mem0.Memory client to provide an interface
    consistent with what MemoryAgentTool expects.
    """
    def __init__(self, agent_id: str = "default_agent_zero_user", config: Optional[Dict] = None,
                 persistence_dir: str = "memory/mem0_persistence"):
        self.agent_id = agent_id # Used as user_id for mem0 operations
        self.persistence_dir = Path(persistence_dir) / self.agent_id
        self.persistence_dir.mkdir(parents=True, exist_ok=True)

        self.vector_store_file = self.persistence_dir / "vector_store.json"
        self.graph_store_file_nx = self.persistence_dir / "graph_store.gpickle" # For networkx
        self.graph_store_file_list = self.persistence_dir / "graph_store_list.json" # For list fallback

        if not MEM0_AVAILABLE:
            logger.warning(f"Mem0MemorySystem: mem0 library not available. Operations will use placeholders for agent_id: {agent_id}")
            self._mem0_client = Mem0Client() # Placeholder instance
            self._llm_client_for_summary = None # No LLM if mem0 not available
            self.summary_llm_model = "placeholder"
        else:
            # Initialize mem0.Memory client with enhanced configuration
            # Default config for mem0 with OpenAI integration
            default_config = {
                "llm": {
                    "provider": "openai",
                    "config": {
                        "model": os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                        "temperature": 0.1,
                        "max_tokens": 1000
                    }
                },
                "embedder": {
                    "provider": "openai",
                    "config": {
                        "model": "text-embedding-3-small"
                    }
                }
            }

            # Merge with user-provided config
            effective_config = {**default_config, **(config or {})}

            try:
                self._mem0_client = Mem0Client(config=effective_config)
                logger.info(f"Mem0MemorySystem: Successfully initialized mem0.Memory client with config: {json.dumps(effective_config, indent=2)}")

                # Initialize separate OpenAI client for summarization
                openai_api_key = os.getenv("OPENAI_API_KEY")
                if openai_api_key:
                    self._llm_client_for_summary = OpenAI(api_key=openai_api_key)
                    self.summary_llm_model = os.getenv("OPENAI_MODEL_SUMMARY", "gpt-4o-mini")
                    logger.info(f"Mem0MemorySystem: Initialized LLM client for summarization with model: {self.summary_llm_model}")
                else:
                    self._llm_client_for_summary = None
                    self.summary_llm_model = "none"
                    logger.warning("Mem0MemorySystem: No OpenAI API key found, summarization features disabled.")

                logger.info(f"Mem0MemorySystem: Full initialization completed for agent_id: {self.agent_id}")
            except Exception as e:
                logger.error(f"Mem0MemorySystem: Error initializing mem0 client: {e}. Falling back to placeholder.", exc_info=True)
                self._mem0_client = Mem0Client() # Fallback to placeholder
                self._llm_client_for_summary = None
                self.summary_llm_model = "fallback"

        # No more local graph storage - using mem0 for everything
        logger.info(f"Mem0MemorySystem: Persistence enabled at {self.persistence_dir}")

    def _load_vector_store(self):
        if self.vector_store_file.exists():
            try:
                with open(self.vector_store_file, 'r') as f:
                    self.store = json.load(f)
                logger.info(f"Mem0MemorySystem: Loaded {len(self.store)} items from vector store file.")
            except Exception as e:
                logger.error(f"Mem0MemorySystem: Error loading vector store from {self.vector_store_file}: {e}. Starting fresh.", exc_info=True)
                self.store = {}

    def _save_vector_store(self):
        try:
            with open(self.vector_store_file, 'w') as f:
                json.dump(self.store, f, indent=2)
            # logger.debug(f"Mem0MemorySystem: Saved vector store to {self.vector_store_file}.")
        except Exception as e:
            logger.error(f"Mem0MemorySystem: Error saving vector store to {self.vector_store_file}: {e}", exc_info=True)

    def _load_graph_store(self):
        if NETWORKX_AVAILABLE and self.graph_store_file_nx.exists():
            try:
                with open(self.graph_store_file_nx, 'rb') as f:
                    self.graph_store = pickle.load(f)
                print(f"Mem0MemorySystem: Loaded graph store from {self.graph_store_file_nx}. Nodes: {len(self.graph_store.nodes)}, Edges: {len(self.graph_store.edges)}") # type: ignore
            except Exception as e:
                print(f"Mem0MemorySystem: Error loading graph store from {self.graph_store_file_nx}: {e}. Starting fresh graph.")
                self.graph_store = nx.MultiDiGraph()
        elif not NETWORKX_AVAILABLE and self.graph_store_file_list.exists():
            try:
                with open(self.graph_store_file_list, 'r') as f:
                    self.graph_store_list_fallback = json.load(f)
                print(f"Mem0MemorySystem: Loaded graph store (list fallback) from {self.graph_store_file_list}.")
            except Exception as e:
                print(f"Mem0MemorySystem: Error loading graph store (list fallback) from {self.graph_store_file_list}: {e}. Starting fresh list.")
                self.graph_store_list_fallback = []

    def _save_graph_store(self):
        if NETWORKX_AVAILABLE and self.graph_store is not None:
            try:
                with open(self.graph_store_file_nx, 'wb') as f:
                    pickle.dump(self.graph_store, f)
                # print(f"Mem0MemorySystem: Saved graph store to {self.graph_store_file_nx}.")
            except Exception as e:
                print(f"Mem0MemorySystem: Error saving graph store to {self.graph_store_file_nx}: {e}")
        elif not NETWORKX_AVAILABLE and self.graph_store_list_fallback is not None:
             try:
                with open(self.graph_store_file_list, 'w') as f:
                    json.dump(self.graph_store_list_fallback, f, indent=2)
                # print(f"Mem0MemorySystem: Saved graph store (list fallback) to {self.graph_store_file_list}.")
             except Exception as e:
                print(f"Mem0MemorySystem: Error saving graph store (list fallback): {e}")

    async def add_messages(self, messages: List[Dict[str, Any]], user_id_override: Optional[str] = None, max_retries: int = 3) -> List[str]:
        """Adds memories extracted by mem0 from a list of messages with enhanced error handling."""
        target_user_id = user_id_override or self.agent_id
        logger.info(f"Mem0MemorySystem: Adding memories from {len(messages)} messages for user '{target_user_id}'.")

        if not messages:
            logger.warning("Mem0MemorySystem: No messages provided for memory addition.")
            return []

        # Validate message format
        valid_messages = []
        for i, msg in enumerate(messages):
            if not isinstance(msg, dict) or not msg.get("content") and not msg.get("text"):
                logger.warning(f"Mem0MemorySystem: Skipping invalid message at index {i}: {msg}")
                continue
            valid_messages.append(msg)

        if not valid_messages:
            logger.error("Mem0MemorySystem: No valid messages found after validation.")
            return []

        for attempt in range(max_retries):
            try:
                # mem0's add method can take messages directly
                results = await self._mem0_client.add(
                    data=valid_messages,
                    user_id=target_user_id,
                    metadata={"source": "chat_messages", "timestamp": str(uuid.uuid4())}
                )

                if not results:
                    logger.warning("Mem0MemorySystem: mem0 returned empty results for add_messages.")
                    return []

                stored_ids = [res.get("id") for res in results if res and res.get("id")]
                logger.info(f"Mem0MemorySystem: Successfully processed {len(valid_messages)} messages, stored {len(stored_ids)} memories.")
                return stored_ids

            except Exception as e:
                wait_time = (2 ** attempt) + np.random.rand() # type: ignore
                logger.error(f"Mem0MemorySystem: Error during add_messages (attempt {attempt+1}/{max_retries}): {e}", exc_info=True)
                if attempt < max_retries - 1:
                    logger.info(f"Mem0MemorySystem: Retrying add_messages in {wait_time:.2f} seconds...")
                    await asyncio.sleep(wait_time)
                else:
                    logger.error("Mem0MemorySystem: All retry attempts failed for add_messages.")
        return []

    async def add_generic_memory(self, data: Any, memory_id: Optional[str] = None, user_id_override: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> str:
        """Adds a generic piece of data as memory using mem0."""
        target_user_id = user_id_override or self.agent_id
        print(f"Mem0MemorySystem: Adding generic memory data for user '{target_user_id}'. ID hint: {memory_id}")
        try:
            # mem0's add method can take a string or dict.
            # If memory_id is provided, mem0 might use it or ignore it depending on its backend.
            # We'll pass it in metadata for now if mem0 doesn't use it directly.
            effective_metadata = metadata or {}
            if memory_id and "original_id_hint" not in effective_metadata : # Avoid overwriting
                effective_metadata["original_id_hint"] = memory_id

            results = await self._mem0_client.add(data=str(data), user_id=target_user_id, metadata=effective_metadata) # Ensure data is string for simplicity
            stored_id = results[0].get("id") if results and results[0] else str(uuid.uuid4()) # Fallback id
            print(f"Mem0MemorySystem: Mem0 stored generic memory with ID: {stored_id}")
            return stored_id
        except Exception as e:
            print(f"Mem0MemorySystem: Error during add_generic_memory with mem0: {e}")
            return str(uuid.uuid4()) # Fallback ID on error

    async def search(self, query: str, user_id_override: Optional[str] = None, limit: int = 5, max_retries: int = 2) -> List[Dict[str, Any]]:
        """Enhanced search with validation and error handling."""
        target_user_id = user_id_override or self.agent_id

        if not query or not query.strip():
            logger.warning("Mem0MemorySystem: Empty query provided for search.")
            return []

        if limit <= 0:
            logger.warning(f"Mem0MemorySystem: Invalid limit {limit} for search, using default of 5.")
            limit = 5

        logger.info(f"Mem0MemorySystem: Searching memories with query '{query[:100]}...' for user '{target_user_id}', limit {limit}.")

        for attempt in range(max_retries):
            try:
                search_results = await self._mem0_client.search(
                    query=query.strip(),
                    user_id=target_user_id,
                    limit=limit
                )

                if not isinstance(search_results, list):
                    logger.error(f"Mem0MemorySystem: Unexpected search result type: {type(search_results)}")
                    return []

                # Validate and clean search results
                valid_results = []
                for result in search_results:
                    if isinstance(result, dict) and (result.get("text") or result.get("data")):
                        valid_results.append(result)
                    else:
                        logger.warning(f"Mem0MemorySystem: Skipping invalid search result: {result}")

                logger.info(f"Mem0MemorySystem: Search returned {len(valid_results)} valid results out of {len(search_results)} total.")
                return valid_results

            except Exception as e:
                wait_time = (2 ** attempt) + np.random.rand() # type: ignore
                logger.error(f"Mem0MemorySystem: Error during search (attempt {attempt+1}/{max_retries}): {e}", exc_info=True)
                if attempt < max_retries - 1:
                    logger.info(f"Mem0MemorySystem: Retrying search in {wait_time:.2f} seconds...")
                    await asyncio.sleep(wait_time)
                else:
                    logger.error("Mem0MemorySystem: All retry attempts failed for search.")
        return []

    async def update(self, memory_id: str, new_data: Any, user_id_override: Optional[str] = None, new_metadata: Optional[Dict] = None) -> bool:
        target_user_id = user_id_override or self.agent_id
        print(f"Mem0MemorySystem: Updating memory '{memory_id}' for user '{target_user_id}'.")
        try:
            # mem0 update might take data and/or metadata
            # For this task, we assume it takes 'data' and 'metadata' kwargs.
            result = await self._mem0_client.update(memory_id=memory_id, user_id=target_user_id, data=str(new_data), metadata=new_metadata)
            success = result.get("status") == "Memory updated successfully" # Example expected status
            print(f"Mem0MemorySystem: Mem0 update for '{memory_id}' status: {success}")
            return success
        except Exception as e:
            print(f"Mem0MemorySystem: Error during update with mem0: {e}")
            return False

    async def delete(self, memory_id: str, user_id_override: Optional[str] = None) -> bool:
        target_user_id = user_id_override or self.agent_id
        print(f"Mem0MemorySystem: Deleting memory '{memory_id}' for user '{target_user_id}'.")
        try:
            result = await self._mem0_client.delete(memory_id=memory_id, user_id=target_user_id)
            success = result.get("status") == "Memory deleted successfully" # Example expected status
            print(f"Mem0MemorySystem: Mem0 delete for '{memory_id}' status: {success}")
            return success
        except Exception as e:
            print(f"Mem0MemorySystem: Error during delete with mem0: {e}")
            return False

    async def get_all(self, user_id_override: Optional[str] = None) -> List[Dict[str, Any]]:
        target_user_id = user_id_override or self.agent_id
        print(f"Mem0MemorySystem: Getting all memories for user '{target_user_id}'.")
        try:
            # mem0 get_all might return a list of memory objects/dicts
            all_memories = await self._mem0_client.get_all(user_id=target_user_id)
            print(f"Mem0MemorySystem: Mem0 get_all returned {len(all_memories)} memories.")
            return all_memories
        except Exception as e:
            print(f"Mem0MemorySystem: Error during get_all with mem0: {e}")
            return []

    async def add_knowledge_graph_triplets(self, triplets: List[Dict[str, Any]], user_id_override: Optional[str] = None) -> Dict[str, Any]:
        """
        Adds knowledge graph triplets by converting them to textual statements and feeding them to mem0.
        Each triplet: {"head": str, "relation": str, "tail": str, "properties": Optional[Dict]}
        """
        target_user_id = user_id_override or self.agent_id
        logger.info(f"Mem0MemorySystem: Adding {len(triplets)} KG triplets as textual statements for user '{target_user_id}'.")

        if not MEM0_AVAILABLE:
            logger.warning("Mem0MemorySystem: mem0 not available, cannot add triplets.")
            return {"status": "error", "message": "Mem0 client not properly initialized.", "triplets_added": 0}

        texts_to_add = []
        metadata_list = []
        for triplet in triplets:
            head = triplet.get("head")
            relation = triplet.get("relation")
            tail = triplet.get("tail")
            props = triplet.get("properties", {})
            if head and relation and tail:
                # Convert triplet to a natural language statement
                statement = f"{head} {relation} {tail}."
                if props:
                    statement += f" Additional details: {json.dumps(props)}."
                texts_to_add.append(statement)
                metadata_list.append({"source_type": "kg_triplet_statement", "triplet_info": triplet, **props})

        if not texts_to_add:
            return {"status": "no_valid_triplets", "triplets_added": 0}

        try:
            # Use mem0's add method to store triplet statements
            results = []
            for i, text in enumerate(texts_to_add):
                metadata = metadata_list[i] if i < len(metadata_list) else {}
                result = await asyncio.to_thread(
                    self._mem0_client.add,
                    data=text,
                    user_id=target_user_id,
                    metadata=metadata
                )
                results.append(result)

            added_count = len([r for r in results if r and isinstance(r, (dict, list))])
            logger.info(f"Mem0MemorySystem: Added {added_count}/{len(texts_to_add)} KG triplet statements to mem0 for user '{target_user_id}'.")
            return {"status": "success" if added_count > 0 else "partial_failure", "triplets_added": added_count}
        except Exception as e:
            logger.error(f"Mem0MemorySystem: Error adding KG triplets as text to mem0: {e}", exc_info=True)
            return {"status": "error", "message": str(e), "triplets_added": 0}

    async def search_knowledge_graph(self, query_entity: Optional[str] = None,
                                     relation_type: Optional[str] = None,
                                     target_entity: Optional[str] = None,
                                     user_id_override: Optional[str] = None, limit: int = 10) -> List[Dict[str, Any]]:
        """
        Searches for graph-like information by formulating a natural language query for mem0's semantic search.
        Relies on mem0's ability to understand relational queries over its ingested text.
        """
        target_user_id = user_id_override or self.agent_id

        # Construct a natural language query from the graph components
        query_parts = []
        if query_entity: query_parts.append(f"information about '{query_entity}'")
        if relation_type: query_parts.append(f"and its '{relation_type}' relationships")
        if target_entity: query_parts.append(f"specifically concerning '{target_entity}'")

        if not query_parts:
            logger.warning("Mem0MemorySystem: search_knowledge_graph called with no query components.")
            return []

        nl_query = " ".join(query_parts)
        if query_entity and relation_type and target_entity: # Specific triplet query
            nl_query = f"Does '{query_entity}' have a '{relation_type}' relationship with '{target_entity}'? Provide details."
        elif query_entity and relation_type:
            nl_query = f"What are the '{relation_type}' relationships for '{query_entity}'?"
        elif query_entity:
            nl_query = f"Tell me about '{query_entity}' and its relationships."
        # Add more sophisticated query formations as needed.

        logger.info(f"Mem0MemorySystem: Searching KG via semantic search for user '{target_user_id}'. NL Query: '{nl_query}'")

        try:
            # Use the existing semantic search method
            search_results = await self.search(query=nl_query, user_id_override=target_user_id, limit=limit)
            # The results are text chunks. The LLM (in RAG or agent) would need to interpret these
            # to confirm if they represent the queried graph structure.
            # For now, we return these results as potentially relevant context.
            # We can add a "query_type": "graph_simulation" to metadata if needed.
            interpreted_graph_results = []
            for res in search_results:
                # This is a placeholder interpretation. Real graph extraction from text is complex.
                interpreted_graph_results.append({
                    "retrieved_text": res.get("text"),
                    "relevance_score": res.get("score"),
                    "source_metadata": res.get("metadata"),
                    "interpretation_hint": "This text may contain information about the queried graph relationship."
                })
            return interpreted_graph_results
        except Exception as e:
            logger.error(f"Mem0MemorySystem: Error during search_knowledge_graph (semantic query) via mem0: {e}", exc_info=True)
            return []

    async def summarize_memory_content(self, memory_id: Optional[str] = None,
                                     query_for_context: Optional[str] = None,
                                     user_id_override: Optional[str] = None,
                                     summary_instruction: Optional[str] = "Provide a concise summary.") -> Optional[str]:
        """
        Retrieves memory content and generates a summary.
        If mem0 has a native summarization API for a memory_id or query, it would be used here.
        Otherwise, it uses retrieved text and a general LLM call.
        """
        target_user_id = user_id_override or self.agent_id
        logger.info(f"Mem0MemorySystem: Summarizing memory for user '{target_user_id}'. ID: {memory_id}, Query: {query_for_context}")

        # --- Hypothetical check for native mem0 summarization ---
        # if MEM0_AVAILABLE and hasattr(self._mem0_client, "summarize"):
        #     try:
        #         logger.info(f"Mem0MemorySystem: Attempting native mem0 summarization.")
        #         mem0_summary_result = await self._mem0_client.summarize(
        #             memory_id=memory_id,
        #             query=query_for_context,
        #             user_id=target_user_id,
        #             instruction=summary_instruction # If mem0 supports it
        #         )
        #         if mem0_summary_result and mem0_summary_result.get("summary"):
        #             logger.info("Mem0MemorySystem: Successfully used native mem0 summarization.")
        #             return mem0_summary_result["summary"]
        #         else:
        #             logger.warning("Mem0MemorySystem: Native mem0 summarization did not return a summary. Falling back to custom.")
        #     except AttributeError: # Method doesn't exist
        #         logger.info("Mem0MemorySystem: Native mem0.summarize method not found. Using custom summarization.")
        #     except Exception as e:
        #         logger.warning(f"Mem0MemorySystem: Error with native mem0 summarization: {e}. Falling back to custom.")
        # --- End Hypothetical ---

        # Fallback to custom LLM summarization if native not available/failed, or if it's the primary strategy.
        if not self._llm_client_for_summary:
            logger.warning("Mem0MemorySystem: LLM client for custom summarization not available. Cannot summarize.")
            return "Summarization service (LLM client) not configured for this memory system."

        text_to_summarize = ""
        if memory_id:
            # Use mem0's get method if available, otherwise search by ID
            try:
                if hasattr(self._mem0_client, 'get'):
                    memory_item_dict = await asyncio.to_thread(self._mem0_client.get, memory_id=memory_id, user_id=target_user_id)
                else:
                    # Fallback: search all memories for the ID
                    all_memories = await self.get_all(user_id_override=target_user_id)
                    memory_item_dict = next((mem for mem in all_memories if mem.get("id") == memory_id), None)

                if memory_item_dict:
                    text_to_summarize = memory_item_dict.get("text", str(memory_item_dict))
                else:
                    return f"Memory with ID '{memory_id}' not found via mem0."
            except Exception as e:
                logger.error(f"Mem0MemorySystem: Error retrieving memory {memory_id}: {e}")
                return f"Error retrieving memory with ID '{memory_id}': {str(e)}"

        elif query_for_context:
            relevant_memories = await self.search(query=query_for_context, user_id_override=target_user_id, limit=3)
            if relevant_memories:
                text_to_summarize = "\n\n---\n\n".join([mem.get("text", "") for mem in relevant_memories if mem.get("text")])
            else:
                return "No relevant memories found via mem0 for the query to summarize."
        else:
            return "Either memory_id or query_for_context must be provided for summarization."

        if not text_to_summarize or not text_to_summarize.strip():
            return "No content found to summarize for the given criteria from mem0."

        max_summary_input_len = 8000 # Max input tokens for summary LLM (approx chars)
        if len(text_to_summarize) > max_summary_input_len:
            text_to_summarize = text_to_summarize[:max_summary_input_len] + "..."
            logger.info(f"Mem0MemorySystem: Truncated text for summarization to {max_summary_input_len} chars.")

        prompt = f"{summary_instruction}\n\nTEXT TO SUMMARIZE:\n\"\"\"\n{text_to_summarize}\n\"\"\"\n\nCONCISE SUMMARY:"
        messages = [
            {"role": "system", "content": "You are an expert at creating concise and informative summaries from provided text."},
            {"role": "user", "content": prompt}
        ]

        max_retries = 2
        for attempt in range(max_retries):
            try:
                response = await asyncio.to_thread(
                    self._llm_client_for_summary.chat.completions.create,
                    model=self.summary_llm_model,
                    messages=messages,
                    temperature=0.3,
                    max_tokens=200
                )

                if not response.choices or not response.choices[0].message.content:
                    logger.error("Mem0MemorySystem: Empty response from LLM for summarization.")
                    return "Unable to generate summary - empty LLM response."

                summary = response.choices[0].message.content.strip()
                logger.info(f"Mem0MemorySystem: Generated summary (length {len(summary)}): '{summary[:100]}...'")
                return summary

            except RateLimitError as rle:
                wait_time = (2 ** attempt) + np.random.rand() # type: ignore
                logger.warning(f"Mem0MemorySystem: Rate limit during summarization (attempt {attempt+1}/{max_retries}): {rle}")
                if attempt < max_retries - 1:
                    await asyncio.sleep(wait_time)
                else:
                    return "Summary generation rate limited. Please try again later."

            except APIError as apie:
                logger.error(f"Mem0MemorySystem: API error during summarization (attempt {attempt+1}/{max_retries}): {apie}", exc_info=True)
                if "context_length_exceeded" in str(apie).lower():
                    return "The content is too long to summarize. Please try with a shorter text."
                if attempt < max_retries - 1:
                    await asyncio.sleep((2 ** attempt) + np.random.rand()) # type: ignore
                else:
                    return f"Could not generate summary due to API error: {str(apie)}"

            except Exception as e:
                logger.error(f"Mem0MemorySystem: Unexpected error during summarization (attempt {attempt+1}/{max_retries}): {e}", exc_info=True)
                if attempt < max_retries - 1:
                    await asyncio.sleep((2 ** attempt) + np.random.rand()) # type: ignore
                else:
                    return f"Could not generate summary due to an unexpected error: {str(e)}"

        return "Unable to generate summary after multiple attempts."


# Legacy classes removed - now using Mem0MemorySystem directly