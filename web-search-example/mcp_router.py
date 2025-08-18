#!/usr/bin/python3

from fastapi import APIRouter
from pydantic import BaseModel
from tool_registry import tool_registry

router = APIRouter()

class MCPRequest(BaseModel):
    command: str
    message: str

class MCPResponse(BaseModel):
    reply: str

@router.post("/mcp", response_model=MCPResponse)
async def mcp_endpoint(req: MCPRequest):
    handler = tool_registry.get(req.command)
    if not handler:
        return MCPResponse(reply=f"Error: Unknown command '{req.command}'")
    reply = handler(req.message)
    return MCPResponse(reply=reply)

