-- Supabase Schema for Task 16 - KnowledgeAgent RAG Database
-- This file contains the SQL schema needed for the Supabase database
-- Execute this in your Supabase SQL editor before using Task 16

-- Enable the pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create the rag_pages table for storing document chunks with embeddings
CREATE TABLE IF NOT EXISTS rag_pages (
    id BIGSERIAL PRIMARY KEY,
    url TEXT NOT NULL,
    chunk_number INTEGER NOT NULL DEFAULT 0,
    content TEXT NOT NULL,
    embedding VECTOR(1536), -- OpenAI text-embedding-3-small dimension
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS rag_pages_url_idx ON rag_pages(url);
CREATE INDEX IF NOT EXISTS rag_pages_chunk_number_idx ON rag_pages(chunk_number);
CREATE INDEX IF NOT EXISTS rag_pages_embedding_idx ON rag_pages USING ivfflat (embedding vector_cosine_ops);

-- Create the match_rag_pages RPC function for semantic search
CREATE OR REPLACE FUNCTION match_rag_pages(
    query_embedding VECTOR(1536),
    match_count INTEGER DEFAULT 5,
    filter JSONB DEFAULT '{}'
)
RETURNS TABLE (
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
        rp.id,
        rp.url,
        rp.chunk_number,
        rp.content,
        rp.metadata,
        1 - (rp.embedding <=> query_embedding) AS similarity
    FROM rag_pages rp
    WHERE 
        CASE 
            WHEN filter = '{}' THEN TRUE
            ELSE rp.metadata @> filter
        END
    ORDER BY rp.embedding <=> query_embedding
    LIMIT match_count;
END;
$$;

-- Create RLS (Row Level Security) policies if needed
-- ALTER TABLE rag_pages ENABLE ROW LEVEL SECURITY;

-- Example policy (uncomment if you need user-specific access control)
-- CREATE POLICY "Users can view their own data" ON rag_pages
--     FOR SELECT USING (auth.uid()::text = (metadata->>'user_id'));

-- Grant necessary permissions
-- GRANT USAGE ON SCHEMA public TO anon, authenticated;
-- GRANT ALL ON rag_pages TO anon, authenticated;
-- GRANT EXECUTE ON FUNCTION match_rag_pages TO anon, authenticated;
