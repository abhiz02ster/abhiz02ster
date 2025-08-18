#!/usr/bin/python3

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from tool_registry import agent_handle_db_query

router = APIRouter()
templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    database: str
    sql: str
    result: dict

@router.get("/", response_class=HTMLResponse)
async def homepage(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(req: ChatRequest):
    out = agent_handle_db_query(req.message)
    return ChatResponse(**out)

