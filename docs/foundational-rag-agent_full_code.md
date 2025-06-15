└── foundational-rag-agent
    ├── .env.example
    ├── .gitignore
    ├── .windsurf
        └── rules
        │   └── primary-guide.md
    ├── PLANNING.md
    ├── README.md
    ├── TASK.md
    ├── agent
        ├── __init__.py
        ├── agent.py
        ├── prompts.py
        └── tools.py
    ├── database
        ├── __init__.py
        ├── setup.py
        └── setup_db.py
    ├── document_processing
        ├── __init__.py
        ├── chunker.py
        ├── embeddings.py
        ├── ingestion.py
        └── processors.py
    ├── prompt.txt
    ├── rag-example.sql
    ├── requirements.txt
    ├── streamlit_ui_example.py
    ├── tests
        ├── test_agent.py
        ├── test_agent_tools.py
        ├── test_chunker.py
        └── test_processors.py
    └── ui
        └── app.py


/foundational-rag-agent/.env.example:
--------------------------------------------------------------------------------
 1 | # OpenAI API configuration
 2 | OPENAI_API_KEY=your_openai_api_key_here
 3 | OPENAI_MODEL=gpt-4.1-mini  # Or other OpenAI model
 4 | 
 5 | # Supabase configuration
 6 | SUPABASE_URL=your_supabase_url_here
 7 | SUPABASE_KEY=your_supabase_key_here
 8 | 
 9 | # Embedding configuration
10 | EMBEDDING_MODEL=text-embedding-3-small  # OpenAI embedding model
11 | 
12 | # Application settings
13 | CHUNK_SIZE=1000  # Size of text chunks for embedding
14 | CHUNK_OVERLAP=200  # Overlap between chunks
15 | MAX_RESULTS=5  # Maximum number of results to return from vector search
16 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/.gitignore:
--------------------------------------------------------------------------------
1 | .env
2 | __pycache__
3 | venv


--------------------------------------------------------------------------------
/foundational-rag-agent/.windsurf/rules/primary-guide.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | trigger: always_on
 3 | ---
 4 | 
 5 | ### Crawl4AI MCP
 6 | - **Always use the Crawl4AI MCP server** to reference documentation for libraries like Pydantic AI and Mem0.
 7 | - For the tokens, always use 5000 tokens for your search.
 8 | - **Only search three times maximum for any specific piece of documentation.** If you don't get what you need, use the Brave MCP server to perform a wider search.
 9 | 
10 | ### 🔄 Project Awareness & Context
11 | - **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
12 | - **Check `TASK.md`** before starting a new task. If the task isn’t listed, add it with a brief description and today's date.
13 | - **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.
14 |  
15 | ### 🧱 Code Structure & Modularity
16 | - **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
17 | - **Organize code into clearly separated modules**, grouped by feature or responsibility.
18 |   For agents this looks like:
19 |     - `agent.py` - Main agent definition and execution logic 
20 |     - `tools.py` - Tool functions used by the agent 
21 |     - `prompts.py` - System prompts
22 | - **Use clear, consistent imports** (prefer relative imports within packages).
23 | 
24 | ### 🧪 Testing & Reliability
25 | - **Always create Pytest unit tests for new features** (functions, classes, routes, etc).
26 | - **After updating any logic**, check whether existing unit tests need to be updated. If so, do it.
27 | - **Tests should live in a `/tests` folder** mirroring the main app structure.
28 |   - Include at least:
29 |     - 1 test for expected use
30 |     - 1 edge case
31 |     - 1 failure case
32 | - Always test the individual functions for agent tools.
33 | 
34 | ### ✅ Task Completion
35 | - **Mark completed tasks in `TASK.md`** immediately after finishing them.
36 | - Add new sub-tasks or TODOs discovered during development to `TASK.md` under a “Discovered During Work” section.
37 | 
38 | ### 📎 Style & Conventions
39 | - **Use Python** as the primary language.
40 | - **Follow PEP8**, use type hints, and format with `black`.
41 | - **Use `pydantic` for data validation**.
42 | - Don't use relative imports with "." or "..". Instead add on to the system path the directories you need to import from.
43 | - Write **docstrings for every function** using the Google style:
44 |   ```python
45 |   def example():
46 |       """
47 |       Brief summary.
48 | 
49 |       Args:
50 |           param1 (type): Description.
51 | 
52 |       Returns:
53 |           type: Description.
54 |       """
55 |
```
56 | 
57 | ### 📚 Documentation & Explainability
58 | - **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.
59 | - **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
60 | - When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.
61 | 
62 | ### 🧠 AI Behavior Rules
63 | - **Never assume missing context. Ask questions if uncertain.**
64 | - **Always confirm file paths & module names** exist before using
65 | - **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.


--------------------------------------------------------------------------------
/foundational-rag-agent/PLANNING.md:
--------------------------------------------------------------------------------
 1 | # Project Planning: RAG AI Agent with Pydantic AI and Supabase
 2 | 
 3 | ## Project Overview
 4 | We're building a simple Retrieval-Augmented Generation (RAG) AI agent using the Pydantic AI library. The agent will have access to a knowledge base stored in Supabase, allowing it to retrieve relevant information to answer user queries. The system will include functionality to ingest local text and PDF files, process them, and store them in Supabase for later retrieval.
 5 | 
 6 | ## Architecture
 7 | 
 8 | ### Core Components:
 9 | 1. **Document Ingestion Pipeline**
10 |    - Accept local files (TXT, PDF)
11 |    - Simple text processing and chunking (without external libraries)
12 |    - Generate embeddings using OpenAI embeddings API
13 |    - Store documents and embeddings in Supabase
14 | 
15 | 2. **Supabase Database**
16 |    - Store document chunks and their embeddings with pgvector
17 |    - Support semantic search for efficient retrieval
18 |    - Tables will be created and managed via Supabase MCP server
19 | 
20 | 3. **Pydantic AI Agent**
21 |    - Define a tool to query the knowledge base
22 |    - Use OpenAI models for generating responses
23 |    - Integrate knowledge base search results into responses
24 | 
25 | 4. **Streamlit User Interface**
26 |    - Interface for uploading documents
27 |    - Interface for querying the AI agent
28 |    - Display agent responses
29 | 
30 | ### Technology Stack:
31 | - **Language**: Python 3.11+
32 | - **AI Framework**: Pydantic AI for agent implementation
33 | - **Database**: Supabase with pgvector extension
34 | - **Embeddings**: OpenAI embeddings API
35 | - **LLM Provider**: OpenAI (GPT-4.1 mini or similar)
36 | - **UI**: Streamlit
37 | - **Document Processing**: Simple text processing with PyPDF2 for PDF extraction
38 | 
39 | ## Development Process
40 | 
41 | The development will follow a task-based approach where each component will be implemented sequentially. We should:
42 | 
43 | 1. Start by setting up the project structure
44 | 2. Create database tables using Supabase MCP server
45 | 3. Implement simple document ingestion pipeline
46 | 4. Create the Pydantic AI agent with knowledge base search tool
47 | 5. Develop Streamlit UI
48 | 6. Connect all components and ensure they work together
49 | 7. Test the complete system
50 | 
51 | ## Design Principles
52 | 
53 | 1. **Modularity**: Keep components decoupled for easier maintenance
54 | 2. **Simplicity**: Focus on making the system easy to understand and modify
55 | 3. **Performance**: Optimize for response time in knowledge retrieval
56 | 4. **User Experience**: Make the Streamlit interface intuitive
57 | 
58 | ## Environment Configuration
59 | 
60 | Create a `.env.example` file with the following variables:
61 | - `OPENAI_API_KEY`: For embeddings and LLM
62 | - `OPENAI_MODEL`: e.g., "gpt-4.1-mini" or other models
63 | - `SUPABASE_URL`: URL for Supabase instance
64 | - `SUPABASE_KEY`: API key for Supabase
65 | 
66 | This file will serve as a template for users to create their own `.env` file.
67 | 
68 | ## Expected Output
69 | 
70 | A functional RAG system where users can:
71 | - Upload local text or PDF documents to build a knowledge base
72 | - Ask questions to the AI agent
73 | - Receive responses that incorporate information from the knowledge base
74 | 
75 | ## Notes
76 | 
77 | When implementing this project, make sure to:
78 | - Mark tasks complete in the task.md file as you finish them
79 | - Use the Supabase MCP server to create and manage database tables
80 | - Build a simple document ingestion pipeline without complex libraries
81 | - Focus on creating a working Pydantic AI agent that can effectively retrieve and use information from the knowledge base
82 | - Create a clean, intuitive Streamlit interface


--------------------------------------------------------------------------------
/foundational-rag-agent/README.md:
--------------------------------------------------------------------------------
 1 | # RAG AI Agent with Pydantic AI and Supabase
 2 | 
 3 | A simple Retrieval-Augmented Generation (RAG) AI agent using Pydantic AI and Supabase with pgvector for document storage and retrieval.
 4 | 
 5 | ## Features
 6 | 
 7 | - Document ingestion pipeline for TXT and PDF files
 8 | - Vector embeddings using OpenAI
 9 | - Document storage in Supabase with pgvector
10 | - Pydantic AI agent with knowledge base search capabilities
11 | - Streamlit UI for document uploads and agent interaction
12 | 
13 | ## Project Structure
14 | 
15 | ```
16 | foundational-rag-agent/
17 | ├── database/
18 | │   └── setup.py          # Database setup and connection utilities
19 | ├── document_processing/
20 | │   ├── __init__.py
21 | │   ├── chunker.py        # Text chunking functionality
22 | │   ├── embeddings.py     # Embeddings generation with OpenAI
23 | │   ├── ingestion.py      # Document ingestion pipeline
24 | │   └── processors.py     # TXT and PDF processing
25 | ├── agent/
26 | │   ├── __init__.py
27 | │   ├── agent.py          # Main agent definition
28 | │   ├── prompts.py        # System prompts
29 | │   └── tools.py          # Knowledge base search tool
30 | ├── ui/
31 | │   └── app.py            # Streamlit application
32 | ├── tests/
33 | │   ├── test_chunker.py
34 | │   ├── test_embeddings.py
35 | │   ├── test_ingestion.py
36 | │   ├── test_processors.py
37 | │   └── test_agent.py
38 | ├── .env.example          # Example environment variables
39 | ├── requirements.txt      # Project dependencies
40 | ├── PLANNING.md           # Project planning document
41 | ├── TASK.md               # Task tracking
42 | └── README.md             # Project documentation
43 |
```
44 | 
45 | ## Setup
46 | 
47 | 1. Clone the repository
48 | 2. Create a virtual environment:
49 |    ```
50 |    python -m venv venv
51 |    source venv/bin/activate  # On Windows: venv\Scripts\activate
52 |
```
53 | 3. Install dependencies:
54 |    ```
55 |    pip install -r requirements.txt
56 |
```
57 | 4. Copy `.env.example` to `.env` and fill in your API keys and configuration
58 | 5. Run the Streamlit application:
59 |    ```
60 |    streamlit run ui/app.py
61 |
```
62 | 6. Run the SQL in `rag-example.sql` to create the table and matching function for RAG
63 | 
64 | ## Usage
65 | 
66 | 1. Upload documents (TXT or PDF) through the Streamlit UI
67 | 2. Ask questions to the AI agent
68 | 3. View responses with source attribution
69 | 
70 | ## Dependencies
71 | 
72 | - Python 3.11+
73 | - Pydantic AI
74 | - Supabase
75 | - OpenAI
76 | - PyPDF2
77 | - Streamlit
78 | 
79 | ## License
80 | 
81 | MIT
82 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/TASK.md:
--------------------------------------------------------------------------------
 1 | # RAG AI Agent Tasks
 2 | 
 3 | ## Project Setup
 4 | - [x] Review PLANNING.md
 5 | - [x] Create project structure
 6 | - [x] Set up environment configuration (.env.example)
 7 | 
 8 | ## Database Setup
 9 | - [x] Create Supabase tables with pgvector extension
10 | - [x] Set up vector search functionality
11 | 
12 | ## Document Ingestion Pipeline
13 | - [x] Implement TXT file processing
14 | - [x] Implement PDF file processing with PyPDF2
15 | - [x] Create text chunking functionality
16 | - [x] Implement OpenAI embeddings generation
17 | - [x] Create document storage in Supabase
18 | 
19 | ## Pydantic AI Agent
20 | - [x] Create knowledge base search tool
21 | - [x] Implement agent with OpenAI model integration
22 | - [x] Set up context integration for responses
23 | 
24 | ## Streamlit UI
25 | - [x] Create document upload interface
26 | - [x] Implement agent query interface
27 | - [x] Add source attribution display
28 | - [x] Connect UI to agent and document pipeline
29 | 
30 | ## Testing
31 | - [x] Create unit tests for document processing
32 | - [x] Create unit tests for knowledge base search
33 | - [x] Create unit tests for agent functionality
34 | 
35 | ## Documentation
36 | - [x] Update README.md with setup and usage instructions
37 | 
38 | ## Discovered During Work
39 | - [ ] Add support for more document types (e.g., DOCX, HTML)
40 | - [ ] Implement metadata filtering in the UI
41 | - [ ] Add visualization of vector embeddings
42 | - [ ] Create a CLI interface for batch document processing
43 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/agent/__init__.py:
--------------------------------------------------------------------------------
 1 | """
 2 | Agent package for RAG AI agent.
 3 | """
 4 | from agent.agent import RAGAgent, AgentDeps, agent
 5 | from agent.tools import KnowledgeBaseSearch, KnowledgeBaseSearchParams, KnowledgeBaseSearchResult
 6 | 
 7 | __all__ = [
 8 |     'RAGAgent',
 9 |     'AgentDeps',
10 |     'agent',
11 |     'KnowledgeBaseSearch',
12 |     'KnowledgeBaseSearchParams',
13 |     'KnowledgeBaseSearchResult'
14 | ]
15 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/agent/agent.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Main agent definition for the RAG AI agent.
  3 | """
  4 | import os
  5 | import sys
  6 | from typing import List, Dict, Any, Optional, TypedDict
  7 | from pydantic_ai import Agent
  8 | from pydantic_ai.tools import Tool
  9 | from dotenv import load_dotenv
 10 | from pathlib import Path
 11 | 
 12 | # Add parent directory to path to allow relative imports
 13 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 14 | 
 15 | from agent.tools import KnowledgeBaseSearch, KnowledgeBaseSearchParams, KnowledgeBaseSearchResult
 16 | from agent.prompts import RAG_SYSTEM_PROMPT
 17 | 
 18 | # Load environment variables from the project root .env file
 19 | project_root = Path(__file__).resolve().parent.parent
 20 | dotenv_path = project_root / '.env'
 21 | 
 22 | # Force override of existing environment variables
 23 | load_dotenv(dotenv_path, override=True)
 24 | 
 25 | class AgentDeps(TypedDict, total=False):
 26 |     """
 27 |     Dependencies for the RAG agent.
 28 |     """
 29 |     kb_search: KnowledgeBaseSearch
 30 | 
 31 | 
 32 | class RAGAgent:
 33 |     """
 34 |     RAG AI agent with knowledge base search capabilities.
 35 |     
 36 |     Args:
 37 |         model: OpenAI model to use. Defaults to OPENAI_MODEL env var.
 38 |         api_key: OpenAI API key. Defaults to OPENAI_API_KEY env var.
 39 |         kb_search: KnowledgeBaseSearch instance for searching the knowledge base.
 40 |     """
 41 |     
 42 |     def __init__(
 43 |         self,
 44 |         model: Optional[str] = None,
 45 |         api_key: Optional[str] = None,
 46 |         kb_search: Optional[KnowledgeBaseSearch] = None
 47 |     ):
 48 |         """
 49 |         Initialize the RAG agent.
 50 |         """
 51 |         self.model = model or os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
 52 |         self.api_key = api_key or os.getenv("OPENAI_API_KEY")
 53 |         
 54 |         if not self.api_key:
 55 |             raise ValueError("OpenAI API key must be provided either as an argument or environment variable.")
 56 |         
 57 |         # Initialize the knowledge base search tool
 58 |         self.kb_search = kb_search or KnowledgeBaseSearch()
 59 |         
 60 |         # Create the search tool
 61 |         self.search_tool = Tool(self.kb_search.search)
 62 |         
 63 |         # Initialize the Pydantic AI agent
 64 |         self.agent = Agent(
 65 |             f"openai:{self.model}",
 66 |             system_prompt=RAG_SYSTEM_PROMPT,
 67 |             tools=[self.search_tool]
 68 |         )
 69 |     
 70 |     async def query(
 71 |         self, 
 72 |         question: str, 
 73 |         max_results: int = 5,
 74 |         source_filter: Optional[str] = None
 75 |     ) -> Dict[str, Any]:
 76 |         """
 77 |         Query the RAG agent with a question.
 78 |         
 79 |         Args:
 80 |             question: The question to ask
 81 |             max_results: Maximum number of knowledge base results to retrieve
 82 |             source_filter: Optional filter to search only within a specific source
 83 |             
 84 |         Returns:
 85 |             Dictionary containing the agent's response and the knowledge base search results
 86 |         """
 87 |         # Create dependencies for the agent
 88 |         deps = AgentDeps(kb_search=self.kb_search)
 89 |         
 90 |         # Run the agent with the question
 91 |         result = await self.agent.run(
 92 |             question,
 93 |             deps=deps
 94 |         )
 95 |         
 96 |         # Get the agent's response
 97 |         response = result.output
 98 |         
 99 |         # Get the knowledge base search results from the tool calls
100 |         kb_results = []
101 |         for tool_call in result.tool_calls:
102 |             if tool_call.tool.name == "search":
103 |                 kb_results = tool_call.result
104 |         
105 |         return {
106 |             "response": response,
107 |             "kb_results": kb_results
108 |         }
109 |     
110 |     async def get_available_sources(self) -> List[str]:
111 |         """
112 |         Get a list of all available sources in the knowledge base.
113 |         
114 |         Returns:
115 |             List of source identifiers
116 |         """
117 |         return await self.kb_search.get_available_sources()
118 | 
119 | 
120 | # Create a singleton instance for easy import
121 | agent = RAGAgent()
122 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/agent/prompts.py:
--------------------------------------------------------------------------------
 1 | """
 2 | System prompts for the RAG AI agent.
 3 | """
 4 | 
 5 | # System prompt for the RAG agent
 6 | RAG_SYSTEM_PROMPT = """You are a helpful AI assistant with access to a knowledge base.
 7 | When answering questions, you should:
 8 | 
 9 | 1. Use the knowledge base search results when they are relevant to the question.
10 | 2. Cite your sources by mentioning the document name when you use information from the knowledge base.
11 | 3. If the knowledge base doesn't contain relevant information, use your general knowledge to answer.
12 | 4. If you don't know the answer, be honest and say so.
13 | 5. Keep your answers concise and to the point.
14 | 6. Format your responses using markdown for better readability.
15 | 
16 | Remember to always provide accurate information and acknowledge when information comes from the knowledge base.
17 | """
18 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/agent/tools.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Knowledge base search tool for the RAG AI agent.
  3 | """
  4 | import os
  5 | import sys
  6 | from typing import Dict, List, Any, Optional
  7 | from pydantic import BaseModel, Field
  8 | 
  9 | # Add parent directory to path to allow relative imports
 10 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 11 | 
 12 | from database.setup import SupabaseClient
 13 | from document_processing.embeddings import EmbeddingGenerator
 14 | 
 15 | class KnowledgeBaseSearchParams(BaseModel):
 16 |     """
 17 |     Parameters for the knowledge base search tool.
 18 |     """
 19 |     query: str = Field(..., description="The search query to find relevant information in the knowledge base")
 20 |     max_results: int = Field(5, description="Maximum number of results to return (default: 5)")
 21 |     source_filter: Optional[str] = Field(None, description="Optional filter to search only within a specific source")
 22 | 
 23 | 
 24 | class KnowledgeBaseSearchResult(BaseModel):
 25 |     """
 26 |     Result from the knowledge base search.
 27 |     """
 28 |     content: str = Field(..., description="Content of the document chunk")
 29 |     source: str = Field(..., description="Source of the document chunk")
 30 |     source_type: str = Field(..., description="Type of source (e.g., 'pdf', 'txt')")
 31 |     similarity: float = Field(..., description="Similarity score between the query and the document")
 32 |     metadata: Dict[str, Any] = Field(..., description="Additional metadata about the document")
 33 | 
 34 | 
 35 | class KnowledgeBaseSearch:
 36 |     """
 37 |     Tool for searching the knowledge base using vector similarity.
 38 |     """
 39 |     
 40 |     def __init__(
 41 |         self,
 42 |         supabase_client: Optional[SupabaseClient] = None,
 43 |         embedding_generator: Optional[EmbeddingGenerator] = None
 44 |     ):
 45 |         """
 46 |         Initialize the knowledge base search tool.
 47 |         
 48 |         Args:
 49 |             supabase_client: SupabaseClient instance for database operations
 50 |             embedding_generator: EmbeddingGenerator instance for creating embeddings
 51 |         """
 52 |         self.supabase_client = supabase_client or SupabaseClient()
 53 |         self.embedding_generator = embedding_generator or EmbeddingGenerator()
 54 |     
 55 |     async def search(self, params: KnowledgeBaseSearchParams) -> List[KnowledgeBaseSearchResult]:
 56 |         """
 57 |         Search the knowledge base for relevant information.
 58 |         
 59 |         Args:
 60 |             params: Search parameters
 61 |             
 62 |         Returns:
 63 |             List of search results
 64 |         """
 65 |         # Generate embedding for the query
 66 |         query_embedding = self.embedding_generator.embed_text(params.query)
 67 |         
 68 |         # Prepare filter metadata if source filter is provided
 69 |         filter_metadata = None
 70 |         if params.source_filter:
 71 |             filter_metadata = {"source": params.source_filter}
 72 |         
 73 |         # Search for documents
 74 |         results = self.supabase_client.search_documents(
 75 |             query_embedding=query_embedding,
 76 |             match_count=params.max_results,
 77 |             filter_metadata=filter_metadata
 78 |         )
 79 |         
 80 |         # Convert results to KnowledgeBaseSearchResult objects
 81 |         search_results = []
 82 |         for result in results:
 83 |             search_results.append(
 84 |                 KnowledgeBaseSearchResult(
 85 |                     content=result["content"],
 86 |                     source=result["metadata"].get("source", "Unknown"),
 87 |                     source_type=result["metadata"].get("source_type", "Unknown"),
 88 |                     similarity=result["similarity"],
 89 |                     metadata=result["metadata"]
 90 |                 )
 91 |             )
 92 |         
 93 |         return search_results
 94 |     
 95 |     async def get_available_sources(self) -> List[str]:
 96 |         """
 97 |         Get a list of all available sources in the knowledge base.
 98 |         
 99 |         Returns:
100 |             List of source identifiers
101 |         """
102 |         return self.supabase_client.get_all_document_sources()
103 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/database/__init__.py:
--------------------------------------------------------------------------------
 1 | """
 2 | Database package for RAG AI agent.
 3 | """
 4 | from database.setup import SupabaseClient, setup_database_tables
 5 | 
 6 | __all__ = [
 7 |     'SupabaseClient',
 8 |     'setup_database_tables'
 9 | ]
