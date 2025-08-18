#!/usr/bin/python3

def choose_database(user_query):
    # More comprehensive keywords
    chinook_keywords = [
        "albums", "track", "invoice", "media", "playlists", "artists", 
        "genre", "music", "song", "band", "purchase", "billing"
    ]
    northwind_keywords = [
        "order", "product", "category", "supplier", "employee", 
        "shipper", "region", "freight", "company", "territory", 
        "discount", "quantity", "unit", "ship"
    ]

    text = user_query.lower()
    chinook_score = sum([1 for kw in chinook_keywords if kw in text])
    northwind_score = sum([1 for kw in northwind_keywords if kw in text])
    
    print(f"Query: {user_query}")
    print(f"Chinook score: {chinook_score}, Northwind score: {northwind_score}")
    
    if chinook_score > northwind_score:
        return "chinook"
    elif northwind_score > chinook_score:
        return "northwind"
    else:
        # If ambiguous, ask user or default to northwind for business queries
        return "northwind"  # Change from None to northwind

