#!/usr/bin/python3

from search_tools import find_best_local_match, search_internet_duckduckgo
from lm_studio_client import query_llm

def handle_agentic_search(message: str) -> str:
    title, desc = find_best_local_match(message)
    if desc:
        return f"(From local facts) {desc}"

    system_prompt = "You are a helpful assistant with knowledge up to November 9, 2023. If you do not know the answer confidently, say 'I don't know.'"
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": message}
    ]
    llm_response = query_llm(messages).strip()

    # If LLM response indicates uncertainty or looks repetitive, fallback
    uncertain_phrases = [
        "i don't know", "i'm not sure", "as of november 9, 2023", 
        "my training data only goes up to", "i cannot provide", "sorry"
    ]

    if any(phrase in llm_response.lower() for phrase in uncertain_phrases):
        internet_result = search_internet_duckduckgo(message)
        return f"(From DuckDuckGo) {internet_result}"

    # Optional: also check if LLM repeats query or generic answers and fallback

    return f"(From LLM) {llm_response}"


tool_registry = {
    "agentic_search": handle_agentic_search,
}

