import logging

from confluent_kafka.avro import AvroProducer
from app.settings import get_settings
from confluent_kafka import avro
from avro.errors import AvroTypeException

settings = get_settings()    
logger = logging.getLogger()

class rgbEventProducer(AvroProducer):
    topic = "rgb-event"
    config = {
        "bootstrap.servers": f"{settings.kafka_host}:{settings.kafka_port}",
        "schema.registry.url": f"http://{settings.kafka_registry_host}:{settings.kafka_registry_port}",
        "compression.type": "gzip"
    }
    key_schema = avro.load("resources/avro/rgb_event_key.avsc")
    value_schema = avro.load("resources/avro/rgb_event_value.avsc")
    
    def __init__(self, **kwargs) -> None:
        super().__init__(
            self.config, 
            default_key_schema=self.key_schema, 
            default_value_schema=self.value_schema,
            **kwargs
        )
        
    def produce(self, key, value):  
        try:
            super().produce(topic = self.topic, key = key, value = value)
            
        except AvroTypeException as avroException:
            logger.error(avroException)
            logger.debug(f"key -> {key}")
            logger.debug(f"key_schema ->{self.key_schema.canonical_form}")
            logger.debug(f"value -> {value}")
            logger.debug(f"value_schema ->{self.value_schema.canonical_form}")
            raise AvroTypeException
    