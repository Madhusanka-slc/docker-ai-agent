import re
from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from .models import ChatMessagePayload, ChatMessage, ChatMessageList
from api.db import get_session
from typing import List

router = APIRouter()

@router.get("/")
def chat_health():
    return {"message": "Chat API is healthy"}

# curl http://localhost:8080/api/chats/recent/
@router.get("/recent/", response_model=List[ChatMessageList])
def chat_list_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    result = session.exec(query).fetchall()[:2]
    return result


# curl -X POST -d '{message: "Hello"}' -H "Content-Type: application/json" http://localhost:8000/api/chats/
# HHTP POST -> payload = {"message": "Hello"}
#  curl -X POST -H "Content-Type: application/json" -d "{\"message\": \"Hello\"}" http://localhost:8000/api/chats/

@router.post("/", response_model=ChatMessage)
def chat_create_message(payload: ChatMessagePayload, session: Session = Depends(get_session)):
    # Placeholder for message handling logic
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj