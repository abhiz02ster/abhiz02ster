***

# NLP-Based Database Search Agent — Usage Guide

***

## Overview

This app allows users to ask natural language questions about two databases (`chinook.db` and `northwind.db`) via a chat UI. The agent:

1. Uses keyword matching or natural language understanding to decide which database to query
2. Sends user query and database schema info to a local LLM (Gemini 3B via LM Studio) to generate SQL
3. Runs the generated SQL on the selected SQLite database
4. Returns formatted results in the chat UI

***

## Requirements

### Programming Language & Environment

- Python 3.8+
- SQLite3 (comes with Python)
- Internet connectivity is NOT required for LLM inference (LM Studio runs locally)

### Python Packages

Install dependencies via pip:

```bash
pip install fastapi uvicorn openai jinja2
```

***

## Key Application Modules

| Module                | Description                                               |
|-----------------------|-----------------------------------------------------------|
| `main.py`             | Starts FastAPI app, includes API and UI routers          |
| `config.py`           | Configuration with paths for databases, LM Studio API    |
| `db_router.py`        | Logic to choose which database to query (Chinook or Northwind)  |
| `lm_studio_client.py` | Connects to LM Studio and generates SQL from user query  |
| `chinook_client.py`   | Runs SQL queries against chinook.db                        |
| `northwind_client.py` | Runs SQL queries against northwind.db                      |
| `tool_registry.py`    | Core agent logic: orchestrates DB selection, SQL generation, and query execution |
| `mcp_router.py`       | FastAPI router for API chat endpoint                       |
| `ui_router.py`        | FastAPI router serving chat web UI (`chat.html`)          |
| `templates/chat.html` | Jinja2 HTML template for chat UI                           |
| `chinook.db`          | SQLite Chinook database                                    |
| `northwind.db`        | SQLite Northwind database                                  |

***

## Running the App

1. **Prepare databases:**

   Download `chinook.db` and `northwind.db` SQLite files and place them in the project root.

2. **Configure LM Studio:**

   Ensure LM Studio is running locally and listening at the configured URL (e.g., `http://localhost:1234/v1`).

3. **Install dependencies:**

   ```bash
   pip install fastapi uvicorn openai jinja2
   ```

4. **Start FastAPI server:**

   ```bash
   python main.py
   ```

5. **Access Chat UI:**

   Open your browser and go to:

   ```
   http://localhost:8000
   ```

***

## How to Use

- Type natural language questions about music (`chinook`) or business/sales (`northwind`) data.
- Examples:
  - `"List all albums by AC/DC"`  
  - `"Show all suppliers from USA"`  
  - `"How many tracks are in playlist 1"`  
  - `"What orders were shipped to Canada?"`
- The agent chooses the suitable database, generates SQL via LLM, executes the query, and shows results with source info and formatted tables.

***

## Notes & Tips

- Make sure the database files (`chinook.db`, `northwind.db`) are valid and accessible.
- The LLM prompt includes schema info—modify it if you add or rename tables/columns.
- Use clear descriptive questions for best LLM accuracy.
- Debug SQL by reviewing console output of generated queries.
- Enhance with additional modules (e.g., caching, more databases, complex NLP).

***

If you want, I can provide a complete setup script or detailed explanations of any component!

Sources
