#!/usr/bin/python3

from db_router import choose_database
from chinook_client import query_chinook
from northwind_client import query_northwind
from lm_studio_client import get_sql_from_llm

def agent_handle_db_query(user_query):
    db = choose_database(user_query)
    print(f"Selected database: {db}")  # Debug output
    
    if not db:
        db = "northwind"  # Default fallback
    
    sql = get_sql_from_llm(user_query, db)
    print(f"Generated SQL: {sql}")  # Debug output
    
    if db == "chinook":
        result = query_chinook(sql)
    else:
        result = query_northwind(sql)

    return {
        "database": db,
        "sql": sql,
        "result": result
    }

