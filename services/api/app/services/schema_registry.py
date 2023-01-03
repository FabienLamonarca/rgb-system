

import json
import logging

import requests
from app.settings import get_settings

logger = logging.getLogger()
settings = get_settings()

base_uri = f"http://{settings.kafka_registry_host}:{settings.kafka_registry_port}"


def update_schemas():
    responses = []
    with open(settings.schemas_path) as schema_file:
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
    return responses