from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import Union



from app.settings import get_settings

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class rgbEvent(BaseModel):
    color: str
    count: int

@app.get("/")
async def root():
    return RedirectResponse("/docs")


@app.get("/info")
async def display_settings():
    return get_settings().dict()

@app.post("/event", status_code=status.HTTP_200_OK)
async def eventLogging(event: rgbEvent):
    return { "action": "save", "event": event.json() }