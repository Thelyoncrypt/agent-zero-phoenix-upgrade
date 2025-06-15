# python/agents/web_crawler/chunker.py
import re
from typing import List, Dict, Any

class HierarchicalChunker:
    """
    Chunks markdown content hierarchically by headers, then by max length.
    """
    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 0): # Overlap less critical for header-based
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap # Not used in this hierarchical version yet, but kept for compatibility
        print(f"HierarchicalChunker: Initialized with chunk_size: {chunk_size}")

    def _split_by_header_level(self, markdown_text: str, header_prefix: str) -> List[str]:
        """Splits text by a specific markdown header level (e.g., '# ', '## ')."""
        # Regex to find headers, ensuring they are at the beginning of a line
        parts = re.split(fr"(^{re.escape(header_prefix)}.+)$", markdown_text, flags=re.MULTILINE)
        chunks = []
        current_header = ""
        for i, part in enumerate(parts):
            if re.match(fr"^{re.escape(header_prefix)}.+", part):
                current_header = part.strip()
            elif part.strip(): # This is content under the current_header or before any header
                if current_header: # Content associated with a header
                    chunks.append(f"{current_header}\n{part.strip()}")
                elif not chunks: # Content before the first header of this level
                    chunks.append(part.strip())
                else: # Content likely orphaned, append to previous chunk if small enough
                    if chunks and len(chunks[-1]) + len(part) < self.chunk_size * 1.5 : # Allow some leeway
                         chunks[-1] += f"\n{part.strip()}"
                    else:
                         chunks.append(part.strip())

        # If no headers of this level were found, return the original text as one chunk
        return chunks if chunks else [markdown_text.strip()]


    def _split_by_char_limit(self, text_segment: str) -> List[str]:
        """Splits a text segment by character limit if it's too long."""
        if len(text_segment) <= self.chunk_size:
            return [text_segment]

        # Simple character-based splitting with overlap (can be improved with sentence awareness)
        # For now, direct split similar to TextChunker in foundational-rag-agent
        split_chunks = []
        start = 0
        while start < len(text_segment):
            end = start + self.chunk_size
            split_chunks.append(text_segment[start:end])
            start += self.chunk_size - self.chunk_overlap # Apply overlap here if desired
            if start >= len(text_segment) and end < len(text_segment) : # Ensure last part is captured
                if text_segment[start:].strip(): split_chunks.append(text_segment[start:])
            elif end >= len(text_segment): # If end already reached or passed length
                break
        return [c.strip() for c in split_chunks if c.strip()]


    async def chunk_document(self, processed_doc: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Chunks a processed document's markdown content.
        processed_doc: dict with "url", "title", "markdown", "metadata"
        """
        markdown_content = processed_doc.get("markdown", "")
        source_url = processed_doc.get("url", "unknown_source")
        doc_title = processed_doc.get("title", "Untitled Document")
        base_metadata = processed_doc.get("metadata", {}) # e.g., {"original_url": ..., "crawl_depth": ...}

        print(f"HierarchicalChunker: Chunking document from {source_url} (Title: {doc_title})")

        if not markdown_content or not markdown_content.strip():
            print(f"HierarchicalChunker: No markdown content to chunk for {source_url}.")
            return []

        final_chunks_data: List[Dict[str, Any]] = []

        # Split by H1
        h1_sections = self._split_by_header_level(markdown_content, "# ")
        if len(h1_sections) == 1 and markdown_content.startswith("# "): # Only one H1 section is the whole doc
            pass # Proceed to H2 within this section
        elif not any(s.startswith("# ") for s in h1_sections) and h1_sections: # No H1s at all
             h1_sections = [markdown_content] # Treat whole doc as one section for H2/H3 splitting

        chunk_index_counter = 0
        for h1_text in h1_sections:
            current_h1_title = h1_text.splitlines()[0].lstrip('# ').strip() if h1_text.startswith("# ") else ""

            # Split by H2 within H1 section
            h2_sections = self._split_by_header_level(h1_text, "## ")
            if len(h2_sections) == 1 and h1_text.startswith("## "): # Only one H2 section means h1_text was actually an H2 block
                 pass
            elif not any(s.startswith("## ") for s in h2_sections) and h2_sections:
                 h2_sections = [h1_text]

            for h2_text in h2_sections:
                current_h2_title = h2_text.splitlines()[0].lstrip('## ').strip() if h2_text.startswith("## ") else ""

                # Split by H3 within H2 section
                h3_sections = self._split_by_header_level(h2_text, "### ")
                if len(h3_sections) == 1 and h2_text.startswith("### "):
                    pass
                elif not any(s.startswith("### ") for s in h3_sections) and h3_sections:
                    h3_sections = [h2_text]

                for h3_text_segment in h3_sections:
                    current_h3_title = h3_text_segment.splitlines()[0].lstrip('### ').strip() if h3_text_segment.startswith("### ") else ""

                    # Now, if h3_text_segment is still too large, split by character limit
                    char_split_sub_chunks = self._split_by_char_limit(h3_text_segment)

                    for sub_chunk_text in char_split_sub_chunks:
                        if not sub_chunk_text.strip():
                            continue

                        headers_info = []
                        if current_h1_title: headers_info.append(f"H1: {current_h1_title}")
                        if current_h2_title and current_h2_title != current_h1_title : headers_info.append(f"H2: {current_h2_title}")
                        if current_h3_title and current_h3_title != current_h2_title: headers_info.append(f"H3: {current_h3_title}")

                        chunk_metadata = {
                            **base_metadata, # original_url, crawl_depth
                            "source_url": source_url, # Redundant but good for direct use
                            "document_title": doc_title,
                            "chunk_index": chunk_index_counter,
                            "headers": "; ".join(headers_info) if headers_info else "General Content",
                            "char_count": len(sub_chunk_text)
                        }

                        final_chunks_data.append({
                            "id": f"{source_url}_chunk_{chunk_index_counter}", # Unique ID for the chunk
                            "text": sub_chunk_text,
                            "metadata": chunk_metadata
                            # Embedding will be added by KnowledgeAgentTool
                        })
                        chunk_index_counter += 1

        print(f"HierarchicalChunker: Generated {len(final_chunks_data)} chunks for {source_url}.")
        return final_chunks_data