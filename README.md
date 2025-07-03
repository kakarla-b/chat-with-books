# chat-with-books

# Chat-with-books

This project is an AI-powered chatbot application designed to retrieve and answer user queries based on the content of uploaded books. It leverages embeddings and ChromaDB for semantic search, enabling users to have meaningful conversations with their data.

## Features

- Upload CSV files containing book data
- Automatically generates text embeddings for semantic understanding
- Ask natural language questions and receive accurate responses
- Uses ChromaDB as the vector store for document retrieval
- Clean and modular codebase with utility scripts for preprocessing and analysis

## Tech Stack

- **Python** for backend logic
- **ChromaDB** for storing and retrieving vector embeddings
- **OpenAI Embeddings** for generating semantic vectors
- **Pandas / NumPy** for data handling
- **dotenv** for managing environment variables
  
## Folder Structure
chat-with-books/
├── chatbot.py # Main chatbot interface

├── embedding_dataset.py # Embedding generator from text

├── retrive_data_chromadb.py # ChromaDB-based retriever

├── clener.py # Data cleaning utility

├── data_analysis.py # Book data analyzer

├── booktest.csv # Sample input data

├── book_analyze.csv # Analyzed book output

├── requirements.txt # Python dependencies

├── .env # API keys and configs (not committed)

└── README.md # Project documentation



