# python/agents/knowledge_agent/prompts.py
from typing import List, Dict, Any

RAG_GENERATION_SYSTEM_PROMPT = """
You are a knowledgeable assistant that answers questions based ONLY on the provided context from a knowledge base.

Guidelines:
1. Answer questions using ONLY the information provided in the "Retrieved Context from Knowledge Base" section.
2. If the context doesn't contain enough information to answer the question, clearly state that you cannot find the relevant information in the provided documents.
3. When referencing information, you may mention the source if it helps provide context (e.g., "According to the documentation..." or "Based on the provided guide...").
4. Do not make up information or use knowledge outside of the provided context.
5. If multiple sources provide conflicting information, acknowledge this and present both perspectives.
6. Structure your answers clearly with proper formatting when appropriate (bullet points, numbered lists, etc.).
7. Be concise yet thorough. Avoid unnecessary verbosity.
8. If the query is a greeting or off-topic, respond politely and indicate you are designed to answer questions about the provided documents.
"""

def format_rag_prompt(query: str, context_chunks_with_metadata: List[Dict[str, Any]]) -> str:
    context_str = ""
    for i, chunk_data in enumerate(context_chunks_with_metadata):
        content = chunk_data.get("content", "")
        metadata = chunk_data.get("metadata", {})
        source = metadata.get("source_url", metadata.get("url", f"UnknownSource_{i+1}"))
        chunk_idx = metadata.get("chunk_index", "N/A")
        similarity = chunk_data.get("similarity", "N/A") # Assuming similarity is passed in chunk_data
        if isinstance(similarity, float): similarity = f"{similarity:.2f}"

        context_str += f"Context Chunk {i+1} (Source: {source}, Chunk Index: {chunk_idx}, Similarity: {similarity}):\n"
        context_str += f"{content}\n\n---\n\n"

    if not context_str:
        context_str = "No relevant context was found in the knowledge base for this query."

    prompt = f"""
User Query: "{query}"

Retrieved Context from Knowledge Base:
--- BEGIN CONTEXT ---
{context_str}
--- END CONTEXT ---

Based ONLY on the "Retrieved Context from Knowledge Base" provided above, answer the "User Query".
Adhere strictly to the system prompt guidelines.
Answer:
"""
    return prompt
