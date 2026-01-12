import os

from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI

class EmailMessageSchema(BaseModel):
    subject: str
    content: str
    invalid_request: bool = Field(default=False)


    class SupervisorMessageSchema(BaseModel):
    content: str