from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from app.llm.client import LLMNotConfiguredError, generate_reply

router = APIRouter(prefix="/api", tags=["chat"])


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=10_000)


class ChatResponse(BaseModel):
    reply: str


@router.post("/chat", response_model=ChatResponse)
async def chat(payload: ChatRequest) -> ChatResponse:
    try:
        reply = await generate_reply(payload.message)
        return ChatResponse(reply=reply)
    except LLMNotConfiguredError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=502, detail="Falha ao consultar o modelo de IA.") from exc
