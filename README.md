
# 🤖 Automated GitHub Code Review System with GenAI,RAG & Azure LLM

This project automates code reviews by integrating GitHub REST APIs, Azure cloud services, and a **Retrieval-Augmented Generation (RAG)** architecture powered by a **cloud-hosted Large Language Model (LLM)**. It contextualizes incoming pull requests using historical review data to provide intelligent, automated feedback.

---

## 🚀 Features

- Retrieves pull request (PR) files and review comments using GitHub REST APIs
- Stores structured data in JSON format for easy indexing
- Indexes review data in Azure for scalable, fast retrieval
- Implements a RAG architecture to inject contextual data into the LLM
- Uses the indexed historical review data to generate relevant, automated code review suggestions

---

## 🛠️ Tech Stack

- **GitHub REST API** – PR file content and review comment extraction  
- **Azure** – For storing and indexing data  
- **RAG Architecture** – Combines retrieval and generation for context-aware responses  
- **Cloud-hosted LLM (Azure OpenAI GPT)** – Performs actual code review generation  
- **Python** – Core implementation language  

---