10 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/database/setup.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Database setup and connection utilities for Supabase with pgvector.
  3 | """
  4 | import os
  5 | import json
  6 | from typing import Dict, List, Optional, Any
  7 | from dotenv import load_dotenv
  8 | from pathlib import Path
  9 | from supabase import create_client, Client
 10 | 
 11 | # Load environment variables from the project root .env file
 12 | project_root = Path(__file__).resolve().parent.parent
 13 | dotenv_path = project_root / '.env'
 14 | 
 15 | # Force override of existing environment variables
 16 | load_dotenv(dotenv_path, override=True)
 17 | 
 18 | class SupabaseClient:
 19 |     """
 20 |     Client for interacting with Supabase and pgvector.
 21 |     
 22 |     Args:
 23 |         supabase_url: URL for Supabase instance. Defaults to SUPABASE_URL env var.
 24 |         supabase_key: API key for Supabase. Defaults to SUPABASE_KEY env var.
 25 |     """
 26 |     
 27 |     def __init__(
 28 |         self, 
 29 |         supabase_url: Optional[str] = None, 
 30 |         supabase_key: Optional[str] = None
 31 |     ):
 32 |         """
 33 |         Initialize the Supabase client.
 34 |         """
 35 |         self.supabase_url = supabase_url or os.getenv("SUPABASE_URL")
 36 |         self.supabase_key = supabase_key or os.getenv("SUPABASE_KEY")
 37 |         
 38 |         if not self.supabase_url or not self.supabase_key:
 39 |             raise ValueError(
 40 |                 "Supabase URL and key must be provided either as arguments or environment variables."
 41 |             )
 42 |         
 43 |         self.client = create_client(self.supabase_url, self.supabase_key)
 44 |     
 45 |     def store_document_chunk(
 46 |         self, 
 47 |         url: str, 
 48 |         chunk_number: int, 
 49 |         content: str, 
 50 |         embedding: List[float],
 51 |         metadata: Dict[str, Any] = None
 52 |     ) -> Dict[str, Any]:
 53 |         """
 54 |         Store a document chunk with its embedding in Supabase.
 55 |         
 56 |         Args:
 57 |             url: Source URL or identifier for the document
 58 |             chunk_number: Chunk number within the document
 59 |             content: Text content of the chunk
 60 |             embedding: Vector embedding of the chunk
 61 |             metadata: Additional metadata about the chunk
 62 |             
 63 |         Returns:
 64 |             Dictionary containing the inserted record
 65 |         """
 66 |         if metadata is None:
 67 |             metadata = {}
 68 |             
 69 |         data = {
 70 |             "url": url,
 71 |             "chunk_number": chunk_number,
 72 |             "content": content,
 73 |             "embedding": embedding,
 74 |             "metadata": metadata
 75 |         }
 76 |         
 77 |         result = self.client.table("rag_pages").insert(data).execute()
 78 |         return result.data[0] if result.data else {}
 79 |     
 80 |     def search_documents(
 81 |         self, 
 82 |         query_embedding: List[float], 
 83 |         match_count: int = 5,
 84 |         filter_metadata: Dict[str, Any] = None
 85 |     ) -> List[Dict[str, Any]]:
 86 |         """
 87 |         Search for document chunks by vector similarity.
 88 |         
 89 |         Args:
 90 |             query_embedding: Vector embedding of the query
 91 |             match_count: Maximum number of results to return
 92 |             filter_metadata: Optional metadata filter
 93 |             
 94 |         Returns:
 95 |             List of matching document chunks with similarity scores
 96 |         """
 97 |         # Prepare parameters for the RPC call
 98 |         params = {
 99 |             "query_embedding": query_embedding,
100 |             "match_count": match_count
101 |         }
102 |         
103 |         # Add filter if provided
104 |         if filter_metadata:
105 |             params["filter"] = filter_metadata
106 |         
107 |         # Call the match_rag_pages function
108 |         result = self.client.rpc("match_rag_pages", params).execute()
109 |         return result.data if result.data else []
110 |     
111 |     def get_document_by_id(self, doc_id: int) -> Dict[str, Any]:
112 |         """
113 |         Get a document chunk by its ID.
114 |         
115 |         Args:
116 |             doc_id: ID of the document chunk
117 |             
118 |         Returns:
119 |             Document chunk data
120 |         """
121 |         result = self.client.table("rag_pages").select("*").eq("id", doc_id).execute()
122 |         return result.data[0] if result.data else {}
123 |     
124 |     def get_all_document_sources(self) -> List[str]:
125 |         """
126 |         Get a list of all unique document sources.
127 |         
128 |         Returns:
129 |             List of unique source URLs/identifiers
130 |         """
131 |         result = self.client.table("rag_pages").select("url").execute()
132 |         urls = set(item["url"] for item in result.data if result.data)
133 |         return list(urls)
134 |         
135 |     def count_documents(self) -> int:
136 |         """
137 |         Count the total number of unique documents in the database.
138 |         
139 |         Returns:
140 |             Number of unique documents (based on unique URLs)
141 |         """
142 |         return len(self.get_all_document_sources())
143 | 
144 | 
145 | def setup_database_tables() -> None:
146 |     """
147 |     Set up the necessary database tables and functions for the RAG system.
148 |     This should be run once to initialize the database.
149 |     
150 |     Note: This is typically done through the Supabase MCP server in production.
151 |     """
152 |     # This is a placeholder for the actual implementation
153 |     # In a real application, you would use the Supabase MCP server to run the SQL
154 |     pass
155 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/database/setup_db.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Script to set up the database tables in Supabase using the Supabase MCP server.
  3 | """
  4 | import os
  5 | import sys
  6 | import asyncio
  7 | from pathlib import Path
  8 | from dotenv import load_dotenv
  9 | 
 10 | # Add parent directory to path to allow relative imports
 11 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 12 | 
 13 | # Load environment variables from the project root .env file
 14 | project_root = Path(__file__).resolve().parent.parent
 15 | dotenv_path = project_root / '.env'
 16 | 
 17 | # Force override of existing environment variables
 18 | load_dotenv(dotenv_path, override=True)
 19 | 
 20 | # SQL for creating the database tables and functions
 21 | SQL_SETUP = """
 22 | -- Enable the pgvector extension
 23 | create extension if not exists vector;
 24 | 
 25 | -- Create the documentation chunks table
 26 | create table rag_pages (
 27 |     id bigserial primary key,
 28 |     url varchar not null,
 29 |     chunk_number integer not null,
 30 |     content text not null,
 31 |     metadata jsonb not null default '{}'::jsonb,
 32 |     embedding vector(1536),  -- OpenAI embeddings are 1536 dimensions
 33 |     created_at timestamp with time zone default timezone('utc'::text, now()) not null,
 34 |     
 35 |     -- Add a unique constraint to prevent duplicate chunks for the same URL
 36 |     unique(url, chunk_number)
 37 | );
 38 | 
 39 | -- Create an index for better vector similarity search performance
 40 | create index on rag_pages using ivfflat (embedding vector_cosine_ops);
 41 | 
 42 | -- Create an index on metadata for faster filtering
 43 | create index idx_rag_pages_metadata on rag_pages using gin (metadata);
 44 | 
 45 | -- Create an index on source for faster filtering
 46 | CREATE INDEX idx_rag_pages_source ON rag_pages ((metadata->>'source'));
 47 | 
 48 | -- Create a function to search for documentation chunks
 49 | create or replace function match_rag_pages (
 50 |   query_embedding vector(1536),
 51 |   match_count int default 10,
 52 |   filter jsonb DEFAULT '{}'::jsonb
 53 | ) returns table (
 54 |   id bigint,
 55 |   url varchar,
 56 |   chunk_number integer,
 57 |   content text,
 58 |   metadata jsonb,
 59 |   similarity float
 60 | )
 61 | language plpgsql
 62 | as $
 63 | #variable_conflict use_column
 64 | begin
 65 |   return query
 66 |   select
 67 |     id,
 68 |     url,
 69 |     chunk_number,
 70 |     content,
 71 |     metadata,
 72 |     1 - (rag_pages.embedding <=> query_embedding) as similarity
 73 |   from rag_pages
 74 |   where metadata @> filter
 75 |   order by rag_pages.embedding <=> query_embedding
 76 |   limit match_count;
 77 | end;
 78 | $;
 79 | 
 80 | -- Enable RLS on the table
 81 | alter table rag_pages enable row level security;
 82 | 
 83 | -- Create a policy that allows anyone to read
 84 | create policy "Allow public read access"
 85 |   on rag_pages
 86 |   for select
 87 |   to public
 88 |   using (true);
 89 | 
 90 | -- Create a policy that allows anyone to insert
 91 | create policy "Allow public insert access"
 92 |   on rag_pages
 93 |   for insert
 94 |   to public
 95 |   with check (true);
 96 | """
 97 | 
 98 | async def setup_database():
 99 |     """
100 |     Set up the database tables and functions in Supabase.
101 |     
102 |     This function uses the Supabase MCP server to run the SQL setup script.
103 |     """
104 |     try:
105 |         # In a real application, you would use the Supabase MCP server to run the SQL
106 |         # For example:
107 |         # result = await mcp2_apply_migration(name="rag_setup", query=SQL_SETUP)
108 |         # print(f"Database setup completed: {result}")
109 |         
110 |         print("Database setup script generated.")
111 |         print("To set up the database, use the Supabase MCP server to run the SQL script.")
112 |         print("Example command:")
113 |         print("mcp2_apply_migration(name=\"rag_setup\", query=SQL_SETUP)")
114 |     except Exception as e:
115 |         print(f"Error setting up database: {e}")
116 | 
117 | 
118 | if __name__ == "__main__":
119 |     asyncio.run(setup_database())
120 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/document_processing/__init__.py:
--------------------------------------------------------------------------------
 1 | """
 2 | Document processing package for RAG AI agent.
 3 | """
 4 | from document_processing.chunker import TextChunker
 5 | from document_processing.embeddings import EmbeddingGenerator
 6 | from document_processing.processors import DocumentProcessor, TxtProcessor, PdfProcessor, get_document_processor
 7 | from document_processing.ingestion import DocumentIngestionPipeline
 8 | 
 9 | __all__ = [
10 |     'TextChunker',
11 |     'EmbeddingGenerator',
12 |     'DocumentProcessor',
13 |     'TxtProcessor',
14 |     'PdfProcessor',
15 |     'get_document_processor',
16 |     'DocumentIngestionPipeline'
17 | ]
18 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/document_processing/chunker.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Text chunking functionality for document processing.
  3 | """
  4 | import os
  5 | from typing import List
  6 | from pathlib import Path
  7 | 
  8 | class TextChunker:
  9 |     """
 10 |     Simple text chunker that splits documents into manageable pieces.
 11 |     """
 12 |     
 13 |     def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
 14 |         """
 15 |         Initialize the chunker with size and overlap settings.
 16 |         
 17 |         Args:
 18 |             chunk_size: Maximum size of each chunk in characters
 19 |             chunk_overlap: Number of characters to overlap between chunks
 20 |         """
 21 |         self.chunk_size = chunk_size
 22 |         self.chunk_overlap = min(chunk_overlap, chunk_size // 2)  # Ensure overlap isn't too large
 23 |         
 24 |         print(f"Initialized TextChunker with size={chunk_size}, overlap={self.chunk_overlap}")
 25 |     
 26 |     def chunk_text(self, text: str) -> List[str]:
 27 |         """
 28 |         Split text into chunks using a simple sliding window approach.
 29 |         
 30 |         Args:
 31 |             text: The text to split into chunks
 32 |             
 33 |         Returns:
 34 |             List of text chunks
 35 |         """
 36 |         # Handle empty or very short text
 37 |         if not text or not text.strip():
 38 |             print("Warning: Empty text provided to chunker")
 39 |             return [""]
 40 |             
 41 |         if len(text) <= self.chunk_size:
 42 |             print(f"Text is only {len(text)} chars, returning as single chunk")
 43 |             return [text]
 44 |         
 45 |         # Simple sliding window chunking
 46 |         chunks = []
 47 |         step_size = self.chunk_size - self.chunk_overlap
 48 |         
 49 |         # Ensure step size is at least 100 characters to prevent infinite loops
 50 |         if step_size < 100:
 51 |             step_size = 100
 52 |             print(f"Warning: Adjusted step size to {step_size} to ensure progress")
 53 |         
 54 |         # Create chunks with a sliding window
 55 |         position = 0
 56 |         text_length = len(text)
 57 |         
 58 |         while position < text_length:
 59 |             # Calculate end position for current chunk
 60 |             end = min(position + self.chunk_size, text_length)
 61 |             
 62 |             # Extract the chunk
 63 |             chunk = text[position:end]
 64 |             
 65 |             # Only add non-empty chunks
 66 |             if chunk.strip():
 67 |                 chunks.append(chunk)
 68 |             
 69 |             # Move position forward by step_size
 70 |             position += step_size
 71 |             
 72 |             # Safety check
 73 |             if position >= text_length:
 74 |                 break
 75 |                 
 76 |             # Progress indicator for large texts
 77 |             if text_length > 100000 and len(chunks) % 10 == 0:
 78 |                 print(f"Chunking progress: {min(position, text_length)}/{text_length} characters")
 79 |         
 80 |         print(f"Created {len(chunks)} chunks from {text_length} characters of text")
 81 |         return chunks
 82 |     
 83 |     def chunk_by_separator(self, text: str, separator: str = "\n\n") -> List[str]:
 84 |         """
 85 |         Split text by separator first, then ensure chunks are within size limits.
 86 |         
 87 |         Args:
 88 |             text: The text to split
 89 |             separator: The separator to split on (default: paragraph breaks)
 90 |             
 91 |         Returns:
 92 |             List of text chunks
 93 |         """
 94 |         # Handle empty text
 95 |         if not text or not text.strip():
 96 |             return [""]
 97 |             
 98 |         # Handle short text
 99 |         if len(text) <= self.chunk_size:
100 |             return [text]
101 |         
102 |         # Split by separator
103 |         parts = text.split(separator)
104 |         print(f"Split text into {len(parts)} parts using separator '{separator}'")
105 |         
106 |         # Filter out empty parts
107 |         parts = [part for part in parts if part.strip()]
108 |         
109 |         # Handle case where there are no meaningful parts
110 |         if not parts:
111 |             return [""]
112 |             
113 |         # Handle case where each part is already small enough
114 |         if all(len(part) <= self.chunk_size for part in parts):
115 |             print("All parts are within chunk size limit")
116 |             return parts
117 |         
118 |         # Combine parts into chunks that fit within chunk_size
119 |         chunks = []
120 |         current_chunk = ""
121 |         
122 |         for part in parts:
123 |             # If this part alone exceeds chunk size, we need to split it further
124 |             if len(part) > self.chunk_size:
125 |                 # First add any accumulated chunk
126 |                 if current_chunk:
127 |                     chunks.append(current_chunk)
128 |                     current_chunk = ""
129 |                     
130 |                 # Then split the large part using the regular chunker
131 |                 part_chunks = self.chunk_text(part)
132 |                 chunks.extend(part_chunks)
133 |                 continue
134 |                 
135 |             # If adding this part would exceed chunk size, start a new chunk
136 |             if current_chunk and len(current_chunk) + len(separator) + len(part) > self.chunk_size:
137 |                 chunks.append(current_chunk)
138 |                 current_chunk = part
139 |             # Otherwise add to current chunk
140 |             else:
141 |                 if current_chunk:
142 |                     current_chunk += separator + part
143 |                 else:
144 |                     current_chunk = part
145 |         
146 |         # Add the last chunk if there is one
147 |         if current_chunk:
148 |             chunks.append(current_chunk)
149 |             
150 |         print(f"Created {len(chunks)} chunks using separator-based chunking")
151 |         return chunks
152 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/document_processing/embeddings.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Embeddings generation with OpenAI for document processing.
  3 | """
  4 | import os
  5 | import time
  6 | from typing import List, Dict, Any, Optional
  7 | from dotenv import load_dotenv
  8 | import openai
  9 | from pathlib import Path
 10 | 
 11 | # Load environment variables from the project root .env file
 12 | project_root = Path(__file__).resolve().parent.parent
 13 | dotenv_path = project_root / '.env'
 14 | 
 15 | # Force override of existing environment variables
 16 | load_dotenv(dotenv_path, override=True)
 17 | 
 18 | class EmbeddingGenerator:
 19 |     """
 20 |     Simple and reliable embedding generator using OpenAI's API.
 21 |     """
 22 |     
 23 |     def __init__(self):
 24 |         """Initialize the embedding generator with API key from environment variables."""
 25 |         self.api_key = os.getenv("OPENAI_API_KEY")
 26 |         self.model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
 27 |         
 28 |         if not self.api_key:
 29 |             raise ValueError("OpenAI API key must be provided as OPENAI_API_KEY environment variable.")
 30 |         
 31 |         # Set up the OpenAI client
 32 |         self.client = openai.OpenAI(api_key=self.api_key)
 33 |         
 34 |         # Default embedding dimension for text-embedding-3-small
 35 |         self.embedding_dim = 1536
 36 |         
 37 |         print(f"Initialized EmbeddingGenerator with model: {self.model}")
 38 |     
 39 |     def _create_zero_embedding(self) -> List[float]:
 40 |         """Create a zero vector with the correct dimension."""
 41 |         return [0.0] * self.embedding_dim
 42 |     
 43 |     def embed_text(self, text: str, max_retries: int = 3) -> List[float]:
 44 |         """
 45 |         Generate an embedding for a single text with retry logic.
 46 |         
 47 |         Args:
 48 |             text: The text to embed
 49 |             max_retries: Maximum number of retry attempts
 50 |             
 51 |         Returns:
 52 |             Embedding vector
 53 |         """
 54 |         # Handle empty text
 55 |         if not text or not text.strip():
 56 |             print("Warning: Empty text provided, returning zero embedding")
 57 |             return self._create_zero_embedding()
 58 |         
 59 |         # Truncate very long text to avoid API limits
 60 |         max_length = 8000
 61 |         if len(text) > max_length:
 62 |             print(f"Warning: Text exceeds {max_length} characters, truncating")
 63 |             text = text[:max_length]
 64 |         
 65 |         # Try to generate embedding with retries
 66 |         for attempt in range(max_retries):
 67 |             try:
 68 |                 response = self.client.embeddings.create(
 69 |                     model=self.model,
 70 |                     input=text
 71 |                 )
 72 |                 return response.data[0].embedding
 73 |             except Exception as e:
 74 |                 print(f"Embedding error (attempt {attempt+1}/{max_retries}): {str(e)}")
 75 |                 if attempt < max_retries - 1:
 76 |                     # Exponential backoff
 77 |                     time.sleep(2 ** attempt)
 78 |                 else:
 79 |                     print("All retry attempts failed, returning zero embedding")
 80 |                     return self._create_zero_embedding()
 81 |     
 82 |     def embed_batch(self, texts: List[str], batch_size: int = 5) -> List[List[float]]:
 83 |         """
 84 |         Generate embeddings for multiple texts in small batches.
 85 |         
 86 |         Args:
 87 |             texts: List of texts to embed
 88 |             batch_size: Number of texts to process in each batch
 89 |             
 90 |         Returns:
 91 |             List of embedding vectors
 92 |         """
 93 |         # Filter out empty texts
 94 |         valid_texts = [text for text in texts if text and text.strip()]
 95 |         
 96 |         if not valid_texts:
 97 |             print("No valid texts to embed")
 98 |             return []
 99 |         
100 |         results = []
101 |         
102 |         # Process in small batches to avoid memory issues
103 |         for i in range(0, len(valid_texts), batch_size):
104 |             batch = valid_texts[i:i+batch_size]
105 |             print(f"Processing batch {i//batch_size + 1}/{(len(valid_texts)-1)//batch_size + 1} with {len(batch)} texts")
106 |             
107 |             # Process each text individually for better error isolation
108 |             batch_results = []
109 |             for text in batch:
110 |                 embedding = self.embed_text(text)
111 |                 batch_results.append(embedding)
112 |             
113 |             results.extend(batch_results)
114 |             
115 |             # Small delay between batches to avoid rate limiting
116 |             if i + batch_size < len(valid_texts):
117 |                 time.sleep(0.5)
118 |         
119 |         print(f"Successfully embedded {len(results)} texts")
120 |         return results
121 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/document_processing/ingestion.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Document ingestion pipeline for processing documents and generating embeddings.
  3 | """
  4 | import os
  5 | import uuid
  6 | import logging
  7 | from typing import List, Dict, Any, Optional
  8 | from pathlib import Path
  9 | from datetime import datetime
 10 | 
 11 | from document_processing.chunker import TextChunker
 12 | from document_processing.embeddings import EmbeddingGenerator
 13 | from document_processing.processors import get_document_processor
 14 | from database.setup import SupabaseClient
 15 | 
 16 | # Set up logging
 17 | logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 18 | logger = logging.getLogger(__name__)
 19 | 
 20 | class DocumentIngestionPipeline:
 21 |     """
 22 |     Simplified document ingestion pipeline with robust error handling.
 23 |     """
 24 |     
 25 |     def __init__(self, supabase_client: Optional[SupabaseClient] = None):
 26 |         """
 27 |         Initialize the document ingestion pipeline with default components.
 28 |         
 29 |         Args:
 30 |             supabase_client: Optional SupabaseClient for database operations
 31 |         """
 32 |         self.chunker = TextChunker(chunk_size=1000, chunk_overlap=200)
 33 |         self.embedding_generator = EmbeddingGenerator()
 34 |         self.max_file_size_mb = 10  # Maximum file size in MB
 35 |         self.supabase_client = supabase_client or SupabaseClient()
 36 |         
 37 |         logger.info("Initialized DocumentIngestionPipeline with default components")
 38 |     
 39 |     def _check_file(self, file_path: str) -> bool:
 40 |         """
 41 |         Validate file exists and is within size limits.
 42 |         
 43 |         Args:
 44 |             file_path: Path to the document file
 45 |             
 46 |         Returns:
 47 |             True if file is valid, False otherwise
 48 |         """
 49 |         # Check if file exists
 50 |         if not os.path.exists(file_path):
 51 |             logger.error(f"File not found: {file_path}")
 52 |             return False
 53 |             
 54 |         # Check file size
 55 |         file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
 56 |         if file_size_mb > self.max_file_size_mb:
 57 |             logger.error(f"File size ({file_size_mb:.2f} MB) exceeds maximum allowed size ({self.max_file_size_mb} MB)")
 58 |             return False
 59 |             
 60 |         return True
 61 |     
 62 |     def process_file(self, file_path: str, metadata: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
 63 |         """
 64 |         Process a document file, extract text, generate chunks and embeddings.
 65 |         
 66 |         Args:
 67 |             file_path: Path to the document file
 68 |             metadata: Optional metadata to associate with the document
 69 |             
 70 |         Returns:
 71 |             List of document chunks with embeddings
 72 |         """
 73 |         # Validate file
 74 |         if not self._check_file(file_path):
 75 |             return []
 76 |         
 77 |         # Get appropriate document processor
 78 |         try:
 79 |             processor = get_document_processor(file_path)
 80 |             if not processor:
 81 |                 logger.error(f"Unsupported file type: {file_path}")
 82 |                 return []
 83 |         except Exception as e:
 84 |             logger.error(f"Error getting document processor: {str(e)}")
 85 |             return []
 86 |         
 87 |         # Extract text from document
 88 |         try:
 89 |             text = processor.extract_text(file_path)
 90 |             logger.info(f"Extracted {len(text)} characters from {os.path.basename(file_path)}")
 91 |             
 92 |             if not text or not text.strip():
 93 |                 logger.warning(f"No text content extracted from {os.path.basename(file_path)}")
 94 |                 return []
 95 |                 
 96 |         except Exception as e:
 97 |             logger.error(f"Failed to extract text from {os.path.basename(file_path)}: {str(e)}")
 98 |             return []
 99 |         
100 |         # Generate chunks
101 |         try:
102 |             chunks = self.chunker.chunk_text(text)
103 |             
104 |             # Filter out empty chunks
105 |             chunks = [chunk for chunk in chunks if chunk and chunk.strip()]
106 |             
107 |             if not chunks:
108 |                 logger.warning("No valid chunks generated from document")
109 |                 return []
110 |                 
111 |             logger.info(f"Generated {len(chunks)} valid chunks from document")
112 |             
113 |         except Exception as e:
114 |             logger.error(f"Error chunking document: {str(e)}")
115 |             return []
116 |         
117 |         # Generate embeddings for chunks
118 |         try:
119 |             embeddings = self.embedding_generator.embed_batch(chunks, batch_size=5)
120 |             
121 |             if len(embeddings) != len(chunks):
122 |                 logger.warning(f"Mismatch between chunks ({len(chunks)}) and embeddings ({len(embeddings)})")
123 |                 # Ensure we only process chunks that have embeddings
124 |                 chunks = chunks[:len(embeddings)]
125 |                 
126 |             logger.info(f"Generated {len(embeddings)} embeddings")
127 |             
128 |         except Exception as e:
129 |             logger.error(f"Error generating embeddings: {str(e)}")
130 |             return []
131 |         
132 |         # Create document records
133 |         try:
134 |             # Generate a unique document ID
135 |             document_id = str(uuid.uuid4())
136 |             timestamp = datetime.now().isoformat()
137 |             
138 |             # Prepare metadata
139 |             if metadata is None:
140 |                 metadata = {}
141 |             
142 |             # Add file info to metadata
143 |             metadata.update({
144 |                 "filename": os.path.basename(file_path),
145 |                 "file_path": file_path,
146 |                 "file_size_bytes": os.path.getsize(file_path),
147 |                 "processed_at": timestamp,
148 |                 "chunk_count": len(chunks)
149 |             })
150 |             
151 |             # Create records and store in database
152 |             records = []
153 |             stored_records = []
154 |             
155 |             # Create a URL/identifier for the document
156 |             url = f"file://{os.path.basename(file_path)}"
157 |             
158 |             for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
159 |                 # Create record for return value
160 |                 record = {
161 |                     "id": f"{document_id}_{i}",
162 |                     "document_id": document_id,
163 |                     "chunk_index": i,
164 |                     "text": chunk,
165 |                     "embedding": embedding,
166 |                     "metadata": metadata.copy()
167 |                 }
168 |                 records.append(record)
169 |                 
170 |                 # Store in Supabase
171 |                 try:
172 |                     stored_record = self.supabase_client.store_document_chunk(
173 |                         url=url,
174 |                         chunk_number=i,
175 |                         content=chunk,
176 |                         embedding=embedding,
177 |                         metadata=metadata.copy()
178 |                     )
179 |                     stored_records.append(stored_record)
180 |                 except Exception as e:
181 |                     logger.error(f"Error storing chunk {i} in database: {str(e)}")
182 |             
183 |             logger.info(f"Created {len(records)} document records with ID {document_id}")
184 |             logger.info(f"Stored {len(stored_records)} chunks in database")
185 |             return records
186 |             
187 |         except Exception as e:
188 |             logger.error(f"Error creating document records: {str(e)}")
189 |             return []
190 |     
191 |     def process_text(self, text: str, source_id: str, metadata: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
192 |         """
193 |         Process a text string through the ingestion pipeline.
194 |         
195 |         Args:
196 |             text: Text content to process
197 |             source_id: Identifier for the source of the text
198 |             metadata: Optional metadata about the text
199 |             
200 |         Returns:
201 |             List of dictionaries containing the processed chunks with their IDs
202 |         """
203 |         if not text or not text.strip():
204 |             logger.warning("Empty text provided to process_text")
205 |             return []
206 |             
207 |         if metadata is None:
208 |             metadata = {}
209 |         
210 |         # Add source information to metadata
211 |         metadata.update({
212 |             "source_type": "text",
213 |             "source_id": source_id,
214 |             "processed_at": datetime.now().isoformat()
215 |         })
216 |         
217 |         try:
218 |             # Generate chunks
219 |             chunks = self.chunker.chunk_text(text)
220 |             chunks = [chunk for chunk in chunks if chunk and chunk.strip()]
221 |             
222 |             if not chunks:
223 |                 logger.warning("No valid chunks generated from text")
224 |                 return []
225 |                 
226 |             logger.info(f"Generated {len(chunks)} chunks from text")
227 |             
228 |             # Generate embeddings
229 |             embeddings = self.embedding_generator.embed_batch(chunks)
230 |             
231 |             # Create document records
232 |             document_id = str(uuid.uuid4())
233 |             
234 |             # Create records and store in database
235 |             records = []
236 |             stored_records = []
237 |             
238 |             # Create a URL/identifier for the text
239 |             url = f"text://{source_id}"
240 |             
241 |             for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
242 |                 # Create record for return value
243 |                 record = {
244 |                     "id": f"{document_id}_{i}",
245 |                     "document_id": document_id,
246 |                     "chunk_index": i,
247 |                     "text": chunk,
248 |                     "embedding": embedding,
249 |                     "metadata": metadata.copy()
250 |                 }
251 |                 records.append(record)
252 |                 
253 |                 # Store in Supabase
254 |                 try:
255 |                     stored_record = self.supabase_client.store_document_chunk(
256 |                         url=url,
257 |                         chunk_number=i,
258 |                         content=chunk,
259 |                         embedding=embedding,
260 |                         metadata=metadata.copy()
261 |                     )
262 |                     stored_records.append(stored_record)
263 |                 except Exception as e:
264 |                     logger.error(f"Error storing text chunk {i} in database: {str(e)}")
265 |             
266 |             logger.info(f"Created {len(records)} records from text input")
267 |             logger.info(f"Stored {len(stored_records)} text chunks in database")
268 |             return records
269 |             
270 |         except Exception as e:
271 |             logger.error(f"Error processing text: {str(e)}")
272 |             return []
273 |     
274 |     def process_batch(self, file_paths: List[str], metadata: Optional[Dict[str, Any]] = None) -> Dict[str, List[Dict[str, Any]]]:
275 |         """
276 |         Process a batch of files through the ingestion pipeline.
277 |         
278 |         Args:
279 |             file_paths: List of paths to document files
280 |             metadata: Optional shared metadata for all files
281 |             
282 |         Returns:
283 |             Dictionary mapping file paths to their processed chunks
284 |         """
285 |         results = {}
286 |         
287 |         for file_path in file_paths:
288 |             try:
289 |                 # Create file-specific metadata
290 |                 file_metadata = metadata.copy() if metadata else {}
291 |                 file_metadata["batch_processed"] = True
292 |                 
293 |                 # Process the file
294 |                 file_results = self.process_file(file_path, file_metadata)
295 |                 results[file_path] = file_results
296 |                 
297 |                 logger.info(f"Processed {file_path} with {len(file_results)} chunks")
298 |                 
299 |             except Exception as e:
300 |                 logger.error(f"Error processing {file_path}: {str(e)}")
301 |                 results[file_path] = []
302 |         
303 |         return results
304 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/document_processing/processors.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Document processors for extracting text from various file types.
  3 | """
  4 | import os
  5 | import logging
  6 | from typing import Dict, Any, Optional, List
  7 | from pathlib import Path
  8 | import PyPDF2
  9 | 
 10 | # Set up logging
 11 | logger = logging.getLogger(__name__)
 12 | 
 13 | class DocumentProcessor:
 14 |     """
 15 |     Base class for document processors.
 16 |     """
 17 |     
 18 |     def extract_text(self, file_path: str) -> str:
 19 |         """
 20 |         Extract text content from a document file.
 21 |         
 22 |         Args:
 23 |             file_path: Path to the document file
 24 |             
 25 |         Returns:
 26 |             Extracted text content as a string
 27 |         """
 28 |         raise NotImplementedError("Subclasses must implement extract_text method")
 29 |     
 30 |     def get_metadata(self, file_path: str) -> Dict[str, Any]:
 31 |         """
 32 |         Extract metadata from a document file.
 33 |         
 34 |         Args:
 35 |             file_path: Path to the document file
 36 |             
 37 |         Returns:
 38 |             Dictionary containing document metadata
 39 |         """
 40 |         # Basic metadata common to all file types
 41 |         path = Path(file_path)
 42 |         return {
 43 |             "filename": path.name,
 44 |             "file_extension": path.suffix.lower(),
 45 |             "file_size_bytes": path.stat().st_size,
 46 |             "created_at": path.stat().st_ctime,
 47 |             "modified_at": path.stat().st_mtime
 48 |         }
 49 | 
 50 | 
 51 | class TxtProcessor(DocumentProcessor):
 52 |     """
 53 |     Processor for plain text files with robust error handling.
 54 |     """
 55 |     
 56 |     def extract_text(self, file_path: str) -> str:
 57 |         """
 58 |         Extract text from a TXT file with encoding fallbacks.
 59 |         
 60 |         Args:
 61 |             file_path: Path to the TXT file
 62 |             
 63 |         Returns:
 64 |             Extracted text content
 65 |         """
 66 |         path = Path(file_path)
 67 |         
 68 |         # Validate file exists
 69 |         if not path.exists():
 70 |             raise FileNotFoundError(f"File not found: {file_path}")
 71 |         
 72 |         # Try different encodings if UTF-8 fails
 73 |         encodings = ["utf-8", "latin-1", "cp1252", "ascii"]
 74 |         content = ""
 75 |         
 76 |         for encoding in encodings:
 77 |             try:
 78 |                 with open(file_path, "r", encoding=encoding) as file:
 79 |                     content = file.read()
 80 |                 logger.info(f"Successfully read text file with {encoding} encoding")
 81 |                 break
 82 |             except UnicodeDecodeError:
 83 |                 logger.warning(f"Failed to decode with {encoding}, trying next encoding")
 84 |             except Exception as e:
 85 |                 logger.error(f"Error reading file with {encoding}: {str(e)}")
 86 |                 raise
 87 |         
 88 |         if not content:
 89 |             raise ValueError(f"Could not decode file with any of the attempted encodings")
 90 |             
 91 |         return content
 92 |     
 93 |     def get_metadata(self, file_path: str) -> Dict[str, Any]:
 94 |         """
 95 |         Get metadata for a TXT file.
 96 |         
 97 |         Args:
 98 |             file_path: Path to the TXT file
 99 |             
100 |         Returns:
101 |             Dictionary containing document metadata
102 |         """
103 |         metadata = super().get_metadata(file_path)
104 |         metadata["content_type"] = "text/plain"
105 |         metadata["processor"] = "TxtProcessor"
106 |         
107 |         # Count lines and words
108 |         try:
109 |             text = self.extract_text(file_path)
110 |             metadata["line_count"] = len(text.splitlines())
111 |             metadata["word_count"] = len(text.split())
112 |         except Exception:
113 |             # Don't fail metadata collection if text extraction fails
114 |             pass
115 |             
116 |         return metadata
117 | 
118 | 
119 | class PdfProcessor(DocumentProcessor):
120 |     """
121 |     Processor for PDF files with improved text extraction.
122 |     """
123 |     
124 |     def extract_text(self, file_path: str) -> str:
125 |         """
126 |         Extract text from a PDF file with page tracking.
127 |         
128 |         Args:
129 |             file_path: Path to the PDF file
130 |             
131 |         Returns:
132 |             Extracted text content
133 |         """
134 |         path = Path(file_path)
135 |         
136 |         # Validate file exists
137 |         if not path.exists():
138 |             raise FileNotFoundError(f"File not found: {file_path}")
139 |         
140 |         try:
141 |             with open(file_path, "rb") as file:
142 |                 reader = PyPDF2.PdfReader(file)
143 |                 
144 |                 # Extract text from all pages with page numbers
145 |                 content = []
146 |                 total_pages = len(reader.pages)
147 |                 
148 |                 for page_num in range(total_pages):
149 |                     try:
150 |                         page = reader.pages[page_num]
151 |                         page_text = page.extract_text()
152 |                         
153 |                         # Add page marker and text
154 |                         if page_text and page_text.strip():
155 |                             content.append(f"[Page {page_num + 1} of {total_pages}]\n{page_text}\n")
156 |                     except Exception as e:
157 |                         logger.warning(f"Error extracting text from page {page_num + 1}: {str(e)}")
158 |                         content.append(f"[Page {page_num + 1} of {total_pages} - Text extraction failed]\n")
159 |                 
160 |                 return "\n".join(content)
161 |                 
162 |         except Exception as e:
163 |             logger.error(f"Error processing PDF file: {str(e)}")
164 |             raise
165 |     
166 |     def get_metadata(self, file_path: str) -> Dict[str, Any]:
167 |         """
168 |         Get metadata for a PDF file including PDF-specific properties.
169 |         
170 |         Args:
171 |             file_path: Path to the PDF file
172 |             
173 |         Returns:
174 |             Dictionary containing document metadata
175 |         """
176 |         metadata = super().get_metadata(file_path)
177 |         metadata["content_type"] = "application/pdf"
178 |         metadata["processor"] = "PdfProcessor"
179 |         
180 |         # Extract PDF-specific metadata
181 |         try:
182 |             with open(file_path, "rb") as file:
183 |                 reader = PyPDF2.PdfReader(file)
184 |                 
185 |                 # Basic PDF properties
186 |                 metadata["page_count"] = len(reader.pages)
187 |                 
188 |                 # PDF document info if available
189 |                 if reader.metadata:
190 |                     pdf_info = reader.metadata
191 |                     if pdf_info.title:
192 |                         metadata["title"] = pdf_info.title
193 |                     if pdf_info.author:
194 |                         metadata["author"] = pdf_info.author
195 |                     if pdf_info.subject:
196 |                         metadata["subject"] = pdf_info.subject
197 |                     if pdf_info.creator:
198 |                         metadata["creator"] = pdf_info.creator
199 |                     if pdf_info.producer:
200 |                         metadata["producer"] = pdf_info.producer
201 |         except Exception as e:
202 |             logger.warning(f"Error extracting PDF metadata: {str(e)}")
203 |             
204 |         return metadata
205 | 
206 | 
207 | def get_document_processor(file_path: str) -> Optional[DocumentProcessor]:
208 |     """
209 |     Get the appropriate processor for a file based on its extension.
210 |     
211 |     Args:
212 |         file_path: Path to the document file
213 |         
214 |     Returns:
215 |         DocumentProcessor instance for the file type or None if unsupported
216 |     """
217 |     path = Path(file_path)
218 |     extension = path.suffix.lower()
219 |     
220 |     processors = {
221 |         ".txt": TxtProcessor(),
222 |         ".pdf": PdfProcessor(),
223 |         # Add more processors here as needed
224 |     }
225 |     
226 |     processor = processors.get(extension)
227 |     
228 |     if processor:
229 |         logger.info(f"Using {processor.__class__.__name__} for {path.name}")
230 |         return processor
231 |     else:
232 |         logger.warning(f"Unsupported file type: {extension}")
233 |         return None
234 | 
235 | 
236 | def get_supported_extensions() -> List[str]:
237 |     """
238 |     Get a list of supported file extensions.
239 |     
240 |     Returns:
241 |         List of supported file extensions
242 |     """
243 |     return [".txt", ".pdf"]
244 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/prompt.txt:
--------------------------------------------------------------------------------
 1 | I'd like to build a RAG AI agent with Pydantic AI and Supabase, using the following MCP servers:
 2 | 
 3 | Be sure to review the planning and task files.
 4 | This project should create a simple RAG system with:
 5 | 
 6 | A document ingestion pipeline that:
 7 | 
 8 | Accepts local TXT and PDF files
 9 | Uses a simple chunking approach
