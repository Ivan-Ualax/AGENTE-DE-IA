import httpx

from app.core.config import get_settings
from app.core.prompts import SYSTEM_PROMPT


class LLMNotConfiguredError(RuntimeError):
    pass


async def generate_reply(message: str) -> str:
    settings = get_settings()

    if not settings.llm_api_key:
        raise LLMNotConfiguredError(
            "A chave da API ainda não foi configurada. Copie .env.example para .env e informe LLM_API_KEY."
        )

    payload = {
        "model": settings.llm_model,
        "instructions": SYSTEM_PROMPT,
        "input": message,
    }
    headers = {
        "Authorization": f"Bearer {settings.llm_api_key}",
        "Content-Type": "application/json",
    }

    async with httpx.AsyncClient(timeout=60.0) as client:
        response = await client.post(
            "https://api.openai.com/v1/responses",
            headers=headers,
            json=payload,
        )
        response.raise_for_status()
        data = response.json()

    for item in data.get("output", []):
        for content in item.get("content", []):
            if content.get("type") == "output_text" and content.get("text"):
                return content["text"].strip()

    raise RuntimeError("A API não retornou texto.")
