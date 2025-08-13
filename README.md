# BetterAssistant

An AI-powered assistant that works via **Command Line Interface (CLI)** and provides **REST API endpoints** for programmatic access (e.g., Postman).  

The agent can answer questions by performing a web search using Tavily, then summarising the web results extracted using a summarisation pipeline which makes use of **facebook/bart-large-cnn** model to create a curated response for the user. 

Once the session is completed, It saves the chat history in .txt format for user to reference later.

---

## LangGraph Workflow for the agent
<p align="center">
  <img src="assets/workflow.png" alt="Agent Workflow" />
</p>



## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [CLI](#cli)
  - [API](#api)
- [Author](#author)
---

## Features
- Interactive CLI for conversations.
- REST API for integration with Postman or other tools.
- Web search capability using Tavily.
- Context-aware summarisation of response to create curated, well-structured response.
- Uses ChromaDB to store embeddings for queries and responses for faster retrieval of responses next time similar statement is queried.
- Provides the user with an option to save chat to refer to later
- Easy to extend with new agents or workflows.

---

## Requirements
- **Python** >= 3.11
- Dependencies listed in `conda_environment.yaml`
- API keys for:
  - Tavily API

---

## Installation
```bash
# Clone the repository
https://github.com/piyushjasaiwal/BetterAssistant.git
cd BetterAssistant

# Install dependencies
conda env create -f conda_environment.yaml

# Activate conda environment
conda activate betterAssistant
```
# Configuration

Create a `.env` file at the root of the folder and populate it with the API keys

```bash
tavily_api_key = 
```

## Usage

### Using the Agent via CLI

Run the CLI app using command
```bash
python cli.py
```
- Welcome Screen for the CLI interface
<p align="center">
  <img src="assets/welcome_screen_cli.png" alt="welcome_screen_cli" />
</p>

- Demo query and response from the user
<p align="center">
  <img src="assets/query_response.png" alt="query response" />
</p>

- ChromaDB is initialized as soon as the first query is made by the user and a folder chroma_store is created at the root

<p align="center">
  <img src="assets/chroma_store.png" alt="chroma store" width=600 />
</p>

- Exit screen once the conversation ends
<p align="center">
  <img src="assets/exit_flow.png" alt="exit flow" />
</p>

- Saved chat logs in the logs folder
<p align="center">
  <img src="assets/chat_logs.png" alt="Chat logs" width=600 />
</p>

### Using the Agent via API Endpoints
Run the Flask app using the command
```bash
python flask_app.py
```
The server will start at `http://127.0.0.1:5000`

<p align="center">
  <img src="assets/flask_server.png" alt="Flask server logs"  />
</p>

### API Endpoints
| Method | Endpoint                                           | Description                   | Example Payload             |
|--------|-----------------------------------------|-------------------------------|-----------------------------|
| POST   | `/api/v1/query`                         | Send a question to the agent  | `{"query": "what is a person"}`|
| POST   | `/api/v1/export?filename=<file-name>`   | Export the chat logs          | —                              |
| GET    | `/`                                     | Check server health           | —                              |

### Example API Usage by Postman

- Check Server Health
<p align="center">
  <img src="assets/server_health.png" alt="server health" width=800/>
</p>

- Send a question to agent
<p align="center">
  <img src="assets/server_query.png" alt="server query" width=800/>
</p>

- ChromaDB is initialized as soon as the first query is made by the user and a folder chroma_store is created at the root

<p align="center">
  <img src="assets/chroma_store.png" alt="chroma store" width=600/>
</p>

- Export chat logs
<p align="center">
  <img src="assets/server_export.png" alt="chat export"  width=800/>
</p>

- Saved chat logs in the logs folder
<p align="center">
  <img src="assets/chat_logs.png" alt="Chat logs" width=600/>
</p>

## 👤 Author

**Piyush Jasaiwal**   

<img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" alt="GitHub" height="20"/> [github.com/piyushjasaiwal](https://github.com/piyushjasaiwal)  
<img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/linkedin.svg" alt="LinkedIn" height="20"/> [linkedin.com/in/piyush-jasaiwal](https://www.linkedin.com/in/piyush-jasaiwal/)


