import json
from logging import getLogger
import random
import sys
import uuid
from app.models.events import rgbEvent

from kafka import KafkaProducer


    
logger = getLogger()

class KafkaClient(object):
    host: str
    port: int 
    producer: KafkaProducer
    rgb_event_topic = "rgb-topic"
    
    def serializer(self, v):
        return json.dumps(v).encode('utf-8')
    
    def __init__(self, host:str, port:int):
        self.host = host
        self.port = port        
        self.producer = KafkaProducer(
            bootstrap_servers=f"{self.host}:{self.port}", 
            value_serializer=self.serializer
        )
        
    def produce_event(self, event:rgbEvent):
        for _ in range(event.count):
            key = str.encode(event.color)
            value = {
                "id": str(uuid.uuid4()),
                "color": event.color,
                "data": random.randrange(sys.maxsize)
            }
            self.producer.send(self.rgb_event_topic, key=key, value=value)
    
    def close(self):
        if self.producer:
            self.producer.close()
