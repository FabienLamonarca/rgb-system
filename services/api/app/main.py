from app.services.schema_registry import update_schemas
from app.models.events import rgbEvent
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.responses import RedirectResponse
from app.dependencies import KafkaClient, getKafkaClient
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

@app.get("/")
async def root():
    return RedirectResponse("/docs")

@app.get("/info")
async def display_settings():
    return get_settings().dict()

@app.get("/schemas", status_code=status.HTTP_200_OK)
async def schemas():
    return update_schemas()

@app.post("/event", status_code=status.HTTP_200_OK)
async def eventLogging(event: rgbEvent, kafkaClient:KafkaClient=Depends(getKafkaClient)):
    if event.color in ["red", "green", "blue"]:
        kafkaClient.produce_event(event)
    else:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="Color not allowed")
    
    return { "action": "save", "event": event.json() }