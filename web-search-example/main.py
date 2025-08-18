#!/usr/bin/python3

import uvicorn
from fastapi import FastAPI
from mcp_router import router as mcp_router
from ui_router import router as ui_router

app = FastAPI(title="Agentic LM Studio Chat Server")

app.include_router(mcp_router)
app.include_router(ui_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

