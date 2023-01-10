import json
from logging import getLogger
import random
import sys
import uuid
from app.models.events import rgbEvent

from app.services.rgbEventProducer import rgbEventProducer
    
logger = getLogger()

class KafkaClient(object):
        
    def produce_event(self, event:rgbEvent):    
        producer: rgbEventProducer = rgbEventProducer()  
        for _ in range(event.count):
            key = event.color
            value = {
                "id": str(uuid.uuid4()),
                "color": event.color,
                "data": random.randrange(sys.maxsize)
            }
            producer.produce(key=key, value=value)
           
        producer.flush()


