#!/usr/bin/python3

from fastapi import APIRouter
from pydantic import BaseModel
from tool_registry import agent_handle_db_query

router = APIRouter()

class DBQueryRequest(BaseModel):
    message: str

class DBQueryResponse(BaseModel):
    database: str
    sql: str
    result: dict

@router.post("/dbquery", response_model=DBQueryResponse)
async def db_query_endpoint(req: DBQueryRequest):
    out = agent_handle_db_query(req.message)
    return DBQueryResponse(**out)