10 | Generates embeddings using OpenAI
11 | Stores documents and vectors in Supabase with pgvector
12 | 
13 | 
14 | A Pydantic AI agent that:
15 | 
16 | Has a tool for knowledge base search
17 | Uses OpenAI models for response generation
18 | Integrates retrieved contexts into responses
19 | 
20 | 
21 | A Streamlit UI that:
22 | 
23 | Allows document uploads
24 | Provides a clean interface for querying the agent
25 | Displays responses with source attribution
26 | Use @streamlit_ui_example.py to see exactly how to integrate Streamlit with a Pydantic AI agent.
27 | 
28 | 
29 | Use the Supabase MCP server to create the necessary database tables with the pgvector extension enabled. For document processing, keep it simple using PyPDF2 for PDFs rather than complex document processing libraries.
30 | 
31 | Use the Crawl4AI RAG MCP server that already has the Pydantic AI and Supabase Python documentation available. So just perform RAG queries whenever necessary. Also use the Brave MCP server to search the web for supplemental docs/examples to aid in creating the agent.


--------------------------------------------------------------------------------
/foundational-rag-agent/rag-example.sql:
--------------------------------------------------------------------------------
 1 | -- Enable the pgvector extension
 2 | create extension if not exists vector;
 3 | 
 4 | -- Create the documentation chunks table
 5 | create table rag_pages (
 6 |     id bigserial primary key,
 7 |     url varchar not null,
 8 |     chunk_number integer not null,
 9 |     content text not null,  -- Added content column
10 |     metadata jsonb not null default '{}'::jsonb,  -- Added metadata column
11 |     embedding vector(1536),  -- OpenAI embeddings are 1536 dimensions
12 |     created_at timestamp with time zone default timezone('utc'::text, now()) not null,
13 |     
14 |     -- Add a unique constraint to prevent duplicate chunks for the same URL
15 |     unique(url, chunk_number)
16 | );
17 | 
18 | -- Create an index for better vector similarity search performance
19 | create index on rag_pages using ivfflat (embedding vector_cosine_ops);
20 | 
21 | -- Create an index on metadata for faster filtering
22 | create index idx_rag_pages_metadata on rag_pages using gin (metadata);
23 | 
24 | CREATE INDEX idx_rag_pages_source ON rag_pages ((metadata->>'source'));
25 | 
26 | -- Create a function to search for documentation chunks
27 | create or replace function match_rag_pages (
28 |   query_embedding vector(1536),
29 |   match_count int default 10,
30 |   filter jsonb DEFAULT '{}'::jsonb
31 | ) returns table (
32 |   id bigint,
33 |   url varchar,
34 |   chunk_number integer,
35 |   content text,
36 |   metadata jsonb,
37 |   similarity float
38 | )
39 | language plpgsql
40 | as $
41 | #variable_conflict use_column
42 | begin
43 |   return query
44 |   select
45 |     id,
46 |     url,
47 |     chunk_number,
48 |     content,
49 |     metadata,
50 |     1 - (rag_pages.embedding <=> query_embedding) as similarity
51 |   from rag_pages
52 |   where metadata @> filter
53 |   order by rag_pages.embedding <=> query_embedding
54 |   limit match_count;
55 | end;
56 | $;
57 | 
58 | -- Enable RLS on the table
59 | alter table rag_pages enable row level security;
60 | 
61 | -- Create a policy that allows anyone to read
62 | create policy "Allow public read access"
63 |   on rag_pages
64 |   for select
65 |   to public
66 |   using (true);


--------------------------------------------------------------------------------
/foundational-rag-agent/requirements.txt:
--------------------------------------------------------------------------------
 1 | pydantic-ai>=0.1.12
 2 | supabase>=2.0.0
 3 | openai>=1.0.0
 4 | PyPDF2>=3.0.0
 5 | streamlit>=1.30.0
 6 | python-dotenv>=1.0.0
 7 | numpy>=1.24.0
 8 | pytest>=7.0.0
 9 | pytest-asyncio>=0.21.0
10 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/streamlit_ui_example.py:
--------------------------------------------------------------------------------
 1 | from pydantic_ai import Agent
 2 | from httpx import AsyncClient
 3 | import streamlit as st
 4 | import asyncio
 5 | import sys
 6 | import os
 7 | 
 8 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 9 | from Basic_Pydantic_AI_Agent.src import agent, AgentDeps
10 | 
11 | # Import all the message part classes from Pydantic AI
12 | from pydantic_ai.messages import ModelRequest, ModelResponse, PartDeltaEvent, PartStartEvent, TextPartDelta
13 | 
14 | def display_message_part(part):
15 |     """
16 |     Display a single part of a message in the Streamlit UI.
17 |     Customize how you display system prompts, user prompts,
18 |     tool calls, tool returns, etc.
19 |     """
20 |     # User messages
21 |     if part.part_kind == 'user-prompt' and part.content:
22 |         with st.chat_message("user"):
23 |             st.markdown(part.content)
24 |     # AI messages
25 |     elif part.part_kind == 'text' and part.content:
26 |         with st.chat_message("assistant"):
27 |             st.markdown(part.content)             
28 | 
29 | async def run_agent_with_streaming(user_input):
30 |     async with AsyncClient() as http_client:
31 |         agent_deps = AgentDeps(
32 |             http_client=http_client,
33 |             brave_api_key=os.getenv("BRAVE_API_KEY", ""),
34 |             searxng_base_url=os.getenv("SEARXNG_BASE_URL", "")
35 |         )   
36 | 
37 |         async with agent.iter(user_input, deps=agent_deps, message_history=st.session_state.messages) as run:
38 |             async for node in run:
39 |                 if Agent.is_model_request_node(node):
40 |                     # A model request node => We can stream tokens from the model's request
41 |                     async with node.stream(run.ctx) as request_stream:
42 |                         async for event in request_stream:
43 |                             if isinstance(event, PartStartEvent) and event.part.part_kind == 'text':
44 |                                     yield event.part.content
45 |                             elif isinstance(event, PartDeltaEvent) and isinstance(event.delta, TextPartDelta):
46 |                                     delta = event.delta.content_delta
47 |                                     yield delta         
48 | 
49 |     # Add the new messages to the chat history (including tool calls and responses)
50 |     st.session_state.messages.extend(run.result.new_messages())       
51 | 
52 | 
53 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
54 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
55 | # ~~~~~~~~~~~~~~~~~~ Main Function with UI Creation ~~~~~~~~~~~~~~~~~~~~
56 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
57 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
58 | 
59 | async def main():
60 |     st.title("Pydantic AI Agent")
61 |     
62 |     # Initialize chat history in session state if not present
63 |     if "messages" not in st.session_state:
64 |         st.session_state.messages = []
65 | 
66 |     # Display all messages from the conversation so far
67 |     # Each message is either a ModelRequest or ModelResponse.
68 |     # We iterate over their parts to decide how to display them.
69 |     for msg in st.session_state.messages:
70 |         if isinstance(msg, ModelRequest) or isinstance(msg, ModelResponse):
71 |             for part in msg.parts:
72 |                 display_message_part(part)
73 | 
74 |     # Chat input for the user
75 |     user_input = st.chat_input("What do you want to do today?")
76 | 
77 |     if user_input:
78 |         # Display user prompt in the UI
79 |         with st.chat_message("user"):
80 |             st.markdown(user_input)
81 | 
82 |         # Display the assistant's partial response while streaming
83 |         with st.chat_message("assistant"):
84 |             # Create a placeholder for the streaming text
85 |             message_placeholder = st.empty()
86 |             full_response = ""
87 |             
88 |             # Properly consume the async generator with async for
89 |             generator = run_agent_with_streaming(user_input)
90 |             async for message in generator:
91 |                 full_response += message
92 |                 message_placeholder.markdown(full_response + "▌")
93 |             
94 |             # Final response without the cursor
95 |             message_placeholder.markdown(full_response)
96 | 
97 | 
98 | if __name__ == "__main__":
99 |     asyncio.run(main())


