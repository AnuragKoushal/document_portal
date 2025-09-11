# Document Analysis, Chat & Comparison Portal

**Module 2 – GenAI LLMOPS**

A comprehensive portal for advanced document analysis, comparison, and interactive chat using GenAI and LLMOps principles.

---

## Table of Contents

- [Project Overview](#project-overview)  
- [Features](#features)  
- [Architecture & Implementation](#architecture--implementation)  
- [Workflow](#workflow)  
- [Performance & Optimization](#performance--optimization)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Screenshots](#screenshots)  
- [CI/CD & Deployment](#cicd--deployment)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Project Overview

This project provides a portal for analyzing, comparing, and interacting with documents using large language models (LLMs). It supports single-document and multi-document QnA, session memory for chat history, and document similarity/diff detection for side-by-side comparisons.  

It is designed with performance and scalability in mind, integrating advanced optimization techniques and modern deployment practices.

---

## Features

### Chat & Comparison
- Session memory and chat history management  
- Single-document QnA interface  
- Multi-document chat with vector retriever across all sources  
- Side-by-side document similarity and difference detection  

### Text Processing Tools
- Text extraction from PDFs and DOCX using PyMuPDF, PDFMiner, Unstructured, Python-Docx  

### Evaluation & Testing
- RAG (Retrieval-Augmented Generation) pipeline evaluation  
- End-to-end testing: Upload → Ask → Compare → View Sources  

---

## Architecture & Implementation

### Frontend
- Streamlit or Gradio-based UI for document upload, chat, and comparison  

### Backend
- FastAPI for model serving and API endpoints  

### Core Logic
- Document comparison and similarity detection  
- Chat history management and session memory  
- Vector-based retrieval for multi-document interaction  

### Architecture Diagram
![Architecture Diagram](images/architecture-diagram.png)  
*Replace with your actual architecture image.*

---

## Workflow

1. Upload documents  
2. Ask questions in chat interface  
3. Compare documents side by side  
4. View sources and results  

![Workflow Diagram](images/workflow-diagram.png)  
*Replace with your actual workflow diagram.*

---

## Performance & Optimization

- Local LLM execution using **vLLM**, **Groq**, or quantized models  
- Cache-Augmented Generation (CAG) for repeated queries  
- Optimized for speed and memory efficiency  

---

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/document-analysis-portal.git

# Navigate into the project directory
cd document-analysis-portal

# Install dependencies
pip install -r requirements.txt
