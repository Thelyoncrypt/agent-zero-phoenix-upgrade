"""
HybridMemoryTool - Advanced Context Combination/Ranking with LLM-based Re-ranking/Synthesis

This tool combines results from multiple memory systems (Agent Zero structured memory and mem0 intelligent memory)
and uses an LLM to re-rank, select, and synthesize the most relevant information for a given query.
"""

import json
import asyncio
import logging
from typing import Dict, Any, List
from openai import OpenAI

from python.helpers.tool import Tool, Response as ToolResponse
from python.tools.memory_agent_tool import MemoryAgentTool

logger = logging.getLogger(__name__)

# StreamProtocol not needed for this advanced version

class HybridMemoryTool(Tool):
    """
    Advanced hybrid memory tool that combines multiple memory sources with LLM-based re-ranking and synthesis.
    """

    def __init__(self, agent_id: str = "default_agent", **kwargs):
        super().__init__(**kwargs)
        self.agent_id = agent_id

        # Initialize memory tools
        self.memory_agent_tool = MemoryAgentTool(agent_id=agent_id)

        # Initialize LLM client for re-ranking and synthesis
        self.llm_api_key = kwargs.get("llm_api_key") or self.get_env("OPENAI_API_KEY")
        self.llm_model = kwargs.get("llm_model", "gpt-4o-mini")
        self.llm_client = None

        if self.llm_api_key:
            try:
                self.llm_client = OpenAI(api_key=self.llm_api_key)
                logger.info(f"HybridMemoryTool: Initialized with LLM model '{self.llm_model}' for re-ranking and synthesis.")
            except Exception as e:
                logger.error(f"HybridMemoryTool: Failed to initialize LLM client: {e}")
        else:
            logger.warning("HybridMemoryTool: No OpenAI API key provided. LLM-based re-ranking will not be available.")

        # Load system prompt for re-ranking and synthesis
        try:
            with open("prompts/default/tool.hybrid_memory.rerank_synthesize.system.md", "r") as f:
                self.rerank_system_prompt = f.read()
        except Exception as e:
            logger.warning(f"HybridMemoryTool: Could not load system prompt: {e}. Using fallback.")
            self.rerank_system_prompt = "You are an expert at re-ranking and synthesizing information from multiple sources."

    @property
    def name(self) -> str:
        return "hybrid_memory"

    @property
    def args(self) -> Dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "enum": ["search_and_synthesize"],
                    "description": "Action to perform. Currently supports 'search_and_synthesize' which searches multiple memory sources and synthesizes results."
                },
                "query": {
                    "type": "string",
                    "description": "The search query to find relevant information across memory sources."
                },
                "user_id": {
                    "type": "string",
                    "description": "User ID for scoped memory operations (optional, defaults to agent_id)"
                },
                "max_chunks_per_source": {
                    "type": "integer",
                    "description": "Maximum number of chunks to retrieve from each memory source (default: 5)",
                    "default": 5
                },
                "top_n_final": {
                    "type": "integer",
                    "description": "Number of top chunks to select after LLM re-ranking (default: 3)",
                    "default": 3
                },
                "enable_synthesis": {
                    "type": "boolean",
                    "description": "Whether to synthesize the selected chunks into a coherent context (default: true)",
                    "default": True
                }
            },
            "required": ["action", "query"]
        }

    async def execute(self, **kwargs) -> ToolResponse:
        """Execute the hybrid memory tool action."""
        action = kwargs.get("action")

        if action == "search_and_synthesize":
            return await self._search_and_synthesize(**kwargs)
        else:
            return ToolResponse(
                success=False,
                message=f"Unknown action: {action}",
                error="Invalid action specified"
            )

    async def _search_and_synthesize(self, **kwargs) -> ToolResponse:
        """
        Search multiple memory sources, re-rank with LLM, and synthesize results.
        """
        query = kwargs.get("query")
        user_id = kwargs.get("user_id", self.agent_id)
        max_chunks_per_source = kwargs.get("max_chunks_per_source", 5)
        top_n_final = kwargs.get("top_n_final", 3)
        enable_synthesis = kwargs.get("enable_synthesis", True)

        if not query:
            return ToolResponse(success=False, message="Query is required", error="Missing query parameter")

        logger.info(f"HybridMemoryTool: Searching and synthesizing for query: '{query}' (user: {user_id})")

        # Step 1: Search multiple memory sources
        all_chunks = []

        # Search Agent Zero structured memory
        try:
            az_response = await self.memory_agent_tool.execute(
                action="search",
                query=query,
                user_id=user_id,
                limit=max_chunks_per_source
            )
            if az_response.success and az_response.data:
                memories = az_response.data.get("memories", [])
                for memory in memories:
                    all_chunks.append({
                        "original_id": memory.get("id", "unknown"),
                        "source_type": "agent_zero_structured",
                        "content": memory.get("text", str(memory.get("data", ""))),
                        "initial_score": memory.get("score", 0.5),
                        "metadata": memory.get("metadata", {})
                    })
                logger.info(f"HybridMemoryTool: Retrieved {len(memories)} chunks from Agent Zero structured memory.")
        except Exception as e:
            logger.error(f"HybridMemoryTool: Error searching Agent Zero memory: {e}")

        # Search mem0 intelligent memory
        try:
            mem0_response = await self.memory_agent_tool.execute(
                action="search",
                query=query,
                user_id=user_id,
                limit=max_chunks_per_source
            )
            if mem0_response.success and mem0_response.data:
                memories = mem0_response.data.get("memories", [])
                for memory in memories:
                    all_chunks.append({
                        "original_id": memory.get("id", "unknown"),
                        "source_type": "mem0_intelligent",
                        "content": memory.get("text", str(memory.get("data", ""))),
                        "initial_score": memory.get("score", 0.5),
                        "metadata": memory.get("metadata", {})
                    })
                logger.info(f"HybridMemoryTool: Retrieved {len(memories)} chunks from mem0 intelligent memory.")
        except Exception as e:
            logger.error(f"HybridMemoryTool: Error searching mem0 memory: {e}")

        if not all_chunks:
            return ToolResponse(
                success=True,
                message="No relevant information found in any memory source.",
                data={"synthesized_context": None, "selected_chunks": [], "total_chunks_found": 0}
            )

        logger.info(f"HybridMemoryTool: Total chunks retrieved from all sources: {len(all_chunks)}")

        # Step 2: LLM-based re-ranking and synthesis
        if not self.llm_client:
            # Fallback: simple score-based ranking without LLM
            logger.warning("HybridMemoryTool: LLM client not available. Using simple score-based ranking.")
            sorted_chunks = sorted(all_chunks, key=lambda x: x.get("initial_score", 0), reverse=True)
            selected_chunks = sorted_chunks[:top_n_final]
            synthesized_context = "Multiple memory sources found relevant information, but LLM synthesis is not available."
            overall_confidence = 0.3
        else:
            try:
                llm_result = await self._llm_rerank_and_synthesize(query, all_chunks, top_n_final, enable_synthesis)
                selected_chunks = llm_result.get("ranked_and_selected_chunks", [])
                synthesized_context = llm_result.get("synthesized_context", "")
                overall_confidence = llm_result.get("overall_confidence_in_context", 0.5)
            except Exception as e:
                logger.error(f"HybridMemoryTool: Error during LLM re-ranking: {e}")
                # Fallback to simple ranking
                sorted_chunks = sorted(all_chunks, key=lambda x: x.get("initial_score", 0), reverse=True)
                selected_chunks = sorted_chunks[:top_n_final]
                synthesized_context = f"LLM synthesis failed ({str(e)}), but found relevant information from multiple sources."
                overall_confidence = 0.3

        result_data = {
            "query": query,
            "synthesized_context": synthesized_context,
            "ranked_and_selected_chunks": selected_chunks,  # Match UI expectation
            "total_chunks_found": len(all_chunks),
            "sources_searched": ["agent_zero_structured", "mem0_intelligent"],
            "overall_confidence_in_context": overall_confidence  # Match UI expectation
        }

        success_message = f"Found and synthesized information from {len(all_chunks)} total chunks across multiple memory sources."
        if selected_chunks:
            success_message += f" Selected top {len(selected_chunks)} most relevant chunks."

        return ToolResponse(
            success=True,
            message=success_message,
            data=result_data
        )

    async def _llm_rerank_and_synthesize(self, query: str, chunks: List[Dict[str, Any]],
                                       top_n: int, enable_synthesis: bool) -> Dict[str, Any]:
        """Use LLM to re-rank chunks and optionally synthesize them."""

        # Prepare chunks for LLM
        chunks_for_llm = []
        for i, chunk in enumerate(chunks):
            chunks_for_llm.append({
                "id": i,
                "original_id": chunk.get("original_id"),
                "source_type": chunk.get("source_type"),
                "content": chunk.get("content", "")[:1000],  # Truncate very long content
                "initial_score": chunk.get("initial_score", 0.5)
            })

        user_prompt = f"""
User Query: "{query}"

Retrieved Chunks:
{json.dumps(chunks_for_llm, indent=2)}

Please re-rank these chunks, select the top {top_n} most relevant ones, and {'synthesize them into a coherent context' if enable_synthesis else 'list the key information'}.
"""

        messages = [
            {"role": "system", "content": self.rerank_system_prompt},
            {"role": "user", "content": user_prompt}
        ]

        # Retry logic for LLM call
        max_retries = 3
        retry_delay = 1

        for attempt in range(max_retries):
            try:
                response = await asyncio.to_thread(
                    self.llm_client.chat.completions.create,
                    model=self.llm_model,
                    messages=messages,
                    temperature=0.3,
                    max_tokens=1500
                )
                response_content = response.choices[0].message.content.strip()
                break
            except Exception as e:
                if attempt < max_retries - 1:
                    logger.warning(f"HybridMemoryTool: LLM call attempt {attempt + 1} failed: {e}. Retrying in {retry_delay}s...")
                    await asyncio.sleep(retry_delay)
                    retry_delay *= 2  # Exponential backoff
                else:
                    logger.error(f"HybridMemoryTool: All {max_retries} LLM call attempts failed: {e}")
                    raise

        try:
            # Parse JSON response
            llm_result = json.loads(response_content)

            # Validate crucial keys
            required_keys = ["ranked_and_selected_chunks", "synthesized_context"]
            missing_keys = [key for key in required_keys if key not in llm_result]
            if missing_keys:
                raise ValueError(f"LLM response missing required keys: {missing_keys}")

            # Map back to original chunks with full content
            final_selected_chunks = []
            for selected in llm_result.get("ranked_and_selected_chunks", []):
                chunk_id = selected.get("original_id")
                original_chunk = next((c for c in chunks if c.get("original_id") == chunk_id), None)
                if original_chunk:
                    final_selected_chunks.append({
                        **original_chunk,
                        "llm_relevance_score": selected.get("llm_relevance_score", 0.5),
                        "reason_for_selection": selected.get("reason_for_selection", "")
                    })

            llm_result["ranked_and_selected_chunks"] = final_selected_chunks
            return llm_result

        except (json.JSONDecodeError, ValueError) as e:
            error_msg = f"HybridMemory: Synthesis LLM returned invalid or incomplete JSON: {e}. Raw: {response_content[:500]}"
            logger.error(error_msg)

            # Fallback strategy: return top N raw chunks without synthesis
            logger.info("HybridMemoryTool: Falling back to simple score-based ranking due to LLM synthesis failure.")
            sorted_chunks = sorted(chunks, key=lambda x: x.get("initial_score", 0), reverse=True)
            fallback_chunks = sorted_chunks[:top_n]

            return {
                "ranked_and_selected_chunks": fallback_chunks,
                "synthesized_context": f"LLM synthesis failed ({str(e)}). Here are the top {len(fallback_chunks)} chunks based on initial relevance scores.",
                "overall_confidence_in_context": 0.3,
                "error": error_msg,
                "raw_llm_output": response_content,
                "user_query": query
            }