--------------------------------------------------------------------------------
/foundational-rag-agent/tests/test_agent.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Unit tests for the RAG agent module.
  3 | """
  4 | import os
  5 | import sys
  6 | import pytest
  7 | from unittest.mock import MagicMock, patch
  8 | from typing import List, Dict, Any
  9 | 
 10 | # Add parent directory to path to allow relative imports
 11 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 12 | 
 13 | from agent.agent import RAGAgent
 14 | from agent.tools import KnowledgeBaseSearchResult
 15 | 
 16 | 
 17 | class TestRAGAgent:
 18 |     """
 19 |     Test cases for the RAGAgent class.
 20 |     """
 21 |     
 22 |     @pytest.mark.asyncio
 23 |     async def test_query_with_results(self):
 24 |         """
 25 |         Test that the agent query returns results when documents are found.
 26 |         """
 27 |         # Mock the Pydantic AI Agent and KnowledgeBaseSearch
 28 |         mock_agent = MagicMock()
 29 |         mock_kb_search = MagicMock()
 30 |         
 31 |         # Set up mock return values for the agent
 32 |         mock_result = MagicMock()
 33 |         mock_result.output = "This is the agent's response based on the knowledge base."
 34 |         mock_result.tool_calls = [MagicMock()]
 35 |         mock_result.tool_calls[0].tool.name = "search"
 36 |         
 37 |         # Create mock search results
 38 |         mock_search_results = [
 39 |             KnowledgeBaseSearchResult(
 40 |                 content="This is test content 1.",
 41 |                 source="test1.txt",
 42 |                 source_type="txt",
 43 |                 similarity=0.95,
 44 |                 metadata={"source": "test1.txt", "source_type": "txt"}
 45 |             ),
 46 |             KnowledgeBaseSearchResult(
 47 |                 content="This is test content 2.",
 48 |                 source="test2.txt",
 49 |                 source_type="txt",
 50 |                 similarity=0.85,
 51 |                 metadata={"source": "test2.txt", "source_type": "txt"}
 52 |             )
 53 |         ]
 54 |         mock_result.tool_calls[0].result = mock_search_results
 55 |         
 56 |         # Set the agent's run method to return the mock result
 57 |         mock_agent.run.return_value = mock_result
 58 |         
 59 |         # Create the RAGAgent with mocks
 60 |         with patch('agent.agent.Agent', return_value=mock_agent):
 61 |             rag_agent = RAGAgent(
 62 |                 model="gpt-4.1-mini",
 63 |                 api_key="test_api_key",
 64 |                 kb_search=mock_kb_search
 65 |             )
 66 |             
 67 |             # Call the query method
 68 |             result = await rag_agent.query("What is the test content?")
 69 |             
 70 |             # Check that the agent was called correctly
 71 |             mock_agent.run.assert_called_once()
 72 |             
 73 |             # Check the result
 74 |             assert result["response"] == "This is the agent's response based on the knowledge base."
 75 |             assert len(result["kb_results"]) == 2
 76 |             assert result["kb_results"][0].content == "This is test content 1."
 77 |             assert result["kb_results"][1].content == "This is test content 2."
 78 |     
 79 |     @pytest.mark.asyncio
 80 |     async def test_query_no_kb_results(self):
 81 |         """
 82 |         Test that the agent query works when no knowledge base results are found.
 83 |         """
 84 |         # Mock the Pydantic AI Agent and KnowledgeBaseSearch
 85 |         mock_agent = MagicMock()
 86 |         mock_kb_search = MagicMock()
 87 |         
 88 |         # Set up mock return values for the agent
 89 |         mock_result = MagicMock()
 90 |         mock_result.output = "I don't have specific information about that in my knowledge base."
 91 |         mock_result.tool_calls = [MagicMock()]
 92 |         mock_result.tool_calls[0].tool.name = "search"
 93 |         mock_result.tool_calls[0].result = []  # Empty results
 94 |         
 95 |         # Set the agent's run method to return the mock result
 96 |         mock_agent.run.return_value = mock_result
 97 |         
 98 |         # Create the RAGAgent with mocks
 99 |         with patch('agent.agent.Agent', return_value=mock_agent):
100 |             rag_agent = RAGAgent(
101 |                 model="gpt-4.1-mini",
102 |                 api_key="test_api_key",
103 |                 kb_search=mock_kb_search
104 |             )
105 |             
106 |             # Call the query method
107 |             result = await rag_agent.query("What is something not in the knowledge base?")
108 |             
109 |             # Check that the agent was called correctly
110 |             mock_agent.run.assert_called_once()
111 |             
112 |             # Check the result
113 |             assert result["response"] == "I don't have specific information about that in my knowledge base."
114 |             assert len(result["kb_results"]) == 0
115 |     
116 |     @pytest.mark.asyncio
117 |     async def test_get_available_sources(self):
118 |         """
119 |         Test that get_available_sources returns the list of sources.
120 |         """
121 |         # Mock the KnowledgeBaseSearch
122 |         mock_kb_search = MagicMock()
123 |         
124 |         # Set up mock return values
125 |         mock_sources = ["test1.txt", "test2.pdf", "test3.txt"]
126 |         mock_kb_search.get_available_sources.return_value = mock_sources
127 |         
128 |         # Create the RAGAgent with mock
129 |         with patch('agent.agent.Agent'):
130 |             rag_agent = RAGAgent(
131 |                 model="gpt-4.1-mini",
132 |                 api_key="test_api_key",
133 |                 kb_search=mock_kb_search
134 |             )
135 |             
136 |             # Call the get_available_sources method
137 |             sources = await rag_agent.get_available_sources()
138 |             
139 |             # Check that the mock was called correctly
140 |             mock_kb_search.get_available_sources.assert_called_once()
141 |             
142 |             # Check the results
143 |             assert sources == mock_sources
144 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/tests/test_agent_tools.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Unit tests for the agent tools module.
  3 | """
  4 | import os
  5 | import sys
  6 | import pytest
  7 | import asyncio
  8 | from unittest.mock import MagicMock, patch
  9 | from typing import List, Dict, Any
 10 | 
 11 | # Add parent directory to path to allow relative imports
 12 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 13 | 
 14 | from agent.tools import KnowledgeBaseSearch, KnowledgeBaseSearchParams, KnowledgeBaseSearchResult
 15 | 
 16 | 
 17 | class TestKnowledgeBaseSearch:
 18 |     """
 19 |     Test cases for the KnowledgeBaseSearch class.
 20 |     """
 21 |     
 22 |     @pytest.mark.asyncio
 23 |     async def test_search_with_results(self):
 24 |         """
 25 |         Test that search returns results when documents are found.
 26 |         """
 27 |         # Mock the SupabaseClient and EmbeddingGenerator
 28 |         mock_supabase = MagicMock()
 29 |         mock_embedding_generator = MagicMock()
 30 |         
 31 |         # Set up mock return values
 32 |         mock_embedding = [0.1] * 1536  # Mock embedding vector
 33 |         mock_embedding_generator.embed_text.return_value = mock_embedding
 34 |         
 35 |         mock_search_results = [
 36 |             {
 37 |                 "id": 1,
 38 |                 "url": "local://test1.txt",
 39 |                 "chunk_number": 0,
 40 |                 "content": "This is test content 1.",
 41 |                 "metadata": {
 42 |                     "source": "test1.txt",
 43 |                     "source_type": "txt"
 44 |                 },
 45 |                 "similarity": 0.95
 46 |             },
 47 |             {
 48 |                 "id": 2,
 49 |                 "url": "local://test2.txt",
 50 |                 "chunk_number": 1,
 51 |                 "content": "This is test content 2.",
 52 |                 "metadata": {
 53 |                     "source": "test2.txt",
 54 |                     "source_type": "txt"
 55 |                 },
 56 |                 "similarity": 0.85
 57 |             }
 58 |         ]
 59 |         mock_supabase.search_documents.return_value = mock_search_results
 60 |         
 61 |         # Create the KnowledgeBaseSearch instance with mocks
 62 |         kb_search = KnowledgeBaseSearch(
 63 |             supabase_client=mock_supabase,
 64 |             embedding_generator=mock_embedding_generator
 65 |         )
 66 |         
 67 |         # Create search parameters
 68 |         params = KnowledgeBaseSearchParams(
 69 |             query="test query",
 70 |             max_results=2
 71 |         )
 72 |         
 73 |         # Call the search method
 74 |         results = await kb_search.search(params)
 75 |         
 76 |         # Check that the mocks were called correctly
 77 |         mock_embedding_generator.embed_text.assert_called_once_with("test query")
 78 |         mock_supabase.search_documents.assert_called_once_with(
 79 |             query_embedding=mock_embedding,
 80 |             match_count=2,
 81 |             filter_metadata=None
 82 |         )
 83 |         
 84 |         # Check the results
 85 |         assert len(results) == 2
 86 |         assert isinstance(results[0], KnowledgeBaseSearchResult)
 87 |         assert results[0].content == "This is test content 1."
 88 |         assert results[0].source == "test1.txt"
 89 |         assert results[0].source_type == "txt"
 90 |         assert results[0].similarity == 0.95
 91 |         
 92 |         assert results[1].content == "This is test content 2."
 93 |         assert results[1].source == "test2.txt"
 94 |         assert results[1].source_type == "txt"
 95 |         assert results[1].similarity == 0.85
 96 |     
 97 |     @pytest.mark.asyncio
 98 |     async def test_search_with_source_filter(self):
 99 |         """
100 |         Test that search applies source filter correctly.
101 |         """
102 |         # Mock the SupabaseClient and EmbeddingGenerator
103 |         mock_supabase = MagicMock()
104 |         mock_embedding_generator = MagicMock()
105 |         
106 |         # Set up mock return values
107 |         mock_embedding = [0.1] * 1536  # Mock embedding vector
108 |         mock_embedding_generator.embed_text.return_value = mock_embedding
109 |         
110 |         mock_search_results = [
111 |             {
112 |                 "id": 1,
113 |                 "url": "local://test1.txt",
114 |                 "chunk_number": 0,
115 |                 "content": "This is test content 1.",
116 |                 "metadata": {
117 |                     "source": "test1.txt",
118 |                     "source_type": "txt"
119 |                 },
120 |                 "similarity": 0.95
121 |             }
122 |         ]
123 |         mock_supabase.search_documents.return_value = mock_search_results
124 |         
125 |         # Create the KnowledgeBaseSearch instance with mocks
126 |         kb_search = KnowledgeBaseSearch(
127 |             supabase_client=mock_supabase,
128 |             embedding_generator=mock_embedding_generator
129 |         )
130 |         
131 |         # Create search parameters with source filter
132 |         params = KnowledgeBaseSearchParams(
133 |             query="test query",
134 |             max_results=5,
135 |             source_filter="test1.txt"
136 |         )
137 |         
138 |         # Call the search method
139 |         results = await kb_search.search(params)
140 |         
141 |         # Check that the mocks were called correctly
142 |         mock_embedding_generator.embed_text.assert_called_once_with("test query")
143 |         mock_supabase.search_documents.assert_called_once_with(
144 |             query_embedding=mock_embedding,
145 |             match_count=5,
146 |             filter_metadata={"source": "test1.txt"}
147 |         )
148 |         
149 |         # Check the results
150 |         assert len(results) == 1
151 |         assert results[0].source == "test1.txt"
152 |     
153 |     @pytest.mark.asyncio
154 |     async def test_search_no_results(self):
155 |         """
156 |         Test that search returns empty list when no documents are found.
157 |         """
158 |         # Mock the SupabaseClient and EmbeddingGenerator
159 |         mock_supabase = MagicMock()
160 |         mock_embedding_generator = MagicMock()
161 |         
162 |         # Set up mock return values
163 |         mock_embedding = [0.1] * 1536  # Mock embedding vector
164 |         mock_embedding_generator.embed_text.return_value = mock_embedding
165 |         
166 |         # Return empty results
167 |         mock_supabase.search_documents.return_value = []
168 |         
169 |         # Create the KnowledgeBaseSearch instance with mocks
170 |         kb_search = KnowledgeBaseSearch(
171 |             supabase_client=mock_supabase,
172 |             embedding_generator=mock_embedding_generator
173 |         )
174 |         
175 |         # Create search parameters
176 |         params = KnowledgeBaseSearchParams(
177 |             query="test query",
178 |             max_results=5
179 |         )
180 |         
181 |         # Call the search method
182 |         results = await kb_search.search(params)
183 |         
184 |         # Check the results
185 |         assert len(results) == 0
186 |     
187 |     @pytest.mark.asyncio
188 |     async def test_get_available_sources(self):
189 |         """
190 |         Test that get_available_sources returns the list of sources.
191 |         """
192 |         # Mock the SupabaseClient
193 |         mock_supabase = MagicMock()
194 |         
195 |         # Set up mock return values
196 |         mock_sources = ["test1.txt", "test2.pdf", "test3.txt"]
197 |         mock_supabase.get_all_document_sources.return_value = mock_sources
198 |         
199 |         # Create the KnowledgeBaseSearch instance with mock
200 |         kb_search = KnowledgeBaseSearch(supabase_client=mock_supabase)
201 |         
202 |         # Call the get_available_sources method
203 |         sources = await kb_search.get_available_sources()
204 |         
205 |         # Check that the mock was called correctly
206 |         mock_supabase.get_all_document_sources.assert_called_once()
207 |         
208 |         # Check the results
209 |         assert sources == mock_sources
210 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/tests/test_chunker.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Unit tests for the text chunker module.
  3 | """
  4 | import os
  5 | import sys
  6 | import pytest
  7 | from pathlib import Path
  8 | 
  9 | # Add parent directory to path to allow relative imports
 10 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 11 | 
 12 | from document_processing.chunker import TextChunker
 13 | 
 14 | 
 15 | class TestTextChunker:
 16 |     """
 17 |     Test cases for the TextChunker class.
 18 |     """
 19 |     
 20 |     def test_init_with_default_values(self):
 21 |         """
 22 |         Test that TextChunker initializes with default values.
 23 |         """
 24 |         chunker = TextChunker()
 25 |         assert chunker.chunk_size == 1000
 26 |         assert chunker.chunk_overlap == 200
 27 |     
 28 |     def test_init_with_custom_values(self):
 29 |         """
 30 |         Test that TextChunker initializes with custom values.
 31 |         """
 32 |         chunker = TextChunker(chunk_size=500, chunk_overlap=100)
 33 |         assert chunker.chunk_size == 500
 34 |         assert chunker.chunk_overlap == 100
 35 |     
 36 |     def test_init_with_large_overlap(self):
 37 |         """
 38 |         Test that TextChunker adjusts overlap when it's too large.
 39 |         """
 40 |         # In our new implementation, we automatically adjust the overlap
 41 |         # to be at most half of the chunk size
 42 |         chunker = TextChunker(chunk_size=500, chunk_overlap=500)
 43 |         assert chunker.chunk_overlap == 250  # Should be adjusted to chunk_size // 2
 44 |         
 45 |         chunker = TextChunker(chunk_size=500, chunk_overlap=600)
 46 |         assert chunker.chunk_overlap == 250  # Should be adjusted to chunk_size // 2
 47 |     
 48 |     def test_chunk_text_short_text(self):
 49 |         """
 50 |         Test chunking text that is shorter than chunk_size.
 51 |         """
 52 |         chunker = TextChunker(chunk_size=1000, chunk_overlap=200)
 53 |         text = "This is a short text."
 54 |         chunks = chunker.chunk_text(text)
 55 |         
 56 |         assert len(chunks) == 1
 57 |         assert chunks[0] == text
 58 |     
 59 |     def test_chunk_text_long_text(self):
 60 |         """
 61 |         Test chunking text that is longer than chunk_size.
 62 |         """
 63 |         chunker = TextChunker(chunk_size=100, chunk_overlap=20)
 64 |         text = "This is a longer text that should be split into multiple chunks. " * 5
 65 |         chunks = chunker.chunk_text(text)
 66 |         
 67 |         assert len(chunks) > 1
 68 |         
 69 |         # Check that the chunks cover the entire text
 70 |         reconstructed = ""
 71 |         for i, chunk in enumerate(chunks):
 72 |             if i == 0:
 73 |                 reconstructed += chunk
 74 |             else:
 75 |                 # Account for overlap
 76 |                 overlap_start = len(reconstructed) - chunker.chunk_overlap
 77 |                 if overlap_start > 0:
 78 |                     reconstructed = reconstructed[:overlap_start] + chunk
 79 |                 else:
 80 |                     reconstructed += chunk
 81 |         
 82 |         # The reconstructed text might be slightly different due to splitting at sentence boundaries
 83 |         assert len(reconstructed) >= len(text) * 0.9
 84 |     
 85 |     def test_chunk_by_separator(self):
 86 |         """
 87 |         Test splitting text by a separator.
 88 |         """
 89 |         chunker = TextChunker(chunk_size=100, chunk_overlap=20)
 90 |         paragraphs = [
 91 |             "This is the first paragraph.",
 92 |             "This is the second paragraph.",
 93 |             "This is the third paragraph.",
 94 |             "This is the fourth paragraph."
 95 |         ]
 96 |         text = "\n\n".join(paragraphs)
 97 |         
 98 |         chunks = chunker.chunk_by_separator(text, separator="\n\n")
 99 |         
100 |         assert len(chunks) == 4
101 |         for i, paragraph in enumerate(paragraphs):
102 |             assert paragraph in chunks[i]
103 |     
104 |     def test_chunk_by_separator_large_paragraph(self):
105 |         """
106 |         Test splitting text by a separator with a paragraph larger than chunk_size.
107 |         """
108 |         chunker = TextChunker(chunk_size=50, chunk_overlap=10)
109 |         paragraphs = [
110 |             "This is a short paragraph.",
111 |             "This is a very long paragraph that exceeds the chunk size and should be split into multiple chunks.",
112 |             "This is another short paragraph."
113 |         ]
114 |         text = "\n\n".join(paragraphs)
115 |         
116 |         chunks = chunker.chunk_by_separator(text, separator="\n\n")
117 |         
118 |         assert len(chunks) > 3  # The long paragraph should be split
119 |         assert paragraphs[0] in chunks[0]
120 |         assert paragraphs[2] in chunks[-1]
121 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/tests/test_processors.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Unit tests for the document processors module.
  3 | """
  4 | import os
  5 | import sys
  6 | import pytest
  7 | from pathlib import Path
  8 | import tempfile
  9 | 
 10 | # Add parent directory to path to allow relative imports
 11 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 12 | 
 13 | from document_processing.processors import DocumentProcessor, TxtProcessor, PdfProcessor, get_document_processor
 14 | 
 15 | 
 16 | class TestDocumentProcessor:
 17 |     """
 18 |     Test cases for the DocumentProcessor base class.
 19 |     """
 20 |     
 21 |     def test_extract_text_not_implemented(self):
 22 |         """
 23 |         Test that the base DocumentProcessor raises NotImplementedError for extract_text.
 24 |         """
 25 |         processor = DocumentProcessor()
 26 |         with pytest.raises(NotImplementedError):
 27 |             processor.extract_text("dummy_path")
 28 |             
 29 |     def test_get_metadata_basic(self):
 30 |         """
 31 |         Test that the base DocumentProcessor provides basic metadata.
 32 |         """
 33 |         # Create a temporary file for testing
 34 |         with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
 35 |             temp_file.write(b"Test content")
 36 |             temp_file_path = temp_file.name
 37 |             
 38 |         try:
 39 |             processor = DocumentProcessor()
 40 |             metadata = processor.get_metadata(temp_file_path)
 41 |             
 42 |             # Check basic metadata fields
 43 |             assert "filename" in metadata
 44 |             assert "file_extension" in metadata
 45 |             assert "file_size_bytes" in metadata
 46 |             assert metadata["file_extension"] == ".txt"
 47 |         finally:
 48 |             # Clean up
 49 |             os.unlink(temp_file_path)
 50 | 
 51 | 
 52 | class TestTxtProcessor:
 53 |     """
 54 |     Test cases for the TxtProcessor class.
 55 |     """
 56 |     
 57 |     def test_extract_text_nonexistent_file(self):
 58 |         """
 59 |         Test that TxtProcessor raises FileNotFoundError for nonexistent files.
 60 |         """
 61 |         processor = TxtProcessor()
 62 |         with pytest.raises(FileNotFoundError):
 63 |             processor.extract_text("nonexistent_file.txt")
 64 |     
 65 |     def test_extract_text_valid_txt_file(self):
 66 |         """
 67 |         Test that TxtProcessor correctly extracts text from a valid TXT file.
 68 |         """
 69 |         # Create a temporary TXT file
 70 |         content = "This is a test document.\nIt has multiple lines.\nAnd some content to process."
 71 |         with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
 72 |             temp_file.write(content.encode("utf-8"))
 73 |             temp_file_path = temp_file.name
 74 |         
 75 |         try:
 76 |             processor = TxtProcessor()
 77 |             extracted_text = processor.extract_text(temp_file_path)
 78 |             
 79 |             # Check the extracted text
 80 |             assert extracted_text == content
 81 |         finally:
 82 |             # Clean up the temporary file
 83 |             os.unlink(temp_file_path)
 84 |     
 85 |     def test_get_metadata_txt_file(self):
 86 |         """
 87 |         Test that TxtProcessor correctly extracts metadata from a TXT file.
 88 |         """
 89 |         # Create a temporary TXT file
 90 |         content = "This is a test document.\nIt has multiple lines.\nAnd some content to process."
 91 |         with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
 92 |             temp_file.write(content.encode("utf-8"))
 93 |             temp_file_path = temp_file.name
 94 |         
 95 |         try:
 96 |             processor = TxtProcessor()
 97 |             metadata = processor.get_metadata(temp_file_path)
 98 |             
 99 |             # Check metadata fields
