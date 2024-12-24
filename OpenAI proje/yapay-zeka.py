import openai
import asyncio

# OpenAI API anahtarını buraya ekle
openai.api_key = 'your Open Ai Code'

prompt = input("Prompt: ")

response = openai.ChatCompletion.create(
    model = "gpt-3.5-turbo",
    messages = [{"role":"user","content":prompt}]
)

print(response.choices[0]["message"]["content"])