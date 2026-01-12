from api.ai.schemas import EmailMessageSchema
from api.ai.llms import get_openai_llm

def generate_email_message(query: str) -> EmailMessageSchema:
    llm = get_openai_llm()
    llm_structured = llm.with_structured_output(EmailMessageSchema)

    messages = [
        (
            "system",
            "You are a helpful assistant for research and composing plaintext emails.Do not use markdown in your responses.only respond with the plaintext.",
        ),
        ("human", f"{query} Do not use markdown in your response.only respond with the plaintext."),
    ]

    return llm_structured.invoke(messages)