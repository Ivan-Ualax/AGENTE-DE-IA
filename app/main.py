from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.chat import router as chat_router
from app.core.config import get_settings

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

settings = get_settings()
app = FastAPI(title=settings.app_name, version="0.1.0")
app.include_router(chat_router)
app.mount("/static", StaticFiles(directory=FRONTEND_DIR), name="static")


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/", include_in_schema=False)
async def index() -> FileResponse:
    return FileResponse(FRONTEND_DIR / "index.html")
