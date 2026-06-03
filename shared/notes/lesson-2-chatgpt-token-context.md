# Lesson 2 - Tokens, Context Windows and Embeddings

## Tokens

Tokens are chunks of text processed by the model.

Examples:

"Terraform is awesome"

May become:

* Terraform
* is
* awesome

or smaller sub-word pieces.

## Context Window

The maximum amount of information a model can consider during a conversation.

Examples:

* 8K tokens
* 32K tokens
* 128K tokens

## Embeddings

Embeddings convert text into numerical vectors.

Purpose:

* Semantic search
* Similarity matching
* RAG systems

## Example

These concepts are close in embedding space:

* Terraform
* Azure Bicep
* CloudFormation

This concept is farther away:

* Banana

## Key Takeaways

* Tokens are the language of LLMs.
* Context windows limit how much information the model remembers.
* Embeddings enable semantic search.
