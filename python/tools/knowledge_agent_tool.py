# python/tools/knowledge_agent_tool.py
from python.helpers.tool import Tool, Response as ToolResponse
from typing import Dict, Any, List, Optional
import json

# Import StreamProtocol components if available
try:
    from python.tools.stream_protocol_tool import StreamEventType
    STREAM_PROTOCOL_AVAILABLE = True
except ImportError:
    STREAM_PROTOCOL_AVAILABLE = False
    StreamEventType = None

# Import knowledge agent components
from python.agents.knowledge_agent.agent import KnowledgeRAGAgent
from python.agents.knowledge_agent.database import DatabaseManager
from python.agents.knowledge_agent.embeddings import EmbeddingGenerator
from python.agents.knowledge_agent.retrieval import InformationRetriever

class KnowledgeAgentTool(Tool):
    """
    KnowledgeAgent (Foundational RAG inspired) integration for Agent Zero.
    Manages knowledge base ingestion and retrieval.
    """
    
    def __init__(self, agent, **kwargs):
        super().__init__(
            agent=agent,
            name="knowledge_agent_tool",
            description="Manages and queries a knowledge base using RAG principles.",
            args_schema={
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["ingest_chunks", "query", "raw_search", "list_sources"],
                        "description": "Type of knowledge operation to perform"
                    },
                    "chunks_data": {
                        "type": "array",
                        "items": {"type": "object"},
                        "description": "List of chunks to ingest (for ingest_chunks action)"
                    },
                    "query": {
                        "type": "string",
                        "description": "Search query or question (for query and raw_search actions)"
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of results to return (default: 5)"
                    },
                    "filter_metadata": {
                        "type": "object",
                        "description": "Metadata filters for search (for raw_search action)"
                    }
                },
                "required": ["action"]
            },
            **kwargs
        )
        # These components are now more functional
        self.db_manager = DatabaseManager() # Uses Supabase
        self.embed_generator = EmbeddingGenerator() # Uses OpenAI
        self.retriever = InformationRetriever(self.db_manager, self.embed_generator)

        # KnowledgeRAGAgent now also needs LLM client for generation
        self.rag_agent_logic = KnowledgeRAGAgent(
            database_manager=self.db_manager,
            information_retriever=self.retriever,
            # openai_api_key and llm_model_name will be picked from env by KnowledgeRAGAgent
        )
        print(f"KnowledgeAgentTool initialized for agent {agent.agent_name} with real RAG components.")

    async def _emit_knowledge_event(self, action_name: str, status: str, details: Optional[Dict[str, Any]] = None):
        event_type = StreamEventType.KNOWLEDGE_RESULT if status == "completed" else StreamEventType.PROGRESS_UPDATE
        payload = {"source_tool": "knowledge_agent", "action": action_name, "status": status}
        if details: payload.update(details)
        if hasattr(self.agent, '_emit_stream_event'):
             await self.agent._emit_stream_event(event_type, payload)
        else:
            print(f"KnowledgeAgentTool: Agent does not have _emit_stream_event. Cannot emit {event_type.value}.")

    async def execute(self, **kwargs) -> ToolResponse:
        """
        Execute KnowledgeAgent operations.
        
        Args:
            action (str): Knowledge operation (e.g., "ingest_chunks", "query", "raw_search", "list_sources").
            **kwargs: Arguments for the action.
        """
        action = kwargs.get("action")
        if not action:
            return ToolResponse(
                success=False,
                error="Missing required 'action' parameter",
                message="Error: 'action' is required for KnowledgeAgent operations."
            )

        try:
            if action == "ingest_chunks":
                chunks_data = kwargs.get("chunks_data")
                if not chunks_data:
                    return ToolResponse(
                        success=False,
                        error="Missing 'chunks_data' parameter",
                        message="Error: 'chunks_data' is required for ingest_chunks action."
                    )
                return await self._ingest_chunks(chunks_data)
            
            elif action == "query":
                query_text = kwargs.get("query")
                limit = kwargs.get("limit", 5)
                filter_metadata = kwargs.get("filter_metadata")
                if not query_text:
                    return ToolResponse(
                        success=False,
                        error="Missing 'query' parameter",
                        message="Error: 'query' is required for query action."
                    )
                return await self._query_kb(query_text, limit, filter_metadata)
            
            elif action == "raw_search": # Direct vector search without RAG response generation
                query_text = kwargs.get("query")
                limit = kwargs.get("limit", 5)
                filter_md = kwargs.get("filter_metadata")
                if not query_text:
                    return ToolResponse(
                        success=False,
                        error="Missing 'query' parameter",
                        message="Error: 'query' is required for raw_search action."
                    )
                return await self._raw_search(query_text, limit, filter_md)
            
            elif action == "list_sources":
                return await self._list_sources()
            else:
                return ToolResponse(
                    success=False,
                    error=f"Unknown action: {action}",
                    message=f"Unknown KnowledgeAgent action: {action}"
                )

        except Exception as e:
            import traceback
            error_message = f"KnowledgeAgentTool error during action '{action}': {str(e)}"
            print(f"{error_message}\\n{traceback.format_exc()}")
            await self._emit_knowledge_event(action, "error", {"error": str(e)})
            return ToolResponse(
                success=False,
                error=str(e),
                message=error_message
            )

    async def _ingest_chunks(self, chunks_data: List[Dict[str, Any]]) -> ToolResponse:
        """
        Ingests chunks. If embeddings are not provided, generates them.
        chunks_data: List of dicts, each like {"text": str, "metadata": Dict, "id": str}.
                     "embedding" (List[float]) is optional.
        """
        await self._emit_knowledge_event("ingest_chunks", "starting", {"chunk_count_received": len(chunks_data)})

        texts_to_embed = []
        indices_needing_embedding = []

        for i, chunk_d in enumerate(chunks_data):
            if "embedding" not in chunk_d or not chunk_d["embedding"]:
                text_to_embed = chunk_d.get("text")
                if not text_to_embed or not text_to_embed.strip():
                     err_msg = f"Chunk {i} (id: {chunk_d.get('id')}) has no text to embed."
                     await self._emit_knowledge_event("ingest_chunks", "error", {"message": err_msg})
                     # Skip this chunk or handle error more gracefully
                     print(f"KnowledgeAgentTool: {err_msg}")
                     continue
                texts_to_embed.append(text_to_embed)
                indices_needing_embedding.append(i)

        if texts_to_embed:
            print(f"KnowledgeAgentTool: Generating embeddings for {len(texts_to_embed)} chunks.")
            generated_embeddings = await self.embed_generator.generate_embeddings(texts_to_embed)
            if len(generated_embeddings) != len(indices_needing_embedding):
                msg = "Error: Mismatch in generated embeddings count."
                await self._emit_knowledge_event("ingest_chunks", "error", {"message": msg})
                return ToolResponse(success=False, message=msg, error=msg)

            for original_idx, embedding in zip(indices_needing_embedding, generated_embeddings):
                chunks_data[original_idx]["embedding"] = embedding

        # Filter out chunks that still lack embeddings (e.g., if text was empty and embedding failed)
        valid_chunks_data = [cd for cd in chunks_data if cd.get("embedding")]

        if not valid_chunks_data:
            msg = "No valid chunks with embeddings to ingest."
            await self._emit_knowledge_event("ingest_chunks", "error", {"message": msg})
            return ToolResponse(success=False, message=msg, error=msg)

        result = await self.rag_agent_logic.ingest_document_chunks(valid_chunks_data)

        await self._emit_knowledge_event("ingest_chunks", "completed", result)
        return ToolResponse(success=True, message=f"Ingested {result.get('count', 0)} chunks.", data=result)

    async def _query_kb(self, query: str, limit: int, filter_metadata: Optional[Dict] = None) -> ToolResponse: # Added filter_metadata
        await self._emit_knowledge_event("query_kb", "processing", {"query": query, "filter": filter_metadata})

        # Pass filter_metadata to the RAG logic
        rag_response_dict = await self.rag_agent_logic.query_knowledge_base(query, limit, filter_metadata)

        await self._emit_knowledge_event("query_kb", "completed", rag_response_dict)
        # The tool returns the structured dictionary from KnowledgeRAGAgent
        return ToolResponse(message=rag_response_dict["response"], data=rag_response_dict)

    async def _raw_search(self, query: str, limit: int, filter_metadata: Optional[Dict]) -> ToolResponse:
        await self._emit_knowledge_event("raw_search", "processing", {"query": query, "filter": filter_metadata})

        query_embedding = await self.embed_generator.generate_single_embedding(query)
        search_results = await self.db_manager.semantic_search(query_embedding, limit, filter_metadata)

        await self._emit_knowledge_event("raw_search", "completed", {"results_count": len(search_results)})
        return ToolResponse(success=True, message=json.dumps(search_results), data=search_results) # search_results is List[Dict]

    async def _list_sources(self) -> ToolResponse:
        await self._emit_knowledge_event("list_sources", "processing", {})
        sources = await self.db_manager.get_all_sources()
        await self._emit_knowledge_event("list_sources", "completed", {"sources": sources})
        return ToolResponse(success=True, message=json.dumps({"sources": sources}), data={"sources": sources})