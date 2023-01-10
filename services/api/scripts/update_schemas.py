import json
import logging
from logging.config import dictConfig
import os
import sys
import requests
import yaml

def register_schema(name, key_or_value, schema):
    return {
        f"{name}-{key_or_value}": requests.post(
            url=f'{base_uri}/subjects/{name}-{key_or_value}/versions',
            data=json.dumps({
            'schema': json.dumps(schema)
        })).json()
    }

if __name__ == '__main__':
    
    with open("logger.yml", "r") as config_file:
        dictConfig(yaml.load(config_file, Loader=yaml.FullLoader))
    logger = logging.getLogger()
    
    schema_reg_host = os.getenv("kafka_registry_host")
    schema_reg_port = os.getenv("kafka_registry_port")
    
    if not schema_reg_host or not schema_reg_port:
        logger.error("schema reg not defined")
        sys.exit(-1)
        
    base_uri = f"http://{schema_reg_host}:{schema_reg_port}"
    
    schemas_folder_path = "resources/avro"
    responses = []
    
    schemas = [
        {"name": "rgbEvent", "type": "key"},
        {"name": "rgbEvent", "type": "value"}
    ]
    
    for schema in schemas:
        name = schema["name"]
        key_or_value = schema["type"]
        filename = f"{name}{key_or_value.capitalize()}.avsc"
        with open(f"{schemas_folder_path}/{filename}") as schema_file:
            responses.append(register_schema(name, key_or_value, json.load(schema_file)))

    logger.info(responses)

    sys.exit(0)