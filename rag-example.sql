-- SQL Schema for Task 016: Supabase/pgvector Integration
-- This file contains the required database schema for the KnowledgeAgentTool
-- to work with Supabase and pgvector extension.

-- Enable the pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create the rag_pages table for storing document chunks with embeddings
CREATE TABLE IF NOT EXISTS rag_pages (
    id BIGSERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    chunk_number INTEGER NOT NULL,
    content TEXT NOT NULL,
    embedding VECTOR(1536), -- OpenAI text-embedding-3-small dimension
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    UNIQUE(url, chunk_number)
);

-- Create an index on the embedding column for fast vector similarity search
CREATE INDEX IF NOT EXISTS rag_pages_embedding_idx ON rag_pages 
USING ivfflat (embedding vector_cosine_ops) WITH (lists = 100);

-- Create an index on url for fast source queries
CREATE INDEX IF NOT EXISTS rag_pages_url_idx ON rag_pages (url);

-- Create an index on metadata for filtered searches
CREATE INDEX IF NOT EXISTS rag_pages_metadata_idx ON rag_pages USING gin (metadata);

-- Create the match_rag_pages RPC function for semantic search
CREATE OR REPLACE FUNCTION match_rag_pages(
    query_embedding VECTOR(1536),
    match_count INT DEFAULT 5,
    filter JSONB DEFAULT '{}'
)
RETURNS TABLE(
    id BIGINT,
    url TEXT,
    chunk_number INTEGER,
    content TEXT,
    metadata JSONB,
    similarity FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN QUERY
    SELECT
        rag_pages.id,
        rag_pages.url,
        rag_pages.chunk_number,
        rag_pages.content,
        rag_pages.metadata,
        1 - (rag_pages.embedding <=> query_embedding) AS similarity
    FROM rag_pages
    WHERE 
        CASE 
            WHEN filter = '{}' THEN true
            ELSE rag_pages.metadata @> filter
        END
    ORDER BY rag_pages.embedding <=> query_embedding
    LIMIT match_count;
END;
$$;

-- Grant permissions (adjust as needed for your setup)
-- These are basic permissions - you may need to adjust based on your Supabase setup
ALTER TABLE rag_pages ENABLE ROW LEVEL SECURITY;

-- Example policy (you may want to adjust this based on your authentication needs)
CREATE POLICY "Allow anonymous access to rag_pages" ON rag_pages
    FOR ALL USING (true);

-- Create a function to get unique sources
CREATE OR REPLACE FUNCTION get_unique_sources()
RETURNS TABLE(url TEXT)
LANGUAGE sql
AS $$
    SELECT DISTINCT rag_pages.url FROM rag_pages ORDER BY rag_pages.url;
$$;

-- Comments for documentation
COMMENT ON TABLE rag_pages IS 'Stores document chunks with their vector embeddings for RAG operations';
COMMENT ON COLUMN rag_pages.url IS 'Source URL or identifier for the document';
COMMENT ON COLUMN rag_pages.chunk_number IS 'Sequential number of the chunk within the document';
COMMENT ON COLUMN rag_pages.content IS 'Text content of the document chunk';
COMMENT ON COLUMN rag_pages.embedding IS 'Vector embedding of the content (1536 dimensions for OpenAI)';
COMMENT ON COLUMN rag_pages.metadata IS 'Additional metadata about the chunk (JSON format)';
COMMENT ON FUNCTION match_rag_pages IS 'Performs semantic search using vector similarity with optional metadata filtering';
COMMENT ON FUNCTION get_unique_sources IS 'Returns list of unique source URLs in the database';