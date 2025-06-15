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
        # Initialize components (these would be singletons or configured externally in a full app)
        self.db_manager = DatabaseManager()
        self.embed_generator = EmbeddingGenerator()
        self.retriever = InformationRetriever(self.db_manager, self.embed_generator)
        self.rag_agent_logic = KnowledgeRAGAgent(self.db_manager, self.retriever) # The core logic
        print(f"KnowledgeAgentTool initialized for agent {agent.agent_name} (context: {agent.context.id})")

    async def _emit_knowledge_event(self, action_name: str, status: str, details: Optional[Dict[str, Any]] = None):
        """Helper to emit KNOWLEDGE_RESULT or PROGRESS_UPDATE events."""
        if not STREAM_PROTOCOL_AVAILABLE:
            print(f"KnowledgeAgentTool: StreamProtocol not available, logging event: {action_name} - {status}")
            return
            
        event_type = StreamEventType.KNOWLEDGE_RESULT if status == "completed" else StreamEventType.PROGRESS_UPDATE
        payload = {"action": action_name, "status": status}
        if details:
            payload.update(details)
        
        if hasattr(self.agent, '_emit_stream_event'):
            await self.agent._emit_stream_event(event_type, payload)
        else:
            print(f"KnowledgeAgentTool: Agent does not have _emit_stream_event method. Cannot emit {event_type.value}.")

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
                if not query_text:
                    return ToolResponse(
                        success=False,
                        error="Missing 'query' parameter",
                        message="Error: 'query' is required for query action."
                    )
                return await self._query_kb(query_text, limit)
            
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
        """Ingests pre-processed and pre-embedded chunks."""
        await self._emit_knowledge_event("ingest_chunks", "starting", {"chunk_count": len(chunks_data)})
        
        # Embed if embeddings are not provided (or re-embed based on policy)
        for i, chunk_d in enumerate(chunks_data):
            if "embedding" not in chunk_d or not chunk_d["embedding"]:
                text_to_embed = chunk_d.get("text")
                if not text_to_embed:
                    await self._emit_knowledge_event("ingest_chunks", "error", {"message": f"Chunk {i} has no text to embed."})
                    return ToolResponse(
                        success=False,
                        error=f"Chunk {i} has no text for embedding",
                        message=f"Error: Chunk {i} has no text for embedding."
                    )
                chunks_data[i]["embedding"] = await self.embed_generator.generate_single_embedding(text_to_embed)

        result = await self.rag_agent_logic.ingest_document_chunks(chunks_data)
        
        await self._emit_knowledge_event("ingest_chunks", "completed", result)
        return ToolResponse(
            success=True,
            data=result,
            message=f"Ingested {result.get('count', 0)} chunks."
        )

    async def _query_kb(self, query: str, limit: int) -> ToolResponse:
        """Queries the KB and uses RAG to generate an answer."""
        await self._emit_knowledge_event("query_kb", "processing", {"query": query})
        
        rag_response = await self.rag_agent_logic.query_knowledge_base(query, limit)
        
        await self._emit_knowledge_event("query_kb", "completed", rag_response)
        # The main response text will be sent as TEXT_MESSAGE_CONTENT by the agent after this tool call.
        # This tool provides the structured RAG output.
        return ToolResponse(
            success=True,
            data=rag_response,
            message=json.dumps(rag_response)
        )

    async def _raw_search(self, query: str, limit: int, filter_metadata: Optional[Dict]) -> ToolResponse:
        """Performs a raw semantic search and returns document chunks."""
        await self._emit_knowledge_event("raw_search", "processing", {"query": query, "filter": filter_metadata})
        
        # In a real RAG system, InformationRetriever would be used
        # For this mock, we call db_manager directly after getting embedding
        query_embedding = await self.embed_generator.generate_single_embedding(query)
        search_results = await self.db_manager.semantic_search(query_embedding, limit, filter_metadata)
        
        await self._emit_knowledge_event("raw_search", "completed", {"results_count": len(search_results)})
        return ToolResponse(
            success=True,
            data={"results": search_results},
            message=json.dumps(search_results)
        )

    async def _list_sources(self) -> ToolResponse:
        """Lists all unique sources in the knowledge base."""
        await self._emit_knowledge_event("list_sources", "processing", {})
        sources = await self.db_manager.get_all_sources()
        sources_data = {"sources": sources}
        await self._emit_knowledge_event("list_sources", "completed", sources_data)
        return ToolResponse(
            success=True,
            data=sources_data,
            message=json.dumps(sources_data)
        )