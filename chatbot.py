# chatbot.py
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load environment variables from .env file
load_dotenv()

# Initialize the Groq LLM client
llm = ChatGroq(
    model="llama3-8b-8192",
    temperature=0.3,
    max_tokens=300,
    timeout=15,
    max_retries=2
)

def get_chat_response(message: str) -> str:
    try:
        result = llm.invoke(message)
        return result.content
    except Exception as e:
        return f"Error: {str(e)}"
