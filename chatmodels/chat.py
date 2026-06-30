from dotenv import load_dotenv
import os

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model="mistral-small",   # ✅ working model
    temperature=0
)

response = model.invoke("write a poem about the ocean")

print(response.content)