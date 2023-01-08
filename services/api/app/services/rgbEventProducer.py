import json
import logging

from confluent_kafka.avro import AvroProducer
from app.settings import get_settings
from confluent_kafka import avro
from avro.errors import AvroTypeException

settings = get_settings()    
logger = logging.getLogger()

class rgbEventProducer(object):
    topic = "rgb-event"
    config = {
        "bootstrap.servers": f"{settings.kafka_host}:{settings.kafka_port}",
        "schema.registry.url": f"http://{settings.kafka_registry_host}:{settings.kafka_registry_port}"
    }
    key_schema = avro.load("resources/avro/rgbEventKey.avsc")
    value_schema = avro.load("resources/avro/rgbEventValue.avsc")
    
    def __init__(self) -> None:
        self.producer = AvroProducer(
            self.config, 
            default_key_schema=self.key_schema, 
            default_value_schema=self.value_schema
        )
        
    def produce(self, key, value):  
        try:
            self.producer.produce(topic = self.topic, key = key, value = value)
            self.producer.flush()
            return True
            
        except AvroTypeException as avroException:
            logger.error(avroException)
            logger.debug(f"key -> {key}")
            logger.debug(f"key_schema ->{self.key_schema.canonical_form}")
            logger.debug(f"value -> {value}")
            logger.debug(f"value_schema ->{self.value_schema.canonical_form}")
            raise AvroTypeException
        