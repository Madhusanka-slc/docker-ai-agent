import os

from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class EmailMessage(BaseModel):
    subject: str
    contents: str
    invalid_request: bool = Field(default=False)

OPENAI_MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME", "ai/gemma3")
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")   

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

openai_params = {
    "model": OPENAI_MODEL_NAME,
    "base_url": OPENAI_BASE_URL,
    "api_key": OPENAI_API_KEY,    
}

if OPENAI_BASE_URL:
    openai_params["base_url"] = OPENAI_BASE_URL

llm_base = ChatOpenAI(**openai_params)

llm = llm_base.with_structured_output(EmailMessage)

messages = [
    (
        "system",
        "You are a helpful assistant for research and composing plaintext emails.Do not use markdown in your responses.only respond with the plaintext.",
    ),
    ("human", "Create and email about the benefits of coffee. Do not use markdown in your response.only respond with the plaintext."),
]

response = llm.invoke(messages)

print(response)