100 |             assert "filename" in metadata
101 |             assert "file_extension" in metadata
102 |             assert "file_size_bytes" in metadata
103 |             assert "content_type" in metadata
104 |             assert metadata["file_extension"] == ".txt"
105 |             assert metadata["content_type"] == "text/plain"
106 |             assert "processor" in metadata
107 |             assert metadata["processor"] == "TxtProcessor"
108 |         finally:
109 |             # Clean up the temporary file
110 |             os.unlink(temp_file_path)
111 | 
112 | 
113 | class TestPdfProcessor:
114 |     """
115 |     Test cases for the PdfProcessor class.
116 |     """
117 |     
118 |     def test_extract_text_nonexistent_file(self):
119 |         """
120 |         Test that PdfProcessor raises FileNotFoundError for nonexistent files.
121 |         """
122 |         processor = PdfProcessor()
123 |         with pytest.raises(FileNotFoundError):
124 |             processor.extract_text("nonexistent_file.pdf")
125 |     
126 |     def test_get_metadata_pdf_file(self):
127 |         """
128 |         Test that PdfProcessor correctly extracts metadata.
129 |         Note: This test doesn't use a real PDF file to avoid dependencies,
130 |         but just tests the error handling.
131 |         """
132 |         processor = PdfProcessor()
133 |         
134 |         # Since we can't easily create a valid PDF file in a test,
135 |         # we'll just test that the method handles errors gracefully
136 |         with pytest.raises(FileNotFoundError):
137 |             processor.get_metadata("nonexistent_file.pdf")
138 | 
139 | 
140 | class TestGetDocumentProcessor:
141 |     """
142 |     Test cases for the get_document_processor function.
143 |     """
144 |     
145 |     def test_get_document_processor_txt(self):
146 |         """
147 |         Test that get_document_processor returns a TxtProcessor for .txt files.
148 |         """
149 |         processor = get_document_processor("test.txt")
150 |         assert isinstance(processor, TxtProcessor)
151 |     
152 |     def test_get_document_processor_pdf(self):
153 |         """
154 |         Test that get_document_processor returns a PdfProcessor for .pdf files.
155 |         """
156 |         processor = get_document_processor("test.pdf")
157 |         assert isinstance(processor, PdfProcessor)
158 |     
159 |     def test_get_document_processor_unsupported(self):
160 |         """
161 |         Test that get_document_processor returns None for unsupported file types.
162 |         """
163 |         assert get_document_processor("test.docx") is None
164 |         assert get_document_processor("test.csv") is None
165 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/ui/app.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Streamlit application for the RAG AI agent.
  3 | """
  4 | import os
  5 | import sys
  6 | import asyncio
  7 | from typing import List, Dict, Any
  8 | import streamlit as st
  9 | from pathlib import Path
 10 | import tempfile
 11 | from datetime import datetime
 12 | 
 13 | # Add parent directory to path to allow relative imports
 14 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 15 | 
 16 | from document_processing.ingestion import DocumentIngestionPipeline
 17 | from document_processing.chunker import TextChunker
 18 | from document_processing.embeddings import EmbeddingGenerator
 19 | from database.setup import SupabaseClient
 20 | from agent.agent import RAGAgent, agent as rag_agent
 21 | from pydantic_ai.messages import ModelRequest, ModelResponse, PartDeltaEvent, PartStartEvent, TextPartDelta
 22 | 
 23 | # Set page configuration
 24 | st.set_page_config(
 25 |     page_title="RAG AI Agent",
 26 |     page_icon="🔍",
 27 |     layout="wide",
 28 |     initial_sidebar_state="expanded"
 29 | )
 30 | 
 31 | # Initialize database client
 32 | supabase_client = SupabaseClient()
 33 | 
 34 | # Initialize session state
 35 | if "messages" not in st.session_state:
 36 |     st.session_state.messages = []
 37 |     
 38 | if "sources" not in st.session_state:
 39 |     st.session_state.sources = []
 40 |     
 41 | if "document_count" not in st.session_state:
 42 |     # Initialize document count from database
 43 |     try:
 44 |         st.session_state.document_count = supabase_client.count_documents()
 45 |     except Exception as e:
 46 |         print(f"Error getting document count: {e}")
 47 |         st.session_state.document_count = 0
 48 |     
 49 | if "processed_files" not in st.session_state:
 50 |     st.session_state.processed_files = set()  # Track already processed files
 51 | 
 52 | 
 53 | def display_message_part(part):
 54 |     """
 55 |     Display a single part of a message in the Streamlit UI.
 56 |     
 57 |     Args:
 58 |         part: Message part to display
 59 |     """
 60 |     # User messages
 61 |     if part.part_kind == 'user-prompt' and part.content:
 62 |         with st.chat_message("user"):
 63 |             st.markdown(part.content)
 64 |     # AI messages
 65 |     elif part.part_kind == 'text' and part.content:
 66 |         with st.chat_message("assistant"):
 67 |             st.markdown(part.content)
 68 | 
 69 | 
 70 | async def process_document(file_path: str) -> Dict[str, Any]:
 71 |     """
 72 |     Process a document file and store it in the knowledge base.
 73 |     
 74 |     Args:
 75 |         file_path: Path to the document file
 76 |         
 77 |     Returns:
 78 |         Dictionary containing information about the processed document
 79 |     """
 80 |     # Create document ingestion pipeline with default settings
 81 |     # The pipeline now handles chunking and embedding internally
 82 |     pipeline = DocumentIngestionPipeline()
 83 |     
 84 |     # Process the file
 85 |     try:
 86 |         # Add file-specific metadata
 87 |         metadata = {
 88 |             "source": "ui_upload",
 89 |             "upload_time": str(datetime.now())
 90 |         }
 91 |         
 92 |         # Use asyncio to run the CPU-bound processing in a thread pool
 93 |         # This prevents blocking the Streamlit UI thread
 94 |         loop = asyncio.get_event_loop()
 95 |         
 96 |         # Process the file in a non-blocking way
 97 |         # Using a lambda to properly handle instance methods
 98 |         chunks = await loop.run_in_executor(
 99 |             None,  # Use default executor
100 |             lambda: pipeline.process_file(file_path, metadata)
101 |         )
102 |         
103 |         if not chunks:
104 |             return {
105 |                 "success": False,
106 |                 "file_path": file_path,
107 |                 "error": "No valid chunks were generated from the document"
108 |             }
109 |         
110 |         return {
111 |             "success": True,
112 |             "file_path": file_path,
113 |             "chunk_count": len(chunks)
114 |         }
115 |     except Exception as e:
116 |         import traceback
117 |         print(f"Error processing document: {str(e)}")
118 |         print(traceback.format_exc())
119 |         return {
120 |             "success": False,
121 |             "file_path": file_path,
122 |             "error": str(e)
123 |         }
124 | 
125 | 
126 | async def run_agent_with_streaming(user_input: str):
127 |     """
128 |     Run the RAG agent with streaming response.
129 |     
130 |     Args:
131 |         user_input: User query
132 |         
133 |     Yields:
134 |         Streamed response chunks
135 |     """
136 |     # Run the agent with the user input
137 |     async with rag_agent.agent.iter(user_input, deps={"kb_search": rag_agent.kb_search}, message_history=st.session_state.messages) as run:
138 |         async for node in run:
139 |             # Check if this is a model request node
140 |             if hasattr(node, 'request') and isinstance(node.request, ModelRequest):
141 |                 # Stream tokens from the model's request
142 |                 async with node.stream(run.ctx) as request_stream:
143 |                     async for event in request_stream:
144 |                         if isinstance(event, PartStartEvent) and event.part.part_kind == 'text':
145 |                             yield event.part.content
146 |                         elif isinstance(event, PartDeltaEvent) and isinstance(event.delta, TextPartDelta):
147 |                             delta = event.delta.content_delta
148 |                             yield delta
149 |     
150 |     # Add the new messages to the chat history
151 |     st.session_state.messages.extend(run.result.new_messages())
152 | 
153 | 
154 | async def update_available_sources():
155 |     """
156 |     Update the list of available sources in the knowledge base and refresh document count.
157 |     """
158 |     # Update sources list
159 |     sources = await rag_agent.get_available_sources()
160 |     st.session_state.sources = sources
161 |     
162 |     # Refresh document count from database
163 |     try:
164 |         st.session_state.document_count = supabase_client.count_documents()
165 |     except Exception as e:
166 |         print(f"Error updating document count: {e}")
167 | 
168 | 
169 | async def main():
170 |     """
171 |     Main function for the Streamlit application.
172 |     """
173 |     # Display header
174 |     st.title("🔍 RAG AI Agent")
175 |     st.markdown(
176 |         """
177 |         This application allows you to upload documents (TXT and PDF) to a knowledge base 
178 |         and ask questions that will be answered using the information in those documents.
179 |         """
180 |     )
181 |     
182 |     # Sidebar for document upload
183 |     with st.sidebar:
184 |         st.header("📄 Document Upload")
185 |         
186 |         # File uploader
187 |         uploaded_files = st.file_uploader(
188 |             "Upload documents to the knowledge base",
189 |             type=["txt", "pdf"],
190 |             accept_multiple_files=True
191 |         )
192 |         
193 |         # Process only new uploaded files
194 |         if uploaded_files:
195 |             # Get list of files that haven't been processed yet
196 |             new_files = []
197 |             for uploaded_file in uploaded_files:
198 |                 # Create a unique identifier for the file based on name and content hash
199 |                 file_id = f"{uploaded_file.name}_{hash(uploaded_file.getvalue().hex())}"
200 |                 
201 |                 # Check if this file has already been processed
202 |                 if file_id not in st.session_state.processed_files:
203 |                     new_files.append((uploaded_file, file_id))
204 |             
205 |             # Only show progress bar if there are new files to process
206 |             if new_files:
207 |                 progress_bar = st.progress(0)
208 |                 status_text = st.empty()
209 |                 
210 |                 total_files = len(new_files)
211 |                 for i, (uploaded_file, file_id) in enumerate(new_files):
212 |                     # Update progress
213 |                     progress = (i / total_files)
214 |                     progress_bar.progress(progress)
215 |                     status_text.text(f"Processing {uploaded_file.name}... ({i+1}/{total_files})")
216 |                     
217 |                     # Create a temporary file
218 |                     with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as temp_file:
219 |                         temp_file.write(uploaded_file.getvalue())
220 |                         temp_file_path = temp_file.name
221 |                     
222 |                     try:
223 |                         # Process the document
224 |                         result = await process_document(temp_file_path)
225 |                         
226 |                         # Display result
227 |                         if result["success"]:
228 |                             st.success(f"Processed {uploaded_file.name}: {result['chunk_count']} chunks")
229 |                             st.session_state.document_count += 1
230 |                             # Mark this file as processed
231 |                             st.session_state.processed_files.add(file_id)
232 |                         else:
233 |                             st.error(f"Error processing {uploaded_file.name}: {result['error']}")
234 |                     finally:
235 |                         # Remove temporary file
236 |                         os.unlink(temp_file_path)
237 |                 
238 |                 # Complete progress bar
239 |                 progress_bar.progress(1.0)
240 |                 status_text.text("All documents processed!")
241 |                 
242 |                 # Update available sources
243 |                 await update_available_sources()
244 |             elif uploaded_files:  # If we have files but none are new
245 |                 st.info("All files have already been processed.")
246 |         
247 |         # Display document count
248 |         st.metric("Documents in Knowledge Base", st.session_state.document_count)
249 |         
250 |         # Display available sources
251 |         if st.session_state.sources:
252 |             st.subheader("Available Sources")
253 |             for source in st.session_state.sources:
254 |                 st.write(f"- {source}")
255 |     
256 |     # Main chat interface
257 |     st.header("💬 Chat with the AI")
258 |     
259 |     # Display all messages from the conversation so far
260 |     for msg in st.session_state.messages:
261 |         if isinstance(msg, ModelRequest) or isinstance(msg, ModelResponse):
262 |             for part in msg.parts:
263 |                 display_message_part(part)
264 |     
265 |     # Chat input
266 |     if user_input := st.chat_input("Ask a question about your documents..."):
267 |         # Display user message
268 |         with st.chat_message("user"):
269 |             st.markdown(user_input)
270 |         
271 |         # Display assistant response with streaming
272 |         with st.chat_message("assistant"):
273 |             message_placeholder = st.empty()
274 |             full_response = ""
275 |             
276 |             # Stream the response
277 |             generator = run_agent_with_streaming(user_input)
278 |             async for chunk in generator:
279 |                 full_response += chunk
280 |                 message_placeholder.markdown(full_response + "▌")
281 |             
282 |             # Final response without cursor
283 |             message_placeholder.markdown(full_response)
284 | 
285 | 
286 | if __name__ == "__main__":
287 |     asyncio.run(main())
288 | 


--------------------------------------------------------------------------------└── foundational-rag-agent
    ├── .env.example
    ├── .gitignore
    ├── .windsurf
        └── rules
        │   └── primary-guide.md
    ├── PLANNING.md
    ├── README.md
    ├── TASK.md
    ├── agent
        ├── __init__.py
        ├── agent.py
        ├── prompts.py
        └── tools.py
    ├── database
        ├── __init__.py
        ├── setup.py
        └── setup_db.py
    ├── document_processing
        ├── __init__.py
        ├── chunker.py
        ├── embeddings.py
        ├── ingestion.py
        └── processors.py
    ├── prompt.txt
    ├── rag-example.sql
    ├── requirements.txt
    ├── streamlit_ui_example.py
    ├── tests
        ├── test_agent.py
        ├── test_agent_tools.py
        ├── test_chunker.py
        └── test_processors.py
    └── ui
        └── app.py


/foundational-rag-agent/.env.example:
--------------------------------------------------------------------------------
 1 | # OpenAI API configuration
 2 | OPENAI_API_KEY=your_openai_api_key_here
 3 | OPENAI_MODEL=gpt-4.1-mini  # Or other OpenAI model
 4 | 
 5 | # Supabase configuration
 6 | SUPABASE_URL=your_supabase_url_here
 7 | SUPABASE_KEY=your_supabase_key_here
 8 | 
 9 | # Embedding configuration
10 | EMBEDDING_MODEL=text-embedding-3-small  # OpenAI embedding model
11 | 
12 | # Application settings
13 | CHUNK_SIZE=1000  # Size of text chunks for embedding
14 | CHUNK_OVERLAP=200  # Overlap between chunks
15 | MAX_RESULTS=5  # Maximum number of results to return from vector search
16 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/.gitignore:
--------------------------------------------------------------------------------
1 | .env
2 | __pycache__
3 | venv


--------------------------------------------------------------------------------
/foundational-rag-agent/.windsurf/rules/primary-guide.md:
--------------------------------------------------------------------------------
 1 | ---
 2 | trigger: always_on
 3 | ---
 4 | 
 5 | ### Crawl4AI MCP
 6 | - **Always use the Crawl4AI MCP server** to reference documentation for libraries like Pydantic AI and Mem0.
 7 | - For the tokens, always use 5000 tokens for your search.
 8 | - **Only search three times maximum for any specific piece of documentation.** If you don't get what you need, use the Brave MCP server to perform a wider search.
 9 | 
10 | ### 🔄 Project Awareness & Context
11 | - **Always read `PLANNING.md`** at the start of a new conversation to understand the project's architecture, goals, style, and constraints.
12 | - **Check `TASK.md`** before starting a new task. If the task isn’t listed, add it with a brief description and today's date.
13 | - **Use consistent naming conventions, file structure, and architecture patterns** as described in `PLANNING.md`.
14 |  
15 | ### 🧱 Code Structure & Modularity
16 | - **Never create a file longer than 500 lines of code.** If a file approaches this limit, refactor by splitting it into modules or helper files.
17 | - **Organize code into clearly separated modules**, grouped by feature or responsibility.
18 |   For agents this looks like:
19 |     - `agent.py` - Main agent definition and execution logic 
20 |     - `tools.py` - Tool functions used by the agent 
21 |     - `prompts.py` - System prompts
22 | - **Use clear, consistent imports** (prefer relative imports within packages).
23 | 
24 | ### 🧪 Testing & Reliability
25 | - **Always create Pytest unit tests for new features** (functions, classes, routes, etc).
26 | - **After updating any logic**, check whether existing unit tests need to be updated. If so, do it.
27 | - **Tests should live in a `/tests` folder** mirroring the main app structure.
28 |   - Include at least:
29 |     - 1 test for expected use
30 |     - 1 edge case
31 |     - 1 failure case
32 | - Always test the individual functions for agent tools.
33 | 
34 | ### ✅ Task Completion
35 | - **Mark completed tasks in `TASK.md`** immediately after finishing them.
36 | - Add new sub-tasks or TODOs discovered during development to `TASK.md` under a “Discovered During Work” section.
37 | 
38 | ### 📎 Style & Conventions
39 | - **Use Python** as the primary language.
40 | - **Follow PEP8**, use type hints, and format with `black`.
41 | - **Use `pydantic` for data validation**.
42 | - Don't use relative imports with "." or "..". Instead add on to the system path the directories you need to import from.
43 | - Write **docstrings for every function** using the Google style:
44 |   ```python
45 |   def example():
46 |       """
47 |       Brief summary.
48 | 
49 |       Args:
50 |           param1 (type): Description.
51 | 
52 |       Returns:
53 |           type: Description.
54 |       """
55 |   ```
56 | 
57 | ### 📚 Documentation & Explainability
58 | - **Update `README.md`** when new features are added, dependencies change, or setup steps are modified.
59 | - **Comment non-obvious code** and ensure everything is understandable to a mid-level developer.
60 | - When writing complex logic, **add an inline `# Reason:` comment** explaining the why, not just the what.
61 | 
62 | ### 🧠 AI Behavior Rules
63 | - **Never assume missing context. Ask questions if uncertain.**
64 | - **Always confirm file paths & module names** exist before using
65 | - **Never delete or overwrite existing code** unless explicitly instructed to or if part of a task from `TASK.md`.


--------------------------------------------------------------------------------
/foundational-rag-agent/PLANNING.md:
--------------------------------------------------------------------------------
 1 | # Project Planning: RAG AI Agent with Pydantic AI and Supabase
 2 | 
 3 | ## Project Overview
 4 | We're building a simple Retrieval-Augmented Generation (RAG) AI agent using the Pydantic AI library. The agent will have access to a knowledge base stored in Supabase, allowing it to retrieve relevant information to answer user queries. The system will include functionality to ingest local text and PDF files, process them, and store them in Supabase for later retrieval.
 5 | 
 6 | ## Architecture
 7 | 
 8 | ### Core Components:
 9 | 1. **Document Ingestion Pipeline**
10 |    - Accept local files (TXT, PDF)
11 |    - Simple text processing and chunking (without external libraries)
12 |    - Generate embeddings using OpenAI embeddings API
13 |    - Store documents and embeddings in Supabase
14 | 
15 | 2. **Supabase Database**
16 |    - Store document chunks and their embeddings with pgvector
17 |    - Support semantic search for efficient retrieval
18 |    - Tables will be created and managed via Supabase MCP server
19 | 
20 | 3. **Pydantic AI Agent**
21 |    - Define a tool to query the knowledge base
22 |    - Use OpenAI models for generating responses
23 |    - Integrate knowledge base search results into responses
24 | 
25 | 4. **Streamlit User Interface**
26 |    - Interface for uploading documents
27 |    - Interface for querying the AI agent
28 |    - Display agent responses
29 | 
30 | ### Technology Stack:
31 | - **Language**: Python 3.11+
32 | - **AI Framework**: Pydantic AI for agent implementation
33 | - **Database**: Supabase with pgvector extension
34 | - **Embeddings**: OpenAI embeddings API
35 | - **LLM Provider**: OpenAI (GPT-4.1 mini or similar)
36 | - **UI**: Streamlit
37 | - **Document Processing**: Simple text processing with PyPDF2 for PDF extraction
38 | 
39 | ## Development Process
40 | 
41 | The development will follow a task-based approach where each component will be implemented sequentially. We should:
42 | 
43 | 1. Start by setting up the project structure
44 | 2. Create database tables using Supabase MCP server
45 | 3. Implement simple document ingestion pipeline
46 | 4. Create the Pydantic AI agent with knowledge base search tool
47 | 5. Develop Streamlit UI
48 | 6. Connect all components and ensure they work together
49 | 7. Test the complete system
50 | 
51 | ## Design Principles
52 | 
53 | 1. **Modularity**: Keep components decoupled for easier maintenance
54 | 2. **Simplicity**: Focus on making the system easy to understand and modify
55 | 3. **Performance**: Optimize for response time in knowledge retrieval
56 | 4. **User Experience**: Make the Streamlit interface intuitive
57 | 
58 | ## Environment Configuration
59 | 
60 | Create a `.env.example` file with the following variables:
61 | - `OPENAI_API_KEY`: For embeddings and LLM
62 | - `OPENAI_MODEL`: e.g., "gpt-4.1-mini" or other models
63 | - `SUPABASE_URL`: URL for Supabase instance
64 | - `SUPABASE_KEY`: API key for Supabase
65 | 
66 | This file will serve as a template for users to create their own `.env` file.
67 | 
68 | ## Expected Output
69 | 
70 | A functional RAG system where users can:
71 | - Upload local text or PDF documents to build a knowledge base
72 | - Ask questions to the AI agent
73 | - Receive responses that incorporate information from the knowledge base
74 | 
75 | ## Notes
76 | 
77 | When implementing this project, make sure to:
78 | - Mark tasks complete in the task.md file as you finish them
79 | - Use the Supabase MCP server to create and manage database tables
80 | - Build a simple document ingestion pipeline without complex libraries
81 | - Focus on creating a working Pydantic AI agent that can effectively retrieve and use information from the knowledge base
82 | - Create a clean, intuitive Streamlit interface


--------------------------------------------------------------------------------
/foundational-rag-agent/README.md:
--------------------------------------------------------------------------------
 1 | # RAG AI Agent with Pydantic AI and Supabase
 2 | 
 3 | A simple Retrieval-Augmented Generation (RAG) AI agent using Pydantic AI and Supabase with pgvector for document storage and retrieval.
 4 | 
 5 | ## Features
 6 | 
 7 | - Document ingestion pipeline for TXT and PDF files
 8 | - Vector embeddings using OpenAI
 9 | - Document storage in Supabase with pgvector
10 | - Pydantic AI agent with knowledge base search capabilities
11 | - Streamlit UI for document uploads and agent interaction
12 | 
13 | ## Project Structure
14 | 
15 | ```
16 | foundational-rag-agent/
17 | ├── database/
18 | │   └── setup.py          # Database setup and connection utilities
19 | ├── document_processing/
20 | │   ├── __init__.py
21 | │   ├── chunker.py        # Text chunking functionality
22 | │   ├── embeddings.py     # Embeddings generation with OpenAI
23 | │   ├── ingestion.py      # Document ingestion pipeline
24 | │   └── processors.py     # TXT and PDF processing
25 | ├── agent/
26 | │   ├── __init__.py
27 | │   ├── agent.py          # Main agent definition
28 | │   ├── prompts.py        # System prompts
29 | │   └── tools.py          # Knowledge base search tool
30 | ├── ui/
31 | │   └── app.py            # Streamlit application
32 | ├── tests/
33 | │   ├── test_chunker.py
34 | │   ├── test_embeddings.py
35 | │   ├── test_ingestion.py
36 | │   ├── test_processors.py
37 | │   └── test_agent.py
38 | ├── .env.example          # Example environment variables
39 | ├── requirements.txt      # Project dependencies
40 | ├── PLANNING.md           # Project planning document
41 | ├── TASK.md               # Task tracking
42 | └── README.md             # Project documentation
43 | ```
44 | 
45 | ## Setup
46 | 
47 | 1. Clone the repository
48 | 2. Create a virtual environment:
49 |    ```
50 |    python -m venv venv
51 |    source venv/bin/activate  # On Windows: venv\Scripts\activate
52 |    ```
53 | 3. Install dependencies:
54 |    ```
55 |    pip install -r requirements.txt
56 |    ```
57 | 4. Copy `.env.example` to `.env` and fill in your API keys and configuration
58 | 5. Run the Streamlit application:
59 |    ```
60 |    streamlit run ui/app.py
61 |    ```
62 | 6. Run the SQL in `rag-example.sql` to create the table and matching function for RAG
63 | 
64 | ## Usage
65 | 
66 | 1. Upload documents (TXT or PDF) through the Streamlit UI
67 | 2. Ask questions to the AI agent
68 | 3. View responses with source attribution
69 | 
70 | ## Dependencies
71 | 
72 | - Python 3.11+
73 | - Pydantic AI
74 | - Supabase
75 | - OpenAI
76 | - PyPDF2
77 | - Streamlit
78 | 
79 | ## License
80 | 
81 | MIT
82 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/TASK.md:
--------------------------------------------------------------------------------
 1 | # RAG AI Agent Tasks
 2 | 
 3 | ## Project Setup
 4 | - [x] Review PLANNING.md
 5 | - [x] Create project structure
 6 | - [x] Set up environment configuration (.env.example)
 7 | 
 8 | ## Database Setup
 9 | - [x] Create Supabase tables with pgvector extension
10 | - [x] Set up vector search functionality
11 | 
12 | ## Document Ingestion Pipeline
13 | - [x] Implement TXT file processing
14 | - [x] Implement PDF file processing with PyPDF2
15 | - [x] Create text chunking functionality
16 | - [x] Implement OpenAI embeddings generation
17 | - [x] Create document storage in Supabase
18 | 
19 | ## Pydantic AI Agent
20 | - [x] Create knowledge base search tool
21 | - [x] Implement agent with OpenAI model integration
22 | - [x] Set up context integration for responses
23 | 
24 | ## Streamlit UI
25 | - [x] Create document upload interface
26 | - [x] Implement agent query interface
27 | - [x] Add source attribution display
28 | - [x] Connect UI to agent and document pipeline
29 | 
30 | ## Testing
31 | - [x] Create unit tests for document processing
32 | - [x] Create unit tests for knowledge base search
33 | - [x] Create unit tests for agent functionality
34 | 
35 | ## Documentation
36 | - [x] Update README.md with setup and usage instructions
37 | 
38 | ## Discovered During Work
39 | - [ ] Add support for more document types (e.g., DOCX, HTML)
40 | - [ ] Implement metadata filtering in the UI
41 | - [ ] Add visualization of vector embeddings
42 | - [ ] Create a CLI interface for batch document processing
43 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/agent/__init__.py:
--------------------------------------------------------------------------------
 1 | """
 2 | Agent package for RAG AI agent.
 3 | """
 4 | from agent.agent import RAGAgent, AgentDeps, agent
 5 | from agent.tools import KnowledgeBaseSearch, KnowledgeBaseSearchParams, KnowledgeBaseSearchResult
 6 | 
 7 | __all__ = [
 8 |     'RAGAgent',
 9 |     'AgentDeps',
10 |     'agent',
11 |     'KnowledgeBaseSearch',
12 |     'KnowledgeBaseSearchParams',
13 |     'KnowledgeBaseSearchResult'
14 | ]
15 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/agent/agent.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Main agent definition for the RAG AI agent.
  3 | """
  4 | import os
  5 | import sys
  6 | from typing import List, Dict, Any, Optional, TypedDict
  7 | from pydantic_ai import Agent
  8 | from pydantic_ai.tools import Tool
  9 | from dotenv import load_dotenv
 10 | from pathlib import Path
 11 | 
 12 | # Add parent directory to path to allow relative imports
 13 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 14 | 
 15 | from agent.tools import KnowledgeBaseSearch, KnowledgeBaseSearchParams, KnowledgeBaseSearchResult
 16 | from agent.prompts import RAG_SYSTEM_PROMPT
 17 | 
 18 | # Load environment variables from the project root .env file
 19 | project_root = Path(__file__).resolve().parent.parent
 20 | dotenv_path = project_root / '.env'
 21 | 
 22 | # Force override of existing environment variables
 23 | load_dotenv(dotenv_path, override=True)
 24 | 
 25 | class AgentDeps(TypedDict, total=False):
 26 |     """
 27 |     Dependencies for the RAG agent.
 28 |     """
 29 |     kb_search: KnowledgeBaseSearch
 30 | 
 31 | 
 32 | class RAGAgent:
 33 |     """
 34 |     RAG AI agent with knowledge base search capabilities.
 35 |     
 36 |     Args:
 37 |         model: OpenAI model to use. Defaults to OPENAI_MODEL env var.
 38 |         api_key: OpenAI API key. Defaults to OPENAI_API_KEY env var.
 39 |         kb_search: KnowledgeBaseSearch instance for searching the knowledge base.
 40 |     """
 41 |     
 42 |     def __init__(
 43 |         self,
 44 |         model: Optional[str] = None,
 45 |         api_key: Optional[str] = None,
 46 |         kb_search: Optional[KnowledgeBaseSearch] = None
 47 |     ):
 48 |         """
 49 |         Initialize the RAG agent.
 50 |         """
 51 |         self.model = model or os.getenv("OPENAI_MODEL", "gpt-4.1-mini")
 52 |         self.api_key = api_key or os.getenv("OPENAI_API_KEY")
 53 |         
 54 |         if not self.api_key:
 55 |             raise ValueError("OpenAI API key must be provided either as an argument or environment variable.")
 56 |         
 57 |         # Initialize the knowledge base search tool
 58 |         self.kb_search = kb_search or KnowledgeBaseSearch()
 59 |         
 60 |         # Create the search tool
 61 |         self.search_tool = Tool(self.kb_search.search)
 62 |         
 63 |         # Initialize the Pydantic AI agent
 64 |         self.agent = Agent(
 65 |             f"openai:{self.model}",
 66 |             system_prompt=RAG_SYSTEM_PROMPT,
 67 |             tools=[self.search_tool]
 68 |         )
 69 |     
 70 |     async def query(
 71 |         self, 
 72 |         question: str, 
 73 |         max_results: int = 5,
 74 |         source_filter: Optional[str] = None
 75 |     ) -> Dict[str, Any]:
 76 |         """
 77 |         Query the RAG agent with a question.
 78 |         
 79 |         Args:
 80 |             question: The question to ask
 81 |             max_results: Maximum number of knowledge base results to retrieve
 82 |             source_filter: Optional filter to search only within a specific source
 83 |             
 84 |         Returns:
 85 |             Dictionary containing the agent's response and the knowledge base search results
 86 |         """
 87 |         # Create dependencies for the agent
 88 |         deps = AgentDeps(kb_search=self.kb_search)
 89 |         
 90 |         # Run the agent with the question
 91 |         result = await self.agent.run(
 92 |             question,
 93 |             deps=deps
 94 |         )
 95 |         
 96 |         # Get the agent's response
 97 |         response = result.output
 98 |         
 99 |         # Get the knowledge base search results from the tool calls
100 |         kb_results = []
101 |         for tool_call in result.tool_calls:
102 |             if tool_call.tool.name == "search":
103 |                 kb_results = tool_call.result
104 |         
105 |         return {
106 |             "response": response,
107 |             "kb_results": kb_results
108 |         }
109 |     
110 |     async def get_available_sources(self) -> List[str]:
111 |         """
112 |         Get a list of all available sources in the knowledge base.
113 |         
114 |         Returns:
115 |             List of source identifiers
116 |         """
117 |         return await self.kb_search.get_available_sources()
118 | 
119 | 
120 | # Create a singleton instance for easy import
121 | agent = RAGAgent()
122 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/agent/prompts.py:
--------------------------------------------------------------------------------
 1 | """
 2 | System prompts for the RAG AI agent.
 3 | """
 4 | 
 5 | # System prompt for the RAG agent
 6 | RAG_SYSTEM_PROMPT = """You are a helpful AI assistant with access to a knowledge base.
 7 | When answering questions, you should:
 8 | 
 9 | 1. Use the knowledge base search results when they are relevant to the question.
10 | 2. Cite your sources by mentioning the document name when you use information from the knowledge base.
11 | 3. If the knowledge base doesn't contain relevant information, use your general knowledge to answer.
12 | 4. If you don't know the answer, be honest and say so.
13 | 5. Keep your answers concise and to the point.
14 | 6. Format your responses using markdown for better readability.
15 | 
16 | Remember to always provide accurate information and acknowledge when information comes from the knowledge base.
17 | """
18 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/agent/tools.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Knowledge base search tool for the RAG AI agent.
  3 | """
  4 | import os
  5 | import sys
  6 | from typing import Dict, List, Any, Optional
  7 | from pydantic import BaseModel, Field
  8 | 
  9 | # Add parent directory to path to allow relative imports
 10 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 11 | 
 12 | from database.setup import SupabaseClient
 13 | from document_processing.embeddings import EmbeddingGenerator
 14 | 
 15 | class KnowledgeBaseSearchParams(BaseModel):
 16 |     """
 17 |     Parameters for the knowledge base search tool.
 18 |     """
 19 |     query: str = Field(..., description="The search query to find relevant information in the knowledge base")
 20 |     max_results: int = Field(5, description="Maximum number of results to return (default: 5)")
 21 |     source_filter: Optional[str] = Field(None, description="Optional filter to search only within a specific source")
 22 | 
 23 | 
 24 | class KnowledgeBaseSearchResult(BaseModel):
 25 |     """
 26 |     Result from the knowledge base search.
 27 |     """
 28 |     content: str = Field(..., description="Content of the document chunk")
 29 |     source: str = Field(..., description="Source of the document chunk")
 30 |     source_type: str = Field(..., description="Type of source (e.g., 'pdf', 'txt')")
 31 |     similarity: float = Field(..., description="Similarity score between the query and the document")
 32 |     metadata: Dict[str, Any] = Field(..., description="Additional metadata about the document")
 33 | 
 34 | 
 35 | class KnowledgeBaseSearch:
 36 |     """
 37 |     Tool for searching the knowledge base using vector similarity.
 38 |     """
 39 |     
 40 |     def __init__(
 41 |         self,
 42 |         supabase_client: Optional[SupabaseClient] = None,
 43 |         embedding_generator: Optional[EmbeddingGenerator] = None
 44 |     ):
 45 |         """
 46 |         Initialize the knowledge base search tool.
 47 |         
 48 |         Args:
 49 |             supabase_client: SupabaseClient instance for database operations
 50 |             embedding_generator: EmbeddingGenerator instance for creating embeddings
 51 |         """
 52 |         self.supabase_client = supabase_client or SupabaseClient()
 53 |         self.embedding_generator = embedding_generator or EmbeddingGenerator()
 54 |     
 55 |     async def search(self, params: KnowledgeBaseSearchParams) -> List[KnowledgeBaseSearchResult]:
 56 |         """
 57 |         Search the knowledge base for relevant information.
 58 |         
 59 |         Args:
 60 |             params: Search parameters
 61 |             
 62 |         Returns:
 63 |             List of search results
 64 |         """
 65 |         # Generate embedding for the query
 66 |         query_embedding = self.embedding_generator.embed_text(params.query)
 67 |         
 68 |         # Prepare filter metadata if source filter is provided
 69 |         filter_metadata = None
 70 |         if params.source_filter:
 71 |             filter_metadata = {"source": params.source_filter}
 72 |         
 73 |         # Search for documents
 74 |         results = self.supabase_client.search_documents(
 75 |             query_embedding=query_embedding,
 76 |             match_count=params.max_results,
 77 |             filter_metadata=filter_metadata
 78 |         )
 79 |         
 80 |         # Convert results to KnowledgeBaseSearchResult objects
 81 |         search_results = []
 82 |         for result in results:
 83 |             search_results.append(
 84 |                 KnowledgeBaseSearchResult(
 85 |                     content=result["content"],
 86 |                     source=result["metadata"].get("source", "Unknown"),
 87 |                     source_type=result["metadata"].get("source_type", "Unknown"),
 88 |                     similarity=result["similarity"],
 89 |                     metadata=result["metadata"]
 90 |                 )
 91 |             )
 92 |         
 93 |         return search_results
 94 |     
 95 |     async def get_available_sources(self) -> List[str]:
 96 |         """
 97 |         Get a list of all available sources in the knowledge base.
 98 |         
 99 |         Returns:
100 |             List of source identifiers
101 |         """
102 |         return self.supabase_client.get_all_document_sources()
103 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/database/__init__.py:
--------------------------------------------------------------------------------
 1 | """
 2 | Database package for RAG AI agent.
 3 | """
 4 | from database.setup import SupabaseClient, setup_database_tables
 5 | 
 6 | __all__ = [
 7 |     'SupabaseClient',
 8 |     'setup_database_tables'
 9 | ]
10 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/database/setup.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Database setup and connection utilities for Supabase with pgvector.
  3 | """
  4 | import os
  5 | import json
  6 | from typing import Dict, List, Optional, Any
  7 | from dotenv import load_dotenv
  8 | from pathlib import Path
  9 | from supabase import create_client, Client
 10 | 
 11 | # Load environment variables from the project root .env file
 12 | project_root = Path(__file__).resolve().parent.parent
 13 | dotenv_path = project_root / '.env'
 14 | 
 15 | # Force override of existing environment variables
 16 | load_dotenv(dotenv_path, override=True)
 17 | 
 18 | class SupabaseClient:
 19 |     """
 20 |     Client for interacting with Supabase and pgvector.
 21 |     
 22 |     Args:
 23 |         supabase_url: URL for Supabase instance. Defaults to SUPABASE_URL env var.
 24 |         supabase_key: API key for Supabase. Defaults to SUPABASE_KEY env var.
 25 |     """
 26 |     
 27 |     def __init__(
 28 |         self, 
 29 |         supabase_url: Optional[str] = None, 
 30 |         supabase_key: Optional[str] = None
 31 |     ):
 32 |         """
 33 |         Initialize the Supabase client.
 34 |         """
 35 |         self.supabase_url = supabase_url or os.getenv("SUPABASE_URL")
 36 |         self.supabase_key = supabase_key or os.getenv("SUPABASE_KEY")
 37 |         
 38 |         if not self.supabase_url or not self.supabase_key:
 39 |             raise ValueError(
 40 |                 "Supabase URL and key must be provided either as arguments or environment variables."
 41 |             )
 42 |         
 43 |         self.client = create_client(self.supabase_url, self.supabase_key)
 44 |     
 45 |     def store_document_chunk(
 46 |         self, 
 47 |         url: str, 
 48 |         chunk_number: int, 
 49 |         content: str, 
 50 |         embedding: List[float],
 51 |         metadata: Dict[str, Any] = None
 52 |     ) -> Dict[str, Any]:
 53 |         """
 54 |         Store a document chunk with its embedding in Supabase.
 55 |         
 56 |         Args:
 57 |             url: Source URL or identifier for the document
 58 |             chunk_number: Chunk number within the document
 59 |             content: Text content of the chunk
 60 |             embedding: Vector embedding of the chunk
 61 |             metadata: Additional metadata about the chunk
 62 |             
 63 |         Returns:
 64 |             Dictionary containing the inserted record
 65 |         """
 66 |         if metadata is None:
 67 |             metadata = {}
 68 |             
 69 |         data = {
 70 |             "url": url,
 71 |             "chunk_number": chunk_number,
 72 |             "content": content,
 73 |             "embedding": embedding,
 74 |             "metadata": metadata
 75 |         }
 76 |         
 77 |         result = self.client.table("rag_pages").insert(data).execute()
 78 |         return result.data[0] if result.data else {}
 79 |     
 80 |     def search_documents(
 81 |         self, 
 82 |         query_embedding: List[float], 
 83 |         match_count: int = 5,
 84 |         filter_metadata: Dict[str, Any] = None
 85 |     ) -> List[Dict[str, Any]]:
 86 |         """
 87 |         Search for document chunks by vector similarity.
 88 |         
 89 |         Args:
 90 |             query_embedding: Vector embedding of the query
 91 |             match_count: Maximum number of results to return
 92 |             filter_metadata: Optional metadata filter
 93 |             
 94 |         Returns:
 95 |             List of matching document chunks with similarity scores
 96 |         """
 97 |         # Prepare parameters for the RPC call
 98 |         params = {
 99 |             "query_embedding": query_embedding,
100 |             "match_count": match_count
101 |         }
102 |         
103 |         # Add filter if provided
104 |         if filter_metadata:
105 |             params["filter"] = filter_metadata
106 |         
107 |         # Call the match_rag_pages function
108 |         result = self.client.rpc("match_rag_pages", params).execute()
109 |         return result.data if result.data else []
110 |     
111 |     def get_document_by_id(self, doc_id: int) -> Dict[str, Any]:
112 |         """
113 |         Get a document chunk by its ID.
114 |         
115 |         Args:
116 |             doc_id: ID of the document chunk
117 |             
118 |         Returns:
119 |             Document chunk data
120 |         """
121 |         result = self.client.table("rag_pages").select("*").eq("id", doc_id).execute()
122 |         return result.data[0] if result.data else {}
123 |     
124 |     def get_all_document_sources(self) -> List[str]:
125 |         """
126 |         Get a list of all unique document sources.
127 |         
128 |         Returns:
129 |             List of unique source URLs/identifiers
130 |         """
131 |         result = self.client.table("rag_pages").select("url").execute()
132 |         urls = set(item["url"] for item in result.data if result.data)
133 |         return list(urls)
134 |         
135 |     def count_documents(self) -> int:
136 |         """
137 |         Count the total number of unique documents in the database.
138 |         
139 |         Returns:
140 |             Number of unique documents (based on unique URLs)
141 |         """
142 |         return len(self.get_all_document_sources())
143 | 
144 | 
145 | def setup_database_tables() -> None:
146 |     """
147 |     Set up the necessary database tables and functions for the RAG system.
148 |     This should be run once to initialize the database.
149 |     
150 |     Note: This is typically done through the Supabase MCP server in production.
151 |     """
152 |     # This is a placeholder for the actual implementation
153 |     # In a real application, you would use the Supabase MCP server to run the SQL
154 |     pass
155 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/database/setup_db.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Script to set up the database tables in Supabase using the Supabase MCP server.
  3 | """
  4 | import os
  5 | import sys
  6 | import asyncio
  7 | from pathlib import Path
  8 | from dotenv import load_dotenv
  9 | 
 10 | # Add parent directory to path to allow relative imports
 11 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 12 | 
 13 | # Load environment variables from the project root .env file
 14 | project_root = Path(__file__).resolve().parent.parent
 15 | dotenv_path = project_root / '.env'
 16 | 
 17 | # Force override of existing environment variables
 18 | load_dotenv(dotenv_path, override=True)
 19 | 
 20 | # SQL for creating the database tables and functions
 21 | SQL_SETUP = """
 22 | -- Enable the pgvector extension
 23 | create extension if not exists vector;
 24 | 
 25 | -- Create the documentation chunks table
 26 | create table rag_pages (
 27 |     id bigserial primary key,
 28 |     url varchar not null,
 29 |     chunk_number integer not null,
 30 |     content text not null,
 31 |     metadata jsonb not null default '{}'::jsonb,
 32 |     embedding vector(1536),  -- OpenAI embeddings are 1536 dimensions
 33 |     created_at timestamp with time zone default timezone('utc'::text, now()) not null,
 34 |     
 35 |     -- Add a unique constraint to prevent duplicate chunks for the same URL
 36 |     unique(url, chunk_number)
 37 | );
 38 | 
 39 | -- Create an index for better vector similarity search performance
 40 | create index on rag_pages using ivfflat (embedding vector_cosine_ops);
 41 | 
 42 | -- Create an index on metadata for faster filtering
 43 | create index idx_rag_pages_metadata on rag_pages using gin (metadata);
 44 | 
 45 | -- Create an index on source for faster filtering
 46 | CREATE INDEX idx_rag_pages_source ON rag_pages ((metadata->>'source'));
 47 | 
 48 | -- Create a function to search for documentation chunks
 49 | create or replace function match_rag_pages (
 50 |   query_embedding vector(1536),
 51 |   match_count int default 10,
 52 |   filter jsonb DEFAULT '{}'::jsonb
 53 | ) returns table (
 54 |   id bigint,
 55 |   url varchar,
 56 |   chunk_number integer,
 57 |   content text,
 58 |   metadata jsonb,
 59 |   similarity float
 60 | )
 61 | language plpgsql
 62 | as $
 63 | #variable_conflict use_column
 64 | begin
 65 |   return query
 66 |   select
 67 |     id,
 68 |     url,
 69 |     chunk_number,
 70 |     content,
 71 |     metadata,
 72 |     1 - (rag_pages.embedding <=> query_embedding) as similarity
 73 |   from rag_pages
 74 |   where metadata @> filter
 75 |   order by rag_pages.embedding <=> query_embedding
 76 |   limit match_count;
 77 | end;
 78 | $;
 79 | 
 80 | -- Enable RLS on the table
 81 | alter table rag_pages enable row level security;
 82 | 
 83 | -- Create a policy that allows anyone to read
 84 | create policy "Allow public read access"
 85 |   on rag_pages
 86 |   for select
 87 |   to public
 88 |   using (true);
 89 | 
 90 | -- Create a policy that allows anyone to insert
 91 | create policy "Allow public insert access"
 92 |   on rag_pages
 93 |   for insert
 94 |   to public
 95 |   with check (true);
 96 | """
 97 | 
 98 | async def setup_database():
 99 |     """
