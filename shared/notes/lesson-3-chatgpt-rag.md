# Lesson 3 - Retrieval Augmented Generation (RAG)

## Problem

LLMs do not automatically know:

* Internal repositories
* Company standards
* Private documents

## Solution

Retrieval Augmented Generation (RAG)

## Flow

User Question
↓
Retrieve Documents
↓
Provide Context
↓
LLM Generates Response

## Components

### Documents

* Standards
* Policies
* Runbooks
* Internal Documentation

### Chunking

Large documents are split into smaller sections.

### Embeddings

Chunks are converted into vectors.

### Vector Database

Stores embeddings for retrieval.

## Benefits

* Up-to-date information
* No model retraining
* Better enterprise adoption

## Key Takeaways

RAG extends knowledge without modifying the model.
