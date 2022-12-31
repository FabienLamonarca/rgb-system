from logging import getLogger
from app.services.kafka import KafkaClient
from app.settings import get_settings

settings = get_settings()
logger = getLogger()
       

async def getKafkaClient() -> KafkaClient:
    client = KafkaClient(settings.kafka_host, settings.kafka_port)
    try:
        yield client
    finally:
        client.close()
        
