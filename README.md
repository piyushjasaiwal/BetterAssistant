# BetterAssistant

An AI-powered assistant that works via **Command Line Interface (CLI)** and provides **REST API endpoints** for programmatic access (e.g., Postman).  

The agent can answer questions by performing a web search using Tavily, then summarising the web results extracted using  a summarisation pipeline which makes use of **facebook/bart-large-cnn** model to create a curated response for the user. 

Once the session is completed it saves the chat history in .txt format for user to reference later.

---

## Langgraph Workflow for the agent
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
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Features
- Interactive CLI interface for conversations.
- REST API for integration with Postman or other tools.
- Web search capability using Tavily.
- Context-aware summarisation of response to create curated well structured response.
- Uses chroma db to store embedding for query and responses for faster retreival of responses next time similar statament is queried.
- Provides user with an option to save chat to refer later
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

### Using the Agent Via CLI

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

- ChromaDB is initialised as soon as the first query is made by the user and a folder chroma_store is created at the root

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

### Using the Agent Via API Endpoints
Run the Flask app using command
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

- ChromaDB is initialised as soon as the first query is made by the user and a folder chroma_store is created at the root

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

[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/piyushjasaiwal)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/piyush-jasaiwal/)
