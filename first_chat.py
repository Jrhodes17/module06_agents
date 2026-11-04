# first_chat.py
# Author: James Rhodes

from ollama import chat

MODEL_NAME = "granite4.1:3b"

INSTRUCTIONS = """You are Brenard, a support assistant for Bayside Outfitters.
Answer in one short sentence."""

messages = [
    {"role": "system", "content": INSTRUCTIONS},
    {"role": "user", "content": "What are your store hours?"},
]

response = chat(model=MODEL_NAME, messages=messages)
print(response.message.content)
