# SHARP — Semantic-Hybrid Augmented Retrieval Pipeline

SHARP (Semantic-Hybrid Augmented Retrieval Pipeline) demonstrates a hybrid Retrieval-Augmented Generation (RAG) approach that combines semantic search and keyword search to retrieve relevant information from PDF documents before generating an answer with a Large Language Model (LLM).

## Features

- PDF document upload and text extraction
- Text chunking
- Semantic embeddings using Sentence Transformers
- FAISS-based semantic retrieval
- TF-IDF keyword retrieval
- Hybrid search by combining semantic and keyword results
- Context-aware answer generation using an LLM

## Workflow

```text
PDF Document
   ↓
PDF Text Extraction
   ↓
Text Chunking
   ↓
Embeddings + FAISS Index
   ↓
Semantic Search ─────┐
                     ├──→ Hybrid Search → Context → LLM → Answer
Keyword Search ──────┘
```

## Repository Contents

The **SHARP** repository contains the implementation in **both Jupyter Notebook (`.ipynb`) and Python (`.py`) formats**.

- **`hybrid_search_pdf_QA_system.ipynb`** — Complete step-by-step implementation in Jupyter/Google Colab format.
- **Python files** — The notebook workflow is separated into modular Python files following the sequence of the implementation.

Both formats are available so the project can be explored interactively using the notebook or used as modular Python code.

## Python Files

```text
src/
├── 01_installation.py
├── 02_imports.py
├── 03_pdf_upload.py
├── 04_pdf_extraction.py
├── 05_text_chunking.py
├── 06_embedding_and_faiss.py
├── 07_semantic_search.py
├── 08_keyword_search.py
├── 09_hybrid_search.py
├── 10_llm_setup.py
└── 11_rag_generation.py
```

The numbered files follow the code-cell sequence of `hybrid_search_pdf_QA_system.ipynb`: installation → imports → PDF upload → extraction → chunking → embedding/indexing → semantic search → keyword search → hybrid search → LLM setup → answer generation.

## Technologies

- Python
- PyPDF
- Sentence Transformers
- FAISS
- NumPy
- Scikit-learn
- TF-IDF
- Hugging Face Transformers
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)

## Getting Started

Install the required dependencies:

```bash
pip install pypdf sentence-transformers faiss-cpu accelerate transformers scikit-learn numpy
```

The notebook can be opened in Google Colab or Jupyter. The Python modules can be used individually or integrated into an end-to-end pipeline.

## Purpose

This project is intended for learning and experimentation with hybrid information retrieval, combining semantic and keyword-based search to improve the relevance of retrieved context for question answering.

## License

This project is intended for educational and learning purposes.
