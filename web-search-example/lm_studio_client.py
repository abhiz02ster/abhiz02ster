#!/usr/bin/python3

from openai import OpenAI
from config import LM_STUDIO_API_BASE, LM_STUDIO_API_KEY, LM_STUDIO_MODEL

client = OpenAI(base_url=LM_STUDIO_API_BASE, api_key=LM_STUDIO_API_KEY)

def query_llm(messages):
    completion = client.chat.completions.create(
        model=LM_STUDIO_MODEL,
        messages=messages,
        temperature=0.7
    )
    return completion.choices[0].message.content

