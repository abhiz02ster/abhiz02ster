#!/usr/bin/python3

import sqlite3
from config import CHINOOK_DB_PATH

def query_chinook(sql):
    try:
        conn = sqlite3.connect(CHINOOK_DB_PATH)
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        conn.close()
        return {"columns": columns, "rows": data}
    except Exception as e:
        return {"error": str(e)}

