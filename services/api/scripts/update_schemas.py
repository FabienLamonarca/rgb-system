import json
import logging
from logging.config import dictConfig
import os
import sys
import requests
import yaml



if __name__ == '__main__':
    
    with open("logger.yml", "r") as config_file:
        dictConfig(yaml.load(config_file, Loader=yaml.FullLoader))
    logger = logging.getLogger()
    
    schema_reg_host = os.getenv("kafka_registry_host")
    schema_reg_port = os.getenv("kafka_registry_port")
    base_uri = f"http://{schema_reg_host}:{schema_reg_port}"
    
    schemas_file_path = "resources/schemas.json"
    responses = []
    
    with open(schemas_file_path) as schema_file:
        schemas = json.load(schema_file)
        for schema_data in schemas:
            name = schema_data["name"]
            key_or_value = schema_data["type"]
            schema = schema_data["schema"]

            res = requests.post(
                url=f'{base_uri}/subjects/{name}-{key_or_value}/versions',
                data=json.dumps({
                'schema': json.dumps(schema)
                })
            ).json()
            responses.append({f"{name}-{key_or_value}": res})
    logger.info(responses)
    sys.exit(0)