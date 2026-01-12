import os

from langchain_openai import ChatOpenAI


OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME", "ai/gemma3")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")   

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

def get_openai_llm():
    openai_params = {
        "model": OPENAI_MODEL_NAME,
        "base_url": OPENAI_BASE_URL,
        "api_key": OPENAI_API_KEY,    
    }
    
    if OPENAI_BASE_URL:
        openai_params["base_url"] = OPENAI_BASE_URL
        return ChatOpenAI(**openai_params)