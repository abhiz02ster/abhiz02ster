***

# Web-Based Chat + Web Search Agent

An agentic AI web application that allows users to chat naturally, get answers from a local LLM, retrieve information from local notes, and access live web search results—all via a browser-based interface.

***

## Features

- **Conversational Web UI:** Chat seamlessly with the agent in your browser.
- **Local LLM Support:** Uses a local LLM (e.g., Gemini 3B via LM Studio) for most AI responses.
- **Internet/Web Search Tool:** If the LLM or fact base cannot answer, the agent performs a live web search (e.g., via DuckDuckGo).
- **Local Fact Store:** Returns answers from a personal fact/notes file if found.
- **Agentic Tool Registry:** Modular system—easy to add new tools (calculator, database queries, etc).
- **Open, Extensible Codebase:** Add your own endpoints, tools, or LLMs!

***

## Requirements

- Python 3.8+
- Node.js (optional: for front-end building, if using advanced UI)
- [LM Studio](https://lmstudio.ai/) running locally with a supported model (e.g., Gemini 3B)
- Internet connection for live web search

### Python Packages

```bash
pip install fastapi uvicorn openai jinja2 duckduckgo-search
```

***

## File Overview

| File / Folder           | Description                                                   |
|-------------------------|---------------------------------------------------------------|
| `main.py`               | App entry point. Launches FastAPI and includes all routers    |
| `ui_router.py`          | Serves the chat UI and input endpoints                        |
| `mcp_router.py`         | Modular Control Protocol router—handles agentic logic         |
| `tool_registry.py`      | Main agent: routes requests to LLM, search, fact store, tools |
| `fact_store.py`         | Manages the local fact/notes database                         |
| `lm_studio_client.py`   | Connects to local LLM via LM Studio API                      |
| `search_tools.py`       | Implements live internet search via DuckDuckGo                |
| `templates/chat.html`   | Browser-based chat interface (Jinja2 HTML)                    |
| `fact_notes.json`       | Your local knowledge base file (plain JSON)                   |

***

## Running the App

1. **Start LM Studio**  
   Download and run LM Studio, make sure it's running (e.g., at `http://localhost:1234/v1`), and load your local model (e.g., Gemini 3B).

2. **Run FastAPI Server:**

   ```bash
   python main.py
   ```

3. **Open Browser UI:**

   Visit [http://localhost:8000](http://localhost:8000)

***

## Usage Examples

- “Summarize the latest NASA Mars news”
- “What is the capital of Australia?”
- “Add 43 and 59” (if calculator tool is added)
- “Summarize note about database schema” (will pull from fact store if available)
- If the answer cannot be generated, the system will perform an automatic web search for you.

***

## Adding Your Own Tools

Just implement a new tool module, register it with the agent’s tool registry, and update the routing logic in `tool_registry.py`.

***

## Extending or Customizing

- **Change the LLM:** Plug your own model by updating `lm_studio_client.py`
- **Change Fact File:** Edit/add entries in `fact_notes.json`
- **Improve the UI:** Adjust or replace `templates/chat.html`

***

## Troubleshooting

- **LM Studio not running?** The LLM will not answer questions unless LM Studio is active with your selected model.
- **Web search not working?** Ensure you have network connectivity and haven’t hit DuckDuckGo’s usage limits.
- **Fact base not queried?** Add facts/notes in plain JSON, matching likely user phrasing.

***

Feel free to fork and build on this project—PRs and module suggestions welcome!

Sources
