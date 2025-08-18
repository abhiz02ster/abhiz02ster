#!/usr/bin/python3

import difflib
from duckduckgo_search import DDGS
from fact_store import load_facts

fact_notes = load_facts()

def find_best_local_match(query, cutoff=0.6):
    matches = difflib.get_close_matches(query, fact_notes.keys(), n=1, cutoff=cutoff)
    if matches:
        best = matches[0]
        return best, fact_notes[best]
    return None, None

def search_internet_duckduckgo(query):
    with DDGS() as ddgs:
        results = list(ddgs.text(query, max_results=3))
    if results:
        snippets = [r.get("body", "") for r in results]
        return " ".join(snippets).strip()
    return "No relevant results found from DuckDuckGo."