100 |     Set up the database tables and functions in Supabase.
101 |     
102 |     This function uses the Supabase MCP server to run the SQL setup script.
103 |     """
104 |     try:
105 |         # In a real application, you would use the Supabase MCP server to run the SQL
106 |         # For example:
107 |         # result = await mcp2_apply_migration(name="rag_setup", query=SQL_SETUP)
108 |         # print(f"Database setup completed: {result}")
109 |         
110 |         print("Database setup script generated.")
111 |         print("To set up the database, use the Supabase MCP server to run the SQL script.")
112 |         print("Example command:")
113 |         print("mcp2_apply_migration(name=\"rag_setup\", query=SQL_SETUP)")
114 |     except Exception as e:
115 |         print(f"Error setting up database: {e}")
116 | 
117 | 
118 | if __name__ == "__main__":
119 |     asyncio.run(setup_database())
120 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/document_processing/__init__.py:
--------------------------------------------------------------------------------
 1 | """
 2 | Document processing package for RAG AI agent.
 3 | """
 4 | from document_processing.chunker import TextChunker
 5 | from document_processing.embeddings import EmbeddingGenerator
 6 | from document_processing.processors import DocumentProcessor, TxtProcessor, PdfProcessor, get_document_processor
 7 | from document_processing.ingestion import DocumentIngestionPipeline
 8 | 
 9 | __all__ = [
10 |     'TextChunker',
11 |     'EmbeddingGenerator',
12 |     'DocumentProcessor',
13 |     'TxtProcessor',
14 |     'PdfProcessor',
15 |     'get_document_processor',
16 |     'DocumentIngestionPipeline'
17 | ]
18 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/document_processing/chunker.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Text chunking functionality for document processing.
  3 | """
  4 | import os
  5 | from typing import List
  6 | from pathlib import Path
  7 | 
  8 | class TextChunker:
  9 |     """
 10 |     Simple text chunker that splits documents into manageable pieces.
 11 |     """
 12 |     
 13 |     def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
 14 |         """
 15 |         Initialize the chunker with size and overlap settings.
 16 |         
 17 |         Args:
 18 |             chunk_size: Maximum size of each chunk in characters
 19 |             chunk_overlap: Number of characters to overlap between chunks
 20 |         """
 21 |         self.chunk_size = chunk_size
 22 |         self.chunk_overlap = min(chunk_overlap, chunk_size // 2)  # Ensure overlap isn't too large
 23 |         
 24 |         print(f"Initialized TextChunker with size={chunk_size}, overlap={self.chunk_overlap}")
 25 |     
 26 |     def chunk_text(self, text: str) -> List[str]:
 27 |         """
 28 |         Split text into chunks using a simple sliding window approach.
 29 |         
 30 |         Args:
 31 |             text: The text to split into chunks
 32 |             
 33 |         Returns:
 34 |             List of text chunks
 35 |         """
 36 |         # Handle empty or very short text
 37 |         if not text or not text.strip():
 38 |             print("Warning: Empty text provided to chunker")
 39 |             return [""]
 40 |             
 41 |         if len(text) <= self.chunk_size:
 42 |             print(f"Text is only {len(text)} chars, returning as single chunk")
 43 |             return [text]
 44 |         
 45 |         # Simple sliding window chunking
 46 |         chunks = []
 47 |         step_size = self.chunk_size - self.chunk_overlap
 48 |         
 49 |         # Ensure step size is at least 100 characters to prevent infinite loops
 50 |         if step_size < 100:
 51 |             step_size = 100
 52 |             print(f"Warning: Adjusted step size to {step_size} to ensure progress")
 53 |         
 54 |         # Create chunks with a sliding window
 55 |         position = 0
 56 |         text_length = len(text)
 57 |         
 58 |         while position < text_length:
 59 |             # Calculate end position for current chunk
 60 |             end = min(position + self.chunk_size, text_length)
 61 |             
 62 |             # Extract the chunk
 63 |             chunk = text[position:end]
 64 |             
 65 |             # Only add non-empty chunks
 66 |             if chunk.strip():
 67 |                 chunks.append(chunk)
 68 |             
 69 |             # Move position forward by step_size
 70 |             position += step_size
 71 |             
 72 |             # Safety check
 73 |             if position >= text_length:
 74 |                 break
 75 |                 
 76 |             # Progress indicator for large texts
 77 |             if text_length > 100000 and len(chunks) % 10 == 0:
 78 |                 print(f"Chunking progress: {min(position, text_length)}/{text_length} characters")
 79 |         
 80 |         print(f"Created {len(chunks)} chunks from {text_length} characters of text")
 81 |         return chunks
 82 |     
 83 |     def chunk_by_separator(self, text: str, separator: str = "\n\n") -> List[str]:
 84 |         """
 85 |         Split text by separator first, then ensure chunks are within size limits.
 86 |         
 87 |         Args:
 88 |             text: The text to split
 89 |             separator: The separator to split on (default: paragraph breaks)
 90 |             
 91 |         Returns:
 92 |             List of text chunks
 93 |         """
 94 |         # Handle empty text
 95 |         if not text or not text.strip():
 96 |             return [""]
 97 |             
 98 |         # Handle short text
 99 |         if len(text) <= self.chunk_size:
100 |             return [text]
101 |         
102 |         # Split by separator
103 |         parts = text.split(separator)
104 |         print(f"Split text into {len(parts)} parts using separator '{separator}'")
105 |         
106 |         # Filter out empty parts
107 |         parts = [part for part in parts if part.strip()]
108 |         
109 |         # Handle case where there are no meaningful parts
110 |         if not parts:
111 |             return [""]
112 |             
113 |         # Handle case where each part is already small enough
114 |         if all(len(part) <= self.chunk_size for part in parts):
115 |             print("All parts are within chunk size limit")
116 |             return parts
117 |         
118 |         # Combine parts into chunks that fit within chunk_size
119 |         chunks = []
120 |         current_chunk = ""
121 |         
122 |         for part in parts:
123 |             # If this part alone exceeds chunk size, we need to split it further
124 |             if len(part) > self.chunk_size:
125 |                 # First add any accumulated chunk
126 |                 if current_chunk:
127 |                     chunks.append(current_chunk)
128 |                     current_chunk = ""
129 |                     
130 |                 # Then split the large part using the regular chunker
131 |                 part_chunks = self.chunk_text(part)
132 |                 chunks.extend(part_chunks)
133 |                 continue
134 |                 
135 |             # If adding this part would exceed chunk size, start a new chunk
136 |             if current_chunk and len(current_chunk) + len(separator) + len(part) > self.chunk_size:
137 |                 chunks.append(current_chunk)
138 |                 current_chunk = part
139 |             # Otherwise add to current chunk
140 |             else:
141 |                 if current_chunk:
142 |                     current_chunk += separator + part
143 |                 else:
144 |                     current_chunk = part
145 |         
146 |         # Add the last chunk if there is one
147 |         if current_chunk:
148 |             chunks.append(current_chunk)
149 |             
150 |         print(f"Created {len(chunks)} chunks using separator-based chunking")
151 |         return chunks
152 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/document_processing/embeddings.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Embeddings generation with OpenAI for document processing.
  3 | """
  4 | import os
  5 | import time
  6 | from typing import List, Dict, Any, Optional
  7 | from dotenv import load_dotenv
  8 | import openai
  9 | from pathlib import Path
 10 | 
 11 | # Load environment variables from the project root .env file
 12 | project_root = Path(__file__).resolve().parent.parent
 13 | dotenv_path = project_root / '.env'
 14 | 
 15 | # Force override of existing environment variables
 16 | load_dotenv(dotenv_path, override=True)
 17 | 
 18 | class EmbeddingGenerator:
 19 |     """
 20 |     Simple and reliable embedding generator using OpenAI's API.
 21 |     """
 22 |     
 23 |     def __init__(self):
 24 |         """Initialize the embedding generator with API key from environment variables."""
 25 |         self.api_key = os.getenv("OPENAI_API_KEY")
 26 |         self.model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
 27 |         
 28 |         if not self.api_key:
 29 |             raise ValueError("OpenAI API key must be provided as OPENAI_API_KEY environment variable.")
 30 |         
 31 |         # Set up the OpenAI client
 32 |         self.client = openai.OpenAI(api_key=self.api_key)
 33 |         
 34 |         # Default embedding dimension for text-embedding-3-small
 35 |         self.embedding_dim = 1536
 36 |         
 37 |         print(f"Initialized EmbeddingGenerator with model: {self.model}")
 38 |     
 39 |     def _create_zero_embedding(self) -> List[float]:
 40 |         """Create a zero vector with the correct dimension."""
 41 |         return [0.0] * self.embedding_dim
 42 |     
 43 |     def embed_text(self, text: str, max_retries: int = 3) -> List[float]:
 44 |         """
 45 |         Generate an embedding for a single text with retry logic.
 46 |         
 47 |         Args:
 48 |             text: The text to embed
 49 |             max_retries: Maximum number of retry attempts
 50 |             
 51 |         Returns:
 52 |             Embedding vector
 53 |         """
 54 |         # Handle empty text
 55 |         if not text or not text.strip():
 56 |             print("Warning: Empty text provided, returning zero embedding")
 57 |             return self._create_zero_embedding()
 58 |         
 59 |         # Truncate very long text to avoid API limits
 60 |         max_length = 8000
 61 |         if len(text) > max_length:
 62 |             print(f"Warning: Text exceeds {max_length} characters, truncating")
 63 |             text = text[:max_length]
 64 |         
 65 |         # Try to generate embedding with retries
 66 |         for attempt in range(max_retries):
 67 |             try:
 68 |                 response = self.client.embeddings.create(
 69 |                     model=self.model,
 70 |                     input=text
 71 |                 )
 72 |                 return response.data[0].embedding
 73 |             except Exception as e:
 74 |                 print(f"Embedding error (attempt {attempt+1}/{max_retries}): {str(e)}")
 75 |                 if attempt < max_retries - 1:
 76 |                     # Exponential backoff
 77 |                     time.sleep(2 ** attempt)
 78 |                 else:
 79 |                     print("All retry attempts failed, returning zero embedding")
 80 |                     return self._create_zero_embedding()
 81 |     
 82 |     def embed_batch(self, texts: List[str], batch_size: int = 5) -> List[List[float]]:
 83 |         """
 84 |         Generate embeddings for multiple texts in small batches.
 85 |         
 86 |         Args:
 87 |             texts: List of texts to embed
 88 |             batch_size: Number of texts to process in each batch
 89 |             
 90 |         Returns:
 91 |             List of embedding vectors
 92 |         """
 93 |         # Filter out empty texts
 94 |         valid_texts = [text for text in texts if text and text.strip()]
 95 |         
 96 |         if not valid_texts:
 97 |             print("No valid texts to embed")
 98 |             return []
 99 |         
100 |         results = []
101 |         
102 |         # Process in small batches to avoid memory issues
103 |         for i in range(0, len(valid_texts), batch_size):
104 |             batch = valid_texts[i:i+batch_size]
105 |             print(f"Processing batch {i//batch_size + 1}/{(len(valid_texts)-1)//batch_size + 1} with {len(batch)} texts")
106 |             
107 |             # Process each text individually for better error isolation
108 |             batch_results = []
109 |             for text in batch:
110 |                 embedding = self.embed_text(text)
111 |                 batch_results.append(embedding)
112 |             
113 |             results.extend(batch_results)
114 |             
115 |             # Small delay between batches to avoid rate limiting
116 |             if i + batch_size < len(valid_texts):
117 |                 time.sleep(0.5)
118 |         
119 |         print(f"Successfully embedded {len(results)} texts")
120 |         return results
121 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/document_processing/ingestion.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Document ingestion pipeline for processing documents and generating embeddings.
  3 | """
  4 | import os
  5 | import uuid
  6 | import logging
  7 | from typing import List, Dict, Any, Optional
  8 | from pathlib import Path
  9 | from datetime import datetime
 10 | 
 11 | from document_processing.chunker import TextChunker
 12 | from document_processing.embeddings import EmbeddingGenerator
 13 | from document_processing.processors import get_document_processor
 14 | from database.setup import SupabaseClient
 15 | 
 16 | # Set up logging
 17 | logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
 18 | logger = logging.getLogger(__name__)
 19 | 
 20 | class DocumentIngestionPipeline:
 21 |     """
 22 |     Simplified document ingestion pipeline with robust error handling.
 23 |     """
 24 |     
 25 |     def __init__(self, supabase_client: Optional[SupabaseClient] = None):
 26 |         """
 27 |         Initialize the document ingestion pipeline with default components.
 28 |         
 29 |         Args:
 30 |             supabase_client: Optional SupabaseClient for database operations
 31 |         """
 32 |         self.chunker = TextChunker(chunk_size=1000, chunk_overlap=200)
 33 |         self.embedding_generator = EmbeddingGenerator()
 34 |         self.max_file_size_mb = 10  # Maximum file size in MB
 35 |         self.supabase_client = supabase_client or SupabaseClient()
 36 |         
 37 |         logger.info("Initialized DocumentIngestionPipeline with default components")
 38 |     
 39 |     def _check_file(self, file_path: str) -> bool:
 40 |         """
 41 |         Validate file exists and is within size limits.
 42 |         
 43 |         Args:
 44 |             file_path: Path to the document file
 45 |             
 46 |         Returns:
 47 |             True if file is valid, False otherwise
 48 |         """
 49 |         # Check if file exists
 50 |         if not os.path.exists(file_path):
 51 |             logger.error(f"File not found: {file_path}")
 52 |             return False
 53 |             
 54 |         # Check file size
 55 |         file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
 56 |         if file_size_mb > self.max_file_size_mb:
 57 |             logger.error(f"File size ({file_size_mb:.2f} MB) exceeds maximum allowed size ({self.max_file_size_mb} MB)")
 58 |             return False
 59 |             
 60 |         return True
 61 |     
 62 |     def process_file(self, file_path: str, metadata: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
 63 |         """
 64 |         Process a document file, extract text, generate chunks and embeddings.
 65 |         
 66 |         Args:
 67 |             file_path: Path to the document file
 68 |             metadata: Optional metadata to associate with the document
 69 |             
 70 |         Returns:
 71 |             List of document chunks with embeddings
 72 |         """
 73 |         # Validate file
 74 |         if not self._check_file(file_path):
 75 |             return []
 76 |         
 77 |         # Get appropriate document processor
 78 |         try:
 79 |             processor = get_document_processor(file_path)
 80 |             if not processor:
 81 |                 logger.error(f"Unsupported file type: {file_path}")
 82 |                 return []
 83 |         except Exception as e:
 84 |             logger.error(f"Error getting document processor: {str(e)}")
 85 |             return []
 86 |         
 87 |         # Extract text from document
 88 |         try:
 89 |             text = processor.extract_text(file_path)
 90 |             logger.info(f"Extracted {len(text)} characters from {os.path.basename(file_path)}")
 91 |             
 92 |             if not text or not text.strip():
 93 |                 logger.warning(f"No text content extracted from {os.path.basename(file_path)}")
 94 |                 return []
 95 |                 
 96 |         except Exception as e:
 97 |             logger.error(f"Failed to extract text from {os.path.basename(file_path)}: {str(e)}")
 98 |             return []
 99 |         
100 |         # Generate chunks
101 |         try:
102 |             chunks = self.chunker.chunk_text(text)
103 |             
104 |             # Filter out empty chunks
105 |             chunks = [chunk for chunk in chunks if chunk and chunk.strip()]
106 |             
107 |             if not chunks:
108 |                 logger.warning("No valid chunks generated from document")
109 |                 return []
110 |                 
111 |             logger.info(f"Generated {len(chunks)} valid chunks from document")
112 |             
113 |         except Exception as e:
114 |             logger.error(f"Error chunking document: {str(e)}")
115 |             return []
116 |         
117 |         # Generate embeddings for chunks
118 |         try:
119 |             embeddings = self.embedding_generator.embed_batch(chunks, batch_size=5)
120 |             
121 |             if len(embeddings) != len(chunks):
122 |                 logger.warning(f"Mismatch between chunks ({len(chunks)}) and embeddings ({len(embeddings)})")
123 |                 # Ensure we only process chunks that have embeddings
124 |                 chunks = chunks[:len(embeddings)]
125 |                 
126 |             logger.info(f"Generated {len(embeddings)} embeddings")
127 |             
128 |         except Exception as e:
129 |             logger.error(f"Error generating embeddings: {str(e)}")
130 |             return []
131 |         
132 |         # Create document records
133 |         try:
134 |             # Generate a unique document ID
135 |             document_id = str(uuid.uuid4())
136 |             timestamp = datetime.now().isoformat()
137 |             
138 |             # Prepare metadata
139 |             if metadata is None:
140 |                 metadata = {}
141 |             
142 |             # Add file info to metadata
143 |             metadata.update({
144 |                 "filename": os.path.basename(file_path),
145 |                 "file_path": file_path,
146 |                 "file_size_bytes": os.path.getsize(file_path),
147 |                 "processed_at": timestamp,
148 |                 "chunk_count": len(chunks)
149 |             })
150 |             
151 |             # Create records and store in database
152 |             records = []
153 |             stored_records = []
154 |             
155 |             # Create a URL/identifier for the document
156 |             url = f"file://{os.path.basename(file_path)}"
157 |             
158 |             for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
159 |                 # Create record for return value
160 |                 record = {
161 |                     "id": f"{document_id}_{i}",
162 |                     "document_id": document_id,
163 |                     "chunk_index": i,
164 |                     "text": chunk,
165 |                     "embedding": embedding,
166 |                     "metadata": metadata.copy()
167 |                 }
168 |                 records.append(record)
169 |                 
170 |                 # Store in Supabase
171 |                 try:
172 |                     stored_record = self.supabase_client.store_document_chunk(
173 |                         url=url,
174 |                         chunk_number=i,
175 |                         content=chunk,
176 |                         embedding=embedding,
177 |                         metadata=metadata.copy()
178 |                     )
179 |                     stored_records.append(stored_record)
180 |                 except Exception as e:
181 |                     logger.error(f"Error storing chunk {i} in database: {str(e)}")
182 |             
183 |             logger.info(f"Created {len(records)} document records with ID {document_id}")
184 |             logger.info(f"Stored {len(stored_records)} chunks in database")
185 |             return records
186 |             
187 |         except Exception as e:
188 |             logger.error(f"Error creating document records: {str(e)}")
189 |             return []
190 |     
191 |     def process_text(self, text: str, source_id: str, metadata: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
192 |         """
193 |         Process a text string through the ingestion pipeline.
194 |         
195 |         Args:
196 |             text: Text content to process
197 |             source_id: Identifier for the source of the text
198 |             metadata: Optional metadata about the text
199 |             
200 |         Returns:
201 |             List of dictionaries containing the processed chunks with their IDs
202 |         """
203 |         if not text or not text.strip():
204 |             logger.warning("Empty text provided to process_text")
205 |             return []
206 |             
207 |         if metadata is None:
208 |             metadata = {}
209 |         
210 |         # Add source information to metadata
211 |         metadata.update({
212 |             "source_type": "text",
213 |             "source_id": source_id,
214 |             "processed_at": datetime.now().isoformat()
215 |         })
216 |         
217 |         try:
218 |             # Generate chunks
219 |             chunks = self.chunker.chunk_text(text)
220 |             chunks = [chunk for chunk in chunks if chunk and chunk.strip()]
221 |             
222 |             if not chunks:
223 |                 logger.warning("No valid chunks generated from text")
224 |                 return []
225 |                 
226 |             logger.info(f"Generated {len(chunks)} chunks from text")
227 |             
228 |             # Generate embeddings
229 |             embeddings = self.embedding_generator.embed_batch(chunks)
230 |             
231 |             # Create document records
232 |             document_id = str(uuid.uuid4())
233 |             
234 |             # Create records and store in database
235 |             records = []
236 |             stored_records = []
237 |             
238 |             # Create a URL/identifier for the text
239 |             url = f"text://{source_id}"
240 |             
241 |             for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
242 |                 # Create record for return value
243 |                 record = {
244 |                     "id": f"{document_id}_{i}",
245 |                     "document_id": document_id,
246 |                     "chunk_index": i,
247 |                     "text": chunk,
248 |                     "embedding": embedding,
249 |                     "metadata": metadata.copy()
250 |                 }
251 |                 records.append(record)
252 |                 
253 |                 # Store in Supabase
254 |                 try:
255 |                     stored_record = self.supabase_client.store_document_chunk(
256 |                         url=url,
257 |                         chunk_number=i,
258 |                         content=chunk,
259 |                         embedding=embedding,
260 |                         metadata=metadata.copy()
261 |                     )
262 |                     stored_records.append(stored_record)
263 |                 except Exception as e:
264 |                     logger.error(f"Error storing text chunk {i} in database: {str(e)}")
265 |             
266 |             logger.info(f"Created {len(records)} records from text input")
267 |             logger.info(f"Stored {len(stored_records)} text chunks in database")
268 |             return records
269 |             
270 |         except Exception as e:
271 |             logger.error(f"Error processing text: {str(e)}")
272 |             return []
273 |     
274 |     def process_batch(self, file_paths: List[str], metadata: Optional[Dict[str, Any]] = None) -> Dict[str, List[Dict[str, Any]]]:
275 |         """
276 |         Process a batch of files through the ingestion pipeline.
277 |         
278 |         Args:
279 |             file_paths: List of paths to document files
280 |             metadata: Optional shared metadata for all files
281 |             
282 |         Returns:
283 |             Dictionary mapping file paths to their processed chunks
284 |         """
285 |         results = {}
286 |         
287 |         for file_path in file_paths:
288 |             try:
289 |                 # Create file-specific metadata
290 |                 file_metadata = metadata.copy() if metadata else {}
291 |                 file_metadata["batch_processed"] = True
292 |                 
293 |                 # Process the file
294 |                 file_results = self.process_file(file_path, file_metadata)
295 |                 results[file_path] = file_results
296 |                 
297 |                 logger.info(f"Processed {file_path} with {len(file_results)} chunks")
298 |                 
299 |             except Exception as e:
300 |                 logger.error(f"Error processing {file_path}: {str(e)}")
301 |                 results[file_path] = []
302 |         
303 |         return results
304 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/document_processing/processors.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Document processors for extracting text from various file types.
  3 | """
  4 | import os
  5 | import logging
  6 | from typing import Dict, Any, Optional, List
  7 | from pathlib import Path
  8 | import PyPDF2
  9 | 
 10 | # Set up logging
 11 | logger = logging.getLogger(__name__)
 12 | 
 13 | class DocumentProcessor:
 14 |     """
 15 |     Base class for document processors.
 16 |     """
 17 |     
 18 |     def extract_text(self, file_path: str) -> str:
 19 |         """
 20 |         Extract text content from a document file.
 21 |         
 22 |         Args:
 23 |             file_path: Path to the document file
 24 |             
 25 |         Returns:
 26 |             Extracted text content as a string
 27 |         """
 28 |         raise NotImplementedError("Subclasses must implement extract_text method")
 29 |     
 30 |     def get_metadata(self, file_path: str) -> Dict[str, Any]:
 31 |         """
 32 |         Extract metadata from a document file.
 33 |         
 34 |         Args:
 35 |             file_path: Path to the document file
 36 |             
 37 |         Returns:
 38 |             Dictionary containing document metadata
 39 |         """
 40 |         # Basic metadata common to all file types
 41 |         path = Path(file_path)
 42 |         return {
 43 |             "filename": path.name,
 44 |             "file_extension": path.suffix.lower(),
 45 |             "file_size_bytes": path.stat().st_size,
 46 |             "created_at": path.stat().st_ctime,
 47 |             "modified_at": path.stat().st_mtime
 48 |         }
 49 | 
 50 | 
 51 | class TxtProcessor(DocumentProcessor):
 52 |     """
 53 |     Processor for plain text files with robust error handling.
 54 |     """
 55 |     
 56 |     def extract_text(self, file_path: str) -> str:
 57 |         """
 58 |         Extract text from a TXT file with encoding fallbacks.
 59 |         
 60 |         Args:
 61 |             file_path: Path to the TXT file
 62 |             
 63 |         Returns:
 64 |             Extracted text content
 65 |         """
 66 |         path = Path(file_path)
 67 |         
 68 |         # Validate file exists
 69 |         if not path.exists():
 70 |             raise FileNotFoundError(f"File not found: {file_path}")
 71 |         
 72 |         # Try different encodings if UTF-8 fails
 73 |         encodings = ["utf-8", "latin-1", "cp1252", "ascii"]
 74 |         content = ""
 75 |         
 76 |         for encoding in encodings:
 77 |             try:
 78 |                 with open(file_path, "r", encoding=encoding) as file:
 79 |                     content = file.read()
 80 |                 logger.info(f"Successfully read text file with {encoding} encoding")
 81 |                 break
 82 |             except UnicodeDecodeError:
 83 |                 logger.warning(f"Failed to decode with {encoding}, trying next encoding")
 84 |             except Exception as e:
 85 |                 logger.error(f"Error reading file with {encoding}: {str(e)}")
 86 |                 raise
 87 |         
 88 |         if not content:
 89 |             raise ValueError(f"Could not decode file with any of the attempted encodings")
 90 |             
 91 |         return content
 92 |     
 93 |     def get_metadata(self, file_path: str) -> Dict[str, Any]:
 94 |         """
 95 |         Get metadata for a TXT file.
 96 |         
 97 |         Args:
 98 |             file_path: Path to the TXT file
 99 |             
100 |         Returns:
101 |             Dictionary containing document metadata
102 |         """
103 |         metadata = super().get_metadata(file_path)
104 |         metadata["content_type"] = "text/plain"
105 |         metadata["processor"] = "TxtProcessor"
106 |         
107 |         # Count lines and words
108 |         try:
109 |             text = self.extract_text(file_path)
110 |             metadata["line_count"] = len(text.splitlines())
111 |             metadata["word_count"] = len(text.split())
112 |         except Exception:
113 |             # Don't fail metadata collection if text extraction fails
114 |             pass
115 |             
116 |         return metadata
117 | 
118 | 
119 | class PdfProcessor(DocumentProcessor):
120 |     """
121 |     Processor for PDF files with improved text extraction.
122 |     """
123 |     
124 |     def extract_text(self, file_path: str) -> str:
125 |         """
126 |         Extract text from a PDF file with page tracking.
127 |         
128 |         Args:
129 |             file_path: Path to the PDF file
130 |             
131 |         Returns:
132 |             Extracted text content
133 |         """
134 |         path = Path(file_path)
135 |         
136 |         # Validate file exists
137 |         if not path.exists():
138 |             raise FileNotFoundError(f"File not found: {file_path}")
139 |         
140 |         try:
141 |             with open(file_path, "rb") as file:
142 |                 reader = PyPDF2.PdfReader(file)
143 |                 
144 |                 # Extract text from all pages with page numbers
145 |                 content = []
146 |                 total_pages = len(reader.pages)
147 |                 
148 |                 for page_num in range(total_pages):
149 |                     try:
150 |                         page = reader.pages[page_num]
151 |                         page_text = page.extract_text()
152 |                         
153 |                         # Add page marker and text
154 |                         if page_text and page_text.strip():
155 |                             content.append(f"[Page {page_num + 1} of {total_pages}]\n{page_text}\n")
156 |                     except Exception as e:
157 |                         logger.warning(f"Error extracting text from page {page_num + 1}: {str(e)}")
158 |                         content.append(f"[Page {page_num + 1} of {total_pages} - Text extraction failed]\n")
159 |                 
160 |                 return "\n".join(content)
161 |                 
162 |         except Exception as e:
163 |             logger.error(f"Error processing PDF file: {str(e)}")
164 |             raise
165 |     
166 |     def get_metadata(self, file_path: str) -> Dict[str, Any]:
167 |         """
168 |         Get metadata for a PDF file including PDF-specific properties.
169 |         
170 |         Args:
171 |             file_path: Path to the PDF file
172 |             
173 |         Returns:
174 |             Dictionary containing document metadata
175 |         """
176 |         metadata = super().get_metadata(file_path)
177 |         metadata["content_type"] = "application/pdf"
178 |         metadata["processor"] = "PdfProcessor"
179 |         
180 |         # Extract PDF-specific metadata
181 |         try:
182 |             with open(file_path, "rb") as file:
183 |                 reader = PyPDF2.PdfReader(file)
184 |                 
185 |                 # Basic PDF properties
186 |                 metadata["page_count"] = len(reader.pages)
187 |                 
188 |                 # PDF document info if available
189 |                 if reader.metadata:
190 |                     pdf_info = reader.metadata
191 |                     if pdf_info.title:
192 |                         metadata["title"] = pdf_info.title
193 |                     if pdf_info.author:
194 |                         metadata["author"] = pdf_info.author
195 |                     if pdf_info.subject:
196 |                         metadata["subject"] = pdf_info.subject
197 |                     if pdf_info.creator:
198 |                         metadata["creator"] = pdf_info.creator
199 |                     if pdf_info.producer:
200 |                         metadata["producer"] = pdf_info.producer
201 |         except Exception as e:
202 |             logger.warning(f"Error extracting PDF metadata: {str(e)}")
203 |             
204 |         return metadata
205 | 
206 | 
207 | def get_document_processor(file_path: str) -> Optional[DocumentProcessor]:
208 |     """
209 |     Get the appropriate processor for a file based on its extension.
210 |     
211 |     Args:
212 |         file_path: Path to the document file
213 |         
214 |     Returns:
215 |         DocumentProcessor instance for the file type or None if unsupported
216 |     """
217 |     path = Path(file_path)
218 |     extension = path.suffix.lower()
219 |     
220 |     processors = {
221 |         ".txt": TxtProcessor(),
222 |         ".pdf": PdfProcessor(),
223 |         # Add more processors here as needed
224 |     }
225 |     
226 |     processor = processors.get(extension)
227 |     
228 |     if processor:
229 |         logger.info(f"Using {processor.__class__.__name__} for {path.name}")
230 |         return processor
231 |     else:
232 |         logger.warning(f"Unsupported file type: {extension}")
233 |         return None
234 | 
235 | 
236 | def get_supported_extensions() -> List[str]:
237 |     """
238 |     Get a list of supported file extensions.
239 |     
240 |     Returns:
241 |         List of supported file extensions
242 |     """
243 |     return [".txt", ".pdf"]
244 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/prompt.txt:
--------------------------------------------------------------------------------
 1 | I'd like to build a RAG AI agent with Pydantic AI and Supabase, using the following MCP servers:
 2 | 
 3 | Be sure to review the planning and task files.
 4 | This project should create a simple RAG system with:
 5 | 
 6 | A document ingestion pipeline that:
 7 | 
 8 | Accepts local TXT and PDF files
 9 | Uses a simple chunking approach
10 | Generates embeddings using OpenAI
11 | Stores documents and vectors in Supabase with pgvector
12 | 
13 | 
14 | A Pydantic AI agent that:
15 | 
16 | Has a tool for knowledge base search
17 | Uses OpenAI models for response generation
18 | Integrates retrieved contexts into responses
19 | 
20 | 
21 | A Streamlit UI that:
22 | 
23 | Allows document uploads
24 | Provides a clean interface for querying the agent
25 | Displays responses with source attribution
26 | Use @streamlit_ui_example.py to see exactly how to integrate Streamlit with a Pydantic AI agent.
27 | 
28 | 
29 | Use the Supabase MCP server to create the necessary database tables with the pgvector extension enabled. For document processing, keep it simple using PyPDF2 for PDFs rather than complex document processing libraries.
30 | 
31 | Use the Crawl4AI RAG MCP server that already has the Pydantic AI and Supabase Python documentation available. So just perform RAG queries whenever necessary. Also use the Brave MCP server to search the web for supplemental docs/examples to aid in creating the agent.


--------------------------------------------------------------------------------
/foundational-rag-agent/rag-example.sql:
--------------------------------------------------------------------------------
 1 | -- Enable the pgvector extension
 2 | create extension if not exists vector;
 3 | 
 4 | -- Create the documentation chunks table
 5 | create table rag_pages (
 6 |     id bigserial primary key,
 7 |     url varchar not null,
 8 |     chunk_number integer not null,
 9 |     content text not null,  -- Added content column
10 |     metadata jsonb not null default '{}'::jsonb,  -- Added metadata column
11 |     embedding vector(1536),  -- OpenAI embeddings are 1536 dimensions
12 |     created_at timestamp with time zone default timezone('utc'::text, now()) not null,
13 |     
14 |     -- Add a unique constraint to prevent duplicate chunks for the same URL
15 |     unique(url, chunk_number)
16 | );
17 | 
18 | -- Create an index for better vector similarity search performance
19 | create index on rag_pages using ivfflat (embedding vector_cosine_ops);
20 | 
21 | -- Create an index on metadata for faster filtering
22 | create index idx_rag_pages_metadata on rag_pages using gin (metadata);
23 | 
24 | CREATE INDEX idx_rag_pages_source ON rag_pages ((metadata->>'source'));
25 | 
26 | -- Create a function to search for documentation chunks
27 | create or replace function match_rag_pages (
28 |   query_embedding vector(1536),
29 |   match_count int default 10,
30 |   filter jsonb DEFAULT '{}'::jsonb
31 | ) returns table (
32 |   id bigint,
33 |   url varchar,
34 |   chunk_number integer,
35 |   content text,
36 |   metadata jsonb,
37 |   similarity float
38 | )
39 | language plpgsql
40 | as $
41 | #variable_conflict use_column
42 | begin
43 |   return query
44 |   select
45 |     id,
46 |     url,
47 |     chunk_number,
48 |     content,
49 |     metadata,
50 |     1 - (rag_pages.embedding <=> query_embedding) as similarity
51 |   from rag_pages
52 |   where metadata @> filter
53 |   order by rag_pages.embedding <=> query_embedding
54 |   limit match_count;
55 | end;
56 | $;
57 | 
58 | -- Enable RLS on the table
59 | alter table rag_pages enable row level security;
60 | 
61 | -- Create a policy that allows anyone to read
62 | create policy "Allow public read access"
63 |   on rag_pages
64 |   for select
65 |   to public
66 |   using (true);


--------------------------------------------------------------------------------
/foundational-rag-agent/requirements.txt:
--------------------------------------------------------------------------------
 1 | pydantic-ai>=0.1.12
 2 | supabase>=2.0.0
 3 | openai>=1.0.0
 4 | PyPDF2>=3.0.0
 5 | streamlit>=1.30.0
 6 | python-dotenv>=1.0.0
 7 | numpy>=1.24.0
 8 | pytest>=7.0.0
 9 | pytest-asyncio>=0.21.0
10 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/streamlit_ui_example.py:
--------------------------------------------------------------------------------
 1 | from pydantic_ai import Agent
 2 | from httpx import AsyncClient
 3 | import streamlit as st
 4 | import asyncio
 5 | import sys
 6 | import os
 7 | 
 8 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 9 | from Basic_Pydantic_AI_Agent.src import agent, AgentDeps
10 | 
11 | # Import all the message part classes from Pydantic AI
12 | from pydantic_ai.messages import ModelRequest, ModelResponse, PartDeltaEvent, PartStartEvent, TextPartDelta
13 | 
14 | def display_message_part(part):
15 |     """
16 |     Display a single part of a message in the Streamlit UI.
17 |     Customize how you display system prompts, user prompts,
18 |     tool calls, tool returns, etc.
19 |     """
20 |     # User messages
21 |     if part.part_kind == 'user-prompt' and part.content:
22 |         with st.chat_message("user"):
23 |             st.markdown(part.content)
24 |     # AI messages
25 |     elif part.part_kind == 'text' and part.content:
26 |         with st.chat_message("assistant"):
27 |             st.markdown(part.content)             
28 | 
29 | async def run_agent_with_streaming(user_input):
30 |     async with AsyncClient() as http_client:
31 |         agent_deps = AgentDeps(
32 |             http_client=http_client,
33 |             brave_api_key=os.getenv("BRAVE_API_KEY", ""),
34 |             searxng_base_url=os.getenv("SEARXNG_BASE_URL", "")
35 |         )   
36 | 
37 |         async with agent.iter(user_input, deps=agent_deps, message_history=st.session_state.messages) as run:
38 |             async for node in run:
39 |                 if Agent.is_model_request_node(node):
40 |                     # A model request node => We can stream tokens from the model's request
41 |                     async with node.stream(run.ctx) as request_stream:
42 |                         async for event in request_stream:
43 |                             if isinstance(event, PartStartEvent) and event.part.part_kind == 'text':
44 |                                     yield event.part.content
45 |                             elif isinstance(event, PartDeltaEvent) and isinstance(event.delta, TextPartDelta):
46 |                                     delta = event.delta.content_delta
47 |                                     yield delta         
48 | 
49 |     # Add the new messages to the chat history (including tool calls and responses)
50 |     st.session_state.messages.extend(run.result.new_messages())       
51 | 
52 | 
53 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
54 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
55 | # ~~~~~~~~~~~~~~~~~~ Main Function with UI Creation ~~~~~~~~~~~~~~~~~~~~
56 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
57 | # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
58 | 
59 | async def main():
60 |     st.title("Pydantic AI Agent")
61 |     
62 |     # Initialize chat history in session state if not present
63 |     if "messages" not in st.session_state:
64 |         st.session_state.messages = []
65 | 
66 |     # Display all messages from the conversation so far
67 |     # Each message is either a ModelRequest or ModelResponse.
68 |     # We iterate over their parts to decide how to display them.
69 |     for msg in st.session_state.messages:
70 |         if isinstance(msg, ModelRequest) or isinstance(msg, ModelResponse):
71 |             for part in msg.parts:
72 |                 display_message_part(part)
73 | 
74 |     # Chat input for the user
75 |     user_input = st.chat_input("What do you want to do today?")
76 | 
77 |     if user_input:
78 |         # Display user prompt in the UI
79 |         with st.chat_message("user"):
80 |             st.markdown(user_input)
81 | 
82 |         # Display the assistant's partial response while streaming
83 |         with st.chat_message("assistant"):
84 |             # Create a placeholder for the streaming text
85 |             message_placeholder = st.empty()
86 |             full_response = ""
87 |             
88 |             # Properly consume the async generator with async for
89 |             generator = run_agent_with_streaming(user_input)
90 |             async for message in generator:
91 |                 full_response += message
92 |                 message_placeholder.markdown(full_response + "▌")
93 |             
94 |             # Final response without the cursor
95 |             message_placeholder.markdown(full_response)
96 | 
97 | 
98 | if __name__ == "__main__":
99 |     asyncio.run(main())


--------------------------------------------------------------------------------
/foundational-rag-agent/tests/test_agent.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Unit tests for the RAG agent module.
  3 | """
  4 | import os
  5 | import sys
  6 | import pytest
  7 | from unittest.mock import MagicMock, patch
  8 | from typing import List, Dict, Any
  9 | 
 10 | # Add parent directory to path to allow relative imports
 11 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 12 | 
 13 | from agent.agent import RAGAgent
 14 | from agent.tools import KnowledgeBaseSearchResult
 15 | 
 16 | 
 17 | class TestRAGAgent:
 18 |     """
 19 |     Test cases for the RAGAgent class.
 20 |     """
 21 |     
 22 |     @pytest.mark.asyncio
 23 |     async def test_query_with_results(self):
 24 |         """
 25 |         Test that the agent query returns results when documents are found.
 26 |         """
 27 |         # Mock the Pydantic AI Agent and KnowledgeBaseSearch
 28 |         mock_agent = MagicMock()
 29 |         mock_kb_search = MagicMock()
 30 |         
 31 |         # Set up mock return values for the agent
 32 |         mock_result = MagicMock()
 33 |         mock_result.output = "This is the agent's response based on the knowledge base."
 34 |         mock_result.tool_calls = [MagicMock()]
 35 |         mock_result.tool_calls[0].tool.name = "search"
 36 |         
 37 |         # Create mock search results
 38 |         mock_search_results = [
 39 |             KnowledgeBaseSearchResult(
 40 |                 content="This is test content 1.",
 41 |                 source="test1.txt",
 42 |                 source_type="txt",
 43 |                 similarity=0.95,
 44 |                 metadata={"source": "test1.txt", "source_type": "txt"}
 45 |             ),
 46 |             KnowledgeBaseSearchResult(
 47 |                 content="This is test content 2.",
 48 |                 source="test2.txt",
 49 |                 source_type="txt",
 50 |                 similarity=0.85,
 51 |                 metadata={"source": "test2.txt", "source_type": "txt"}
 52 |             )
 53 |         ]
 54 |         mock_result.tool_calls[0].result = mock_search_results
 55 |         
 56 |         # Set the agent's run method to return the mock result
 57 |         mock_agent.run.return_value = mock_result
 58 |         
 59 |         # Create the RAGAgent with mocks
 60 |         with patch('agent.agent.Agent', return_value=mock_agent):
 61 |             rag_agent = RAGAgent(
 62 |                 model="gpt-4.1-mini",
 63 |                 api_key="test_api_key",
 64 |                 kb_search=mock_kb_search
 65 |             )
 66 |             
 67 |             # Call the query method
 68 |             result = await rag_agent.query("What is the test content?")
 69 |             
 70 |             # Check that the agent was called correctly
 71 |             mock_agent.run.assert_called_once()
 72 |             
 73 |             # Check the result
 74 |             assert result["response"] == "This is the agent's response based on the knowledge base."
 75 |             assert len(result["kb_results"]) == 2
 76 |             assert result["kb_results"][0].content == "This is test content 1."
 77 |             assert result["kb_results"][1].content == "This is test content 2."
 78 |     
 79 |     @pytest.mark.asyncio
 80 |     async def test_query_no_kb_results(self):
 81 |         """
 82 |         Test that the agent query works when no knowledge base results are found.
 83 |         """
 84 |         # Mock the Pydantic AI Agent and KnowledgeBaseSearch
 85 |         mock_agent = MagicMock()
 86 |         mock_kb_search = MagicMock()
 87 |         
 88 |         # Set up mock return values for the agent
 89 |         mock_result = MagicMock()
 90 |         mock_result.output = "I don't have specific information about that in my knowledge base."
 91 |         mock_result.tool_calls = [MagicMock()]
 92 |         mock_result.tool_calls[0].tool.name = "search"
 93 |         mock_result.tool_calls[0].result = []  # Empty results
 94 |         
 95 |         # Set the agent's run method to return the mock result
 96 |         mock_agent.run.return_value = mock_result
 97 |         
 98 |         # Create the RAGAgent with mocks
 99 |         with patch('agent.agent.Agent', return_value=mock_agent):
100 |             rag_agent = RAGAgent(
101 |                 model="gpt-4.1-mini",
102 |                 api_key="test_api_key",
103 |                 kb_search=mock_kb_search
104 |             )
105 |             
106 |             # Call the query method
107 |             result = await rag_agent.query("What is something not in the knowledge base?")
108 |             
109 |             # Check that the agent was called correctly
110 |             mock_agent.run.assert_called_once()
111 |             
112 |             # Check the result
113 |             assert result["response"] == "I don't have specific information about that in my knowledge base."
114 |             assert len(result["kb_results"]) == 0
115 |     
116 |     @pytest.mark.asyncio
117 |     async def test_get_available_sources(self):
118 |         """
119 |         Test that get_available_sources returns the list of sources.
120 |         """
121 |         # Mock the KnowledgeBaseSearch
122 |         mock_kb_search = MagicMock()
123 |         
124 |         # Set up mock return values
125 |         mock_sources = ["test1.txt", "test2.pdf", "test3.txt"]
126 |         mock_kb_search.get_available_sources.return_value = mock_sources
127 |         
128 |         # Create the RAGAgent with mock
129 |         with patch('agent.agent.Agent'):
130 |             rag_agent = RAGAgent(
131 |                 model="gpt-4.1-mini",
132 |                 api_key="test_api_key",
133 |                 kb_search=mock_kb_search
134 |             )
135 |             
136 |             # Call the get_available_sources method
137 |             sources = await rag_agent.get_available_sources()
138 |             
139 |             # Check that the mock was called correctly
140 |             mock_kb_search.get_available_sources.assert_called_once()
141 |             
142 |             # Check the results
143 |             assert sources == mock_sources
144 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/tests/test_agent_tools.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Unit tests for the agent tools module.
  3 | """
  4 | import os
  5 | import sys
  6 | import pytest
  7 | import asyncio
  8 | from unittest.mock import MagicMock, patch
  9 | from typing import List, Dict, Any
 10 | 
 11 | # Add parent directory to path to allow relative imports
 12 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 13 | 
 14 | from agent.tools import KnowledgeBaseSearch, KnowledgeBaseSearchParams, KnowledgeBaseSearchResult
 15 | 
 16 | 
 17 | class TestKnowledgeBaseSearch:
 18 |     """
 19 |     Test cases for the KnowledgeBaseSearch class.
 20 |     """
 21 |     
 22 |     @pytest.mark.asyncio
 23 |     async def test_search_with_results(self):
 24 |         """
 25 |         Test that search returns results when documents are found.
 26 |         """
 27 |         # Mock the SupabaseClient and EmbeddingGenerator
 28 |         mock_supabase = MagicMock()
 29 |         mock_embedding_generator = MagicMock()
 30 |         
 31 |         # Set up mock return values
 32 |         mock_embedding = [0.1] * 1536  # Mock embedding vector
 33 |         mock_embedding_generator.embed_text.return_value = mock_embedding
 34 |         
 35 |         mock_search_results = [
 36 |             {
 37 |                 "id": 1,
 38 |                 "url": "local://test1.txt",
 39 |                 "chunk_number": 0,
 40 |                 "content": "This is test content 1.",
 41 |                 "metadata": {
 42 |                     "source": "test1.txt",
 43 |                     "source_type": "txt"
 44 |                 },
 45 |                 "similarity": 0.95
 46 |             },
 47 |             {
 48 |                 "id": 2,
 49 |                 "url": "local://test2.txt",
 50 |                 "chunk_number": 1,
 51 |                 "content": "This is test content 2.",
 52 |                 "metadata": {
 53 |                     "source": "test2.txt",
 54 |                     "source_type": "txt"
 55 |                 },
 56 |                 "similarity": 0.85
 57 |             }
 58 |         ]
 59 |         mock_supabase.search_documents.return_value = mock_search_results
 60 |         
 61 |         # Create the KnowledgeBaseSearch instance with mocks
 62 |         kb_search = KnowledgeBaseSearch(
 63 |             supabase_client=mock_supabase,
 64 |             embedding_generator=mock_embedding_generator
 65 |         )
 66 |         
 67 |         # Create search parameters
 68 |         params = KnowledgeBaseSearchParams(
 69 |             query="test query",
 70 |             max_results=2
 71 |         )
 72 |         
 73 |         # Call the search method
 74 |         results = await kb_search.search(params)
 75 |         
 76 |         # Check that the mocks were called correctly
 77 |         mock_embedding_generator.embed_text.assert_called_once_with("test query")
 78 |         mock_supabase.search_documents.assert_called_once_with(
 79 |             query_embedding=mock_embedding,
 80 |             match_count=2,
 81 |             filter_metadata=None
 82 |         )
 83 |         
 84 |         # Check the results
 85 |         assert len(results) == 2
 86 |         assert isinstance(results[0], KnowledgeBaseSearchResult)
 87 |         assert results[0].content == "This is test content 1."
 88 |         assert results[0].source == "test1.txt"
 89 |         assert results[0].source_type == "txt"
 90 |         assert results[0].similarity == 0.95
 91 |         
 92 |         assert results[1].content == "This is test content 2."
 93 |         assert results[1].source == "test2.txt"
 94 |         assert results[1].source_type == "txt"
 95 |         assert results[1].similarity == 0.85
 96 |     
 97 |     @pytest.mark.asyncio
 98 |     async def test_search_with_source_filter(self):
 99 |         """
100 |         Test that search applies source filter correctly.
101 |         """
102 |         # Mock the SupabaseClient and EmbeddingGenerator
103 |         mock_supabase = MagicMock()
104 |         mock_embedding_generator = MagicMock()
105 |         
106 |         # Set up mock return values
107 |         mock_embedding = [0.1] * 1536  # Mock embedding vector
108 |         mock_embedding_generator.embed_text.return_value = mock_embedding
109 |         
110 |         mock_search_results = [
111 |             {
112 |                 "id": 1,
113 |                 "url": "local://test1.txt",
114 |                 "chunk_number": 0,
115 |                 "content": "This is test content 1.",
116 |                 "metadata": {
117 |                     "source": "test1.txt",
118 |                     "source_type": "txt"
119 |                 },
120 |                 "similarity": 0.95
121 |             }
122 |         ]
123 |         mock_supabase.search_documents.return_value = mock_search_results
124 |         
125 |         # Create the KnowledgeBaseSearch instance with mocks
126 |         kb_search = KnowledgeBaseSearch(
127 |             supabase_client=mock_supabase,
128 |             embedding_generator=mock_embedding_generator
129 |         )
130 |         
131 |         # Create search parameters with source filter
132 |         params = KnowledgeBaseSearchParams(
133 |             query="test query",
134 |             max_results=5,
135 |             source_filter="test1.txt"
136 |         )
137 |         
138 |         # Call the search method
139 |         results = await kb_search.search(params)
140 |         
141 |         # Check that the mocks were called correctly
142 |         mock_embedding_generator.embed_text.assert_called_once_with("test query")
143 |         mock_supabase.search_documents.assert_called_once_with(
144 |             query_embedding=mock_embedding,
145 |             match_count=5,
146 |             filter_metadata={"source": "test1.txt"}
147 |         )
148 |         
149 |         # Check the results
150 |         assert len(results) == 1
151 |         assert results[0].source == "test1.txt"
152 |     
153 |     @pytest.mark.asyncio
154 |     async def test_search_no_results(self):
155 |         """
156 |         Test that search returns empty list when no documents are found.
157 |         """
158 |         # Mock the SupabaseClient and EmbeddingGenerator
159 |         mock_supabase = MagicMock()
160 |         mock_embedding_generator = MagicMock()
161 |         
162 |         # Set up mock return values
163 |         mock_embedding = [0.1] * 1536  # Mock embedding vector
164 |         mock_embedding_generator.embed_text.return_value = mock_embedding
165 |         
166 |         # Return empty results
167 |         mock_supabase.search_documents.return_value = []
168 |         
169 |         # Create the KnowledgeBaseSearch instance with mocks
170 |         kb_search = KnowledgeBaseSearch(
171 |             supabase_client=mock_supabase,
172 |             embedding_generator=mock_embedding_generator
173 |         )
174 |         
175 |         # Create search parameters
176 |         params = KnowledgeBaseSearchParams(
177 |             query="test query",
178 |             max_results=5
179 |         )
180 |         
181 |         # Call the search method
182 |         results = await kb_search.search(params)
183 |         
184 |         # Check the results
185 |         assert len(results) == 0
186 |     
187 |     @pytest.mark.asyncio
188 |     async def test_get_available_sources(self):
189 |         """
190 |         Test that get_available_sources returns the list of sources.
191 |         """
192 |         # Mock the SupabaseClient
193 |         mock_supabase = MagicMock()
194 |         
195 |         # Set up mock return values
196 |         mock_sources = ["test1.txt", "test2.pdf", "test3.txt"]
197 |         mock_supabase.get_all_document_sources.return_value = mock_sources
198 |         
199 |         # Create the KnowledgeBaseSearch instance with mock
200 |         kb_search = KnowledgeBaseSearch(supabase_client=mock_supabase)
201 |         
202 |         # Call the get_available_sources method
203 |         sources = await kb_search.get_available_sources()
204 |         
205 |         # Check that the mock was called correctly
206 |         mock_supabase.get_all_document_sources.assert_called_once()
207 |         
208 |         # Check the results
209 |         assert sources == mock_sources
210 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/tests/test_chunker.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Unit tests for the text chunker module.
  3 | """
  4 | import os
  5 | import sys
  6 | import pytest
  7 | from pathlib import Path
  8 | 
  9 | # Add parent directory to path to allow relative imports
 10 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 11 | 
 12 | from document_processing.chunker import TextChunker
 13 | 
 14 | 
 15 | class TestTextChunker:
 16 |     """
 17 |     Test cases for the TextChunker class.
 18 |     """
 19 |     
 20 |     def test_init_with_default_values(self):
 21 |         """
 22 |         Test that TextChunker initializes with default values.
 23 |         """
 24 |         chunker = TextChunker()
 25 |         assert chunker.chunk_size == 1000
 26 |         assert chunker.chunk_overlap == 200
 27 |     
 28 |     def test_init_with_custom_values(self):
 29 |         """
 30 |         Test that TextChunker initializes with custom values.
 31 |         """
 32 |         chunker = TextChunker(chunk_size=500, chunk_overlap=100)
 33 |         assert chunker.chunk_size == 500
 34 |         assert chunker.chunk_overlap == 100
 35 |     
 36 |     def test_init_with_large_overlap(self):
 37 |         """
 38 |         Test that TextChunker adjusts overlap when it's too large.
 39 |         """
 40 |         # In our new implementation, we automatically adjust the overlap
 41 |         # to be at most half of the chunk size
 42 |         chunker = TextChunker(chunk_size=500, chunk_overlap=500)
 43 |         assert chunker.chunk_overlap == 250  # Should be adjusted to chunk_size // 2
 44 |         
 45 |         chunker = TextChunker(chunk_size=500, chunk_overlap=600)
 46 |         assert chunker.chunk_overlap == 250  # Should be adjusted to chunk_size // 2
 47 |     
 48 |     def test_chunk_text_short_text(self):
 49 |         """
 50 |         Test chunking text that is shorter than chunk_size.
 51 |         """
 52 |         chunker = TextChunker(chunk_size=1000, chunk_overlap=200)
 53 |         text = "This is a short text."
 54 |         chunks = chunker.chunk_text(text)
 55 |         
 56 |         assert len(chunks) == 1
 57 |         assert chunks[0] == text
 58 |     
 59 |     def test_chunk_text_long_text(self):
 60 |         """
 61 |         Test chunking text that is longer than chunk_size.
 62 |         """
 63 |         chunker = TextChunker(chunk_size=100, chunk_overlap=20)
 64 |         text = "This is a longer text that should be split into multiple chunks. " * 5
 65 |         chunks = chunker.chunk_text(text)
 66 |         
 67 |         assert len(chunks) > 1
 68 |         
 69 |         # Check that the chunks cover the entire text
 70 |         reconstructed = ""
 71 |         for i, chunk in enumerate(chunks):
 72 |             if i == 0:
 73 |                 reconstructed += chunk
 74 |             else:
 75 |                 # Account for overlap
 76 |                 overlap_start = len(reconstructed) - chunker.chunk_overlap
 77 |                 if overlap_start > 0:
 78 |                     reconstructed = reconstructed[:overlap_start] + chunk
 79 |                 else:
 80 |                     reconstructed += chunk
 81 |         
 82 |         # The reconstructed text might be slightly different due to splitting at sentence boundaries
 83 |         assert len(reconstructed) >= len(text) * 0.9
 84 |     
 85 |     def test_chunk_by_separator(self):
 86 |         """
 87 |         Test splitting text by a separator.
 88 |         """
 89 |         chunker = TextChunker(chunk_size=100, chunk_overlap=20)
 90 |         paragraphs = [
 91 |             "This is the first paragraph.",
 92 |             "This is the second paragraph.",
 93 |             "This is the third paragraph.",
 94 |             "This is the fourth paragraph."
 95 |         ]
 96 |         text = "\n\n".join(paragraphs)
 97 |         
 98 |         chunks = chunker.chunk_by_separator(text, separator="\n\n")
 99 |         
100 |         assert len(chunks) == 4
101 |         for i, paragraph in enumerate(paragraphs):
102 |             assert paragraph in chunks[i]
103 |     
104 |     def test_chunk_by_separator_large_paragraph(self):
105 |         """
106 |         Test splitting text by a separator with a paragraph larger than chunk_size.
107 |         """
108 |         chunker = TextChunker(chunk_size=50, chunk_overlap=10)
109 |         paragraphs = [
110 |             "This is a short paragraph.",
111 |             "This is a very long paragraph that exceeds the chunk size and should be split into multiple chunks.",
112 |             "This is another short paragraph."
113 |         ]
114 |         text = "\n\n".join(paragraphs)
115 |         
116 |         chunks = chunker.chunk_by_separator(text, separator="\n\n")
117 |         
118 |         assert len(chunks) > 3  # The long paragraph should be split
119 |         assert paragraphs[0] in chunks[0]
120 |         assert paragraphs[2] in chunks[-1]
121 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/tests/test_processors.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Unit tests for the document processors module.
  3 | """
  4 | import os
  5 | import sys
  6 | import pytest
  7 | from pathlib import Path
  8 | import tempfile
  9 | 
 10 | # Add parent directory to path to allow relative imports
 11 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 12 | 
 13 | from document_processing.processors import DocumentProcessor, TxtProcessor, PdfProcessor, get_document_processor
 14 | 
 15 | 
 16 | class TestDocumentProcessor:
 17 |     """
 18 |     Test cases for the DocumentProcessor base class.
 19 |     """
 20 |     
 21 |     def test_extract_text_not_implemented(self):
 22 |         """
 23 |         Test that the base DocumentProcessor raises NotImplementedError for extract_text.
 24 |         """
 25 |         processor = DocumentProcessor()
 26 |         with pytest.raises(NotImplementedError):
 27 |             processor.extract_text("dummy_path")
 28 |             
 29 |     def test_get_metadata_basic(self):
 30 |         """
 31 |         Test that the base DocumentProcessor provides basic metadata.
 32 |         """
 33 |         # Create a temporary file for testing
 34 |         with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
 35 |             temp_file.write(b"Test content")
 36 |             temp_file_path = temp_file.name
 37 |             
 38 |         try:
 39 |             processor = DocumentProcessor()
 40 |             metadata = processor.get_metadata(temp_file_path)
 41 |             
 42 |             # Check basic metadata fields
 43 |             assert "filename" in metadata
 44 |             assert "file_extension" in metadata
 45 |             assert "file_size_bytes" in metadata
 46 |             assert metadata["file_extension"] == ".txt"
 47 |         finally:
 48 |             # Clean up
 49 |             os.unlink(temp_file_path)
 50 | 
 51 | 
 52 | class TestTxtProcessor:
 53 |     """
 54 |     Test cases for the TxtProcessor class.
 55 |     """
 56 |     
 57 |     def test_extract_text_nonexistent_file(self):
 58 |         """
 59 |         Test that TxtProcessor raises FileNotFoundError for nonexistent files.
 60 |         """
 61 |         processor = TxtProcessor()
 62 |         with pytest.raises(FileNotFoundError):
 63 |             processor.extract_text("nonexistent_file.txt")
 64 |     
 65 |     def test_extract_text_valid_txt_file(self):
 66 |         """
 67 |         Test that TxtProcessor correctly extracts text from a valid TXT file.
 68 |         """
 69 |         # Create a temporary TXT file
 70 |         content = "This is a test document.\nIt has multiple lines.\nAnd some content to process."
 71 |         with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
 72 |             temp_file.write(content.encode("utf-8"))
 73 |             temp_file_path = temp_file.name
 74 |         
 75 |         try:
 76 |             processor = TxtProcessor()
 77 |             extracted_text = processor.extract_text(temp_file_path)
 78 |             
 79 |             # Check the extracted text
 80 |             assert extracted_text == content
 81 |         finally:
 82 |             # Clean up the temporary file
 83 |             os.unlink(temp_file_path)
 84 |     
 85 |     def test_get_metadata_txt_file(self):
 86 |         """
 87 |         Test that TxtProcessor correctly extracts metadata from a TXT file.
 88 |         """
 89 |         # Create a temporary TXT file
 90 |         content = "This is a test document.\nIt has multiple lines.\nAnd some content to process."
 91 |         with tempfile.NamedTemporaryFile(suffix=".txt", delete=False) as temp_file:
 92 |             temp_file.write(content.encode("utf-8"))
 93 |             temp_file_path = temp_file.name
 94 |         
 95 |         try:
 96 |             processor = TxtProcessor()
 97 |             metadata = processor.get_metadata(temp_file_path)
 98 |             
 99 |             # Check metadata fields
100 |             assert "filename" in metadata
101 |             assert "file_extension" in metadata
102 |             assert "file_size_bytes" in metadata
103 |             assert "content_type" in metadata
104 |             assert metadata["file_extension"] == ".txt"
105 |             assert metadata["content_type"] == "text/plain"
106 |             assert "processor" in metadata
107 |             assert metadata["processor"] == "TxtProcessor"
108 |         finally:
109 |             # Clean up the temporary file
110 |             os.unlink(temp_file_path)
111 | 
112 | 
113 | class TestPdfProcessor:
114 |     """
115 |     Test cases for the PdfProcessor class.
116 |     """
117 |     
118 |     def test_extract_text_nonexistent_file(self):
119 |         """
120 |         Test that PdfProcessor raises FileNotFoundError for nonexistent files.
121 |         """
122 |         processor = PdfProcessor()
123 |         with pytest.raises(FileNotFoundError):
124 |             processor.extract_text("nonexistent_file.pdf")
125 |     
126 |     def test_get_metadata_pdf_file(self):
127 |         """
128 |         Test that PdfProcessor correctly extracts metadata.
129 |         Note: This test doesn't use a real PDF file to avoid dependencies,
130 |         but just tests the error handling.
131 |         """
132 |         processor = PdfProcessor()
133 |         
134 |         # Since we can't easily create a valid PDF file in a test,
135 |         # we'll just test that the method handles errors gracefully
136 |         with pytest.raises(FileNotFoundError):
137 |             processor.get_metadata("nonexistent_file.pdf")
138 | 
139 | 
140 | class TestGetDocumentProcessor:
141 |     """
142 |     Test cases for the get_document_processor function.
143 |     """
144 |     
145 |     def test_get_document_processor_txt(self):
146 |         """
147 |         Test that get_document_processor returns a TxtProcessor for .txt files.
148 |         """
149 |         processor = get_document_processor("test.txt")
150 |         assert isinstance(processor, TxtProcessor)
151 |     
152 |     def test_get_document_processor_pdf(self):
153 |         """
154 |         Test that get_document_processor returns a PdfProcessor for .pdf files.
155 |         """
156 |         processor = get_document_processor("test.pdf")
157 |         assert isinstance(processor, PdfProcessor)
158 |     
159 |     def test_get_document_processor_unsupported(self):
160 |         """
161 |         Test that get_document_processor returns None for unsupported file types.
162 |         """
163 |         assert get_document_processor("test.docx") is None
164 |         assert get_document_processor("test.csv") is None
165 | 


--------------------------------------------------------------------------------
/foundational-rag-agent/ui/app.py:
--------------------------------------------------------------------------------
  1 | """
  2 | Streamlit application for the RAG AI agent.
  3 | """
  4 | import os
  5 | import sys
  6 | import asyncio
  7 | from typing import List, Dict, Any
  8 | import streamlit as st
  9 | from pathlib import Path
 10 | import tempfile
 11 | from datetime import datetime
 12 | 
 13 | # Add parent directory to path to allow relative imports
 14 | sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 15 | 
 16 | from document_processing.ingestion import DocumentIngestionPipeline
 17 | from document_processing.chunker import TextChunker
 18 | from document_processing.embeddings import EmbeddingGenerator
 19 | from database.setup import SupabaseClient
 20 | from agent.agent import RAGAgent, agent as rag_agent
 21 | from pydantic_ai.messages import ModelRequest, ModelResponse, PartDeltaEvent, PartStartEvent, TextPartDelta
 22 | 
 23 | # Set page configuration
 24 | st.set_page_config(
 25 |     page_title="RAG AI Agent",
 26 |     page_icon="🔍",
 27 |     layout="wide",
 28 |     initial_sidebar_state="expanded"
 29 | )
 30 | 
 31 | # Initialize database client
 32 | supabase_client = SupabaseClient()
 33 | 
 34 | # Initialize session state
 35 | if "messages" not in st.session_state:
 36 |     st.session_state.messages = []
 37 |     
 38 | if "sources" not in st.session_state:
 39 |     st.session_state.sources = []
 40 |     
 41 | if "document_count" not in st.session_state:
 42 |     # Initialize document count from database
 43 |     try:
 44 |         st.session_state.document_count = supabase_client.count_documents()
 45 |     except Exception as e:
 46 |         print(f"Error getting document count: {e}")
 47 |         st.session_state.document_count = 0
 48 |     
 49 | if "processed_files" not in st.session_state:
 50 |     st.session_state.processed_files = set()  # Track already processed files
 51 | 
 52 | 
 53 | def display_message_part(part):
 54 |     """
 55 |     Display a single part of a message in the Streamlit UI.
 56 |     
 57 |     Args:
 58 |         part: Message part to display
 59 |     """
 60 |     # User messages
 61 |     if part.part_kind == 'user-prompt' and part.content:
 62 |         with st.chat_message("user"):
 63 |             st.markdown(part.content)
 64 |     # AI messages
 65 |     elif part.part_kind == 'text' and part.content:
 66 |         with st.chat_message("assistant"):
 67 |             st.markdown(part.content)
 68 | 
 69 | 
 70 | async def process_document(file_path: str) -> Dict[str, Any]:
 71 |     """
 72 |     Process a document file and store it in the knowledge base.
 73 |     
 74 |     Args:
 75 |         file_path: Path to the document file
 76 |         
 77 |     Returns:
 78 |         Dictionary containing information about the processed document
 79 |     """
 80 |     # Create document ingestion pipeline with default settings
 81 |     # The pipeline now handles chunking and embedding internally
 82 |     pipeline = DocumentIngestionPipeline()
 83 |     
 84 |     # Process the file
 85 |     try:
 86 |         # Add file-specific metadata
 87 |         metadata = {
 88 |             "source": "ui_upload",
 89 |             "upload_time": str(datetime.now())
 90 |         }
 91 |         
 92 |         # Use asyncio to run the CPU-bound processing in a thread pool
 93 |         # This prevents blocking the Streamlit UI thread
 94 |         loop = asyncio.get_event_loop()
 95 |         
 96 |         # Process the file in a non-blocking way
 97 |         # Using a lambda to properly handle instance methods
 98 |         chunks = await loop.run_in_executor(
 99 |             None,  # Use default executor
100 |             lambda: pipeline.process_file(file_path, metadata)
101 |         )
102 |         
103 |         if not chunks:
104 |             return {
105 |                 "success": False,
106 |                 "file_path": file_path,
107 |                 "error": "No valid chunks were generated from the document"
108 |             }
109 |         
110 |         return {
111 |             "success": True,
112 |             "file_path": file_path,
113 |             "chunk_count": len(chunks)
114 |         }
115 |     except Exception as e:
116 |         import traceback
117 |         print(f"Error processing document: {str(e)}")
118 |         print(traceback.format_exc())
119 |         return {
120 |             "success": False,
121 |             "file_path": file_path,
122 |             "error": str(e)
123 |         }
124 | 
125 | 
126 | async def run_agent_with_streaming(user_input: str):
127 |     """
128 |     Run the RAG agent with streaming response.
129 |     
130 |     Args:
131 |         user_input: User query
132 |         
133 |     Yields:
134 |         Streamed response chunks
135 |     """
136 |     # Run the agent with the user input
137 |     async with rag_agent.agent.iter(user_input, deps={"kb_search": rag_agent.kb_search}, message_history=st.session_state.messages) as run:
138 |         async for node in run:
139 |             # Check if this is a model request node
140 |             if hasattr(node, 'request') and isinstance(node.request, ModelRequest):
141 |                 # Stream tokens from the model's request
142 |                 async with node.stream(run.ctx) as request_stream:
143 |                     async for event in request_stream:
144 |                         if isinstance(event, PartStartEvent) and event.part.part_kind == 'text':
145 |                             yield event.part.content
146 |                         elif isinstance(event, PartDeltaEvent) and isinstance(event.delta, TextPartDelta):
147 |                             delta = event.delta.content_delta
148 |                             yield delta
149 |     
150 |     # Add the new messages to the chat history
151 |     st.session_state.messages.extend(run.result.new_messages())
152 | 
153 | 
154 | async def update_available_sources():
155 |     """
156 |     Update the list of available sources in the knowledge base and refresh document count.
157 |     """
158 |     # Update sources list
159 |     sources = await rag_agent.get_available_sources()
160 |     st.session_state.sources = sources
161 |     
162 |     # Refresh document count from database
163 |     try:
164 |         st.session_state.document_count = supabase_client.count_documents()
165 |     except Exception as e:
166 |         print(f"Error updating document count: {e}")
167 | 
168 | 
169 | async def main():
170 |     """
171 |     Main function for the Streamlit application.
172 |     """
173 |     # Display header
174 |     st.title("🔍 RAG AI Agent")
175 |     st.markdown(
176 |         """
177 |         This application allows you to upload documents (TXT and PDF) to a knowledge base 
178 |         and ask questions that will be answered using the information in those documents.
179 |         """
180 |     )
181 |     
182 |     # Sidebar for document upload
183 |     with st.sidebar:
184 |         st.header("📄 Document Upload")
185 |         
186 |         # File uploader
187 |         uploaded_files = st.file_uploader(
188 |             "Upload documents to the knowledge base",
189 |             type=["txt", "pdf"],
190 |             accept_multiple_files=True
191 |         )
192 |         
193 |         # Process only new uploaded files
194 |         if uploaded_files:
195 |             # Get list of files that haven't been processed yet
196 |             new_files = []
197 |             for uploaded_file in uploaded_files:
198 |                 # Create a unique identifier for the file based on name and content hash
199 |                 file_id = f"{uploaded_file.name}_{hash(uploaded_file.getvalue().hex())}"
200 |                 
201 |                 # Check if this file has already been processed
202 |                 if file_id not in st.session_state.processed_files:
203 |                     new_files.append((uploaded_file, file_id))
204 |             
205 |             # Only show progress bar if there are new files to process
206 |             if new_files:
207 |                 progress_bar = st.progress(0)
208 |                 status_text = st.empty()
209 |                 
210 |                 total_files = len(new_files)
211 |                 for i, (uploaded_file, file_id) in enumerate(new_files):
212 |                     # Update progress
213 |                     progress = (i / total_files)
214 |                     progress_bar.progress(progress)
215 |                     status_text.text(f"Processing {uploaded_file.name}... ({i+1}/{total_files})")
216 |                     
217 |                     # Create a temporary file
218 |                     with tempfile.NamedTemporaryFile(delete=False, suffix=Path(uploaded_file.name).suffix) as temp_file:
219 |                         temp_file.write(uploaded_file.getvalue())
220 |                         temp_file_path = temp_file.name
221 |                     
222 |                     try:
223 |                         # Process the document
224 |                         result = await process_document(temp_file_path)
225 |                         
226 |                         # Display result
227 |                         if result["success"]:
228 |                             st.success(f"Processed {uploaded_file.name}: {result['chunk_count']} chunks")
229 |                             st.session_state.document_count += 1
230 |                             # Mark this file as processed
231 |                             st.session_state.processed_files.add(file_id)
232 |                         else:
233 |                             st.error(f"Error processing {uploaded_file.name}: {result['error']}")
234 |                     finally:
235 |                         # Remove temporary file
236 |                         os.unlink(temp_file_path)
237 |                 
238 |                 # Complete progress bar
239 |                 progress_bar.progress(1.0)
240 |                 status_text.text("All documents processed!")
241 |                 
242 |                 # Update available sources
243 |                 await update_available_sources()
244 |             elif uploaded_files:  # If we have files but none are new
245 |                 st.info("All files have already been processed.")
246 |         
247 |         # Display document count
248 |         st.metric("Documents in Knowledge Base", st.session_state.document_count)
249 |         
250 |         # Display available sources
251 |         if st.session_state.sources:
252 |             st.subheader("Available Sources")
253 |             for source in st.session_state.sources:
254 |                 st.write(f"- {source}")
255 |     
256 |     # Main chat interface
257 |     st.header("💬 Chat with the AI")
258 |     
259 |     # Display all messages from the conversation so far
260 |     for msg in st.session_state.messages:
261 |         if isinstance(msg, ModelRequest) or isinstance(msg, ModelResponse):
262 |             for part in msg.parts:
263 |                 display_message_part(part)
264 |     
265 |     # Chat input
266 |     if user_input := st.chat_input("Ask a question about your documents..."):
267 |         # Display user message
268 |         with st.chat_message("user"):
269 |             st.markdown(user_input)
270 |         
271 |         # Display assistant response with streaming
272 |         with st.chat_message("assistant"):
273 |             message_placeholder = st.empty()
274 |             full_response = ""
275 |             
276 |             # Stream the response
277 |             generator = run_agent_with_streaming(user_input)
278 |             async for chunk in generator:
279 |                 full_response += chunk
280 |                 message_placeholder.markdown(full_response + "▌")
281 |             
282 |             # Final response without cursor
283 |             message_placeholder.markdown(full_response)
284 | 
285 | 
286 | if __name__ == "__main__":
287 |     asyncio.run(main())
288 | 


--------------------------------------------------------------------------------