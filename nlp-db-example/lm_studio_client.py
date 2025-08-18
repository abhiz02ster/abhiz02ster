#!/usr/bin/python3

import re
from openai import OpenAI
from config import LM_STUDIO_API_BASE, LM_STUDIO_API_KEY, LM_STUDIO_MODEL

client = OpenAI(base_url=LM_STUDIO_API_BASE, api_key=LM_STUDIO_API_KEY)

def clean_sql(sql_text):
    sql_text = re.sub(r'```[\w]*\n?', '', sql_text)
    sql_text = sql_text.replace('```', '')
    return sql_text.strip()

def get_sql_from_llm(user_query, db_hint=None):
    if db_hint == "chinook":
        schema_info = '''
DATABASE: Chinook (Music Store)
Tables and key columns:
- Albums(AlbumId, Title, ArtistId)
- Artists(ArtistId, Name)
- Customer(CustomerId, FirstName, LastName, Country)
- Invoice(InvoiceId, CustomerId, InvoiceDate, BillingCountry)
- InvoiceLine(InvoiceLineId, InvoiceId, TrackId, UnitPrice, Quantity)
- Track(TrackId, Name, AlbumId, MediaTypeId, GenreId)
- MediaType(MediaTypeId, Name)
- Genre(GenreId, Name)
- Playlists(PlaylistId, Name)
- PlaylistTrack(PlaylistId, TrackId)
'''
    elif db_hint == "northwind":
        schema_info = '''
DATABASE: Northwind (Business/Trading)
Tables and key columns:
- Customers(CustomerID, CompanyName, Country)
- Employees(EmployeeID, LastName, FirstName, City)
- Products(ProductID, ProductName, CategoryID, SupplierID, UnitPrice)
- Categories(CategoryID, CategoryName, Description)
- Orders(OrderID, CustomerID, EmployeeID, OrderDate, ShipCountry)
- OrderDetails(OrderID, ProductID, Quantity, UnitPrice, Discount)
- Suppliers(SupplierID, CompanyName, Country)
- Shippers(ShipperID, CompanyName, Phone)
'''
    else:
        schema_info = "ERROR: No database specified"

    prompt = f"""You are generating SQLite queries for a specific database ONLY.

{schema_info}

IMPORTANT: Use ONLY the tables listed above for the {db_hint} database.

User question: {user_query}

Generate ONLY the SQL query using the correct {db_hint} database tables. No explanations. No markdown."""

    response = client.chat.completions.create(
        model=LM_STUDIO_MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    raw_sql = response.choices[0].message.content.strip()
    return clean_sql(raw_sql)

