import sys
import os
import json

from .container_api import (
    ContainerApi,
    OutputFile,
    LogLevel,
    InputFile,
)

container_api = ContainerApi()


def extract_addresses():
    source_columns: str = os.environ.get("SOURCE_COLUMNS")

    ai_model: str = os.environ.get("AZURE_OPENAI_MODEL")
    azure_openai_endpoint: str = os.environ.get("AZURE_OPENAI_ENDPOINT")
    azure_openai_key: str = os.environ.get("AZURE_OPENAI_API_KEY")
    azure_openai_api_version: str = os.environ.get("AZURE_OPENAI_API_VERSION")
    system_prompt: str = os.environ.get("SYSTEM_PROMPT")
    user_prompt_prefix: str = os.environ.get("USER_PROMPT_PREFIX")

    data_separator: str = os.environ.get("DATA_SEPARATOR")
    data_item_prefix: str = os.environ.get("DATA_ITEM_PREFIX")
    new_column_prefix: str = os.environ.get("NEW_COLUMN_PREFIX")

    if (
        not source_columns
        or not ai_model
        or not azure_openai_endpoint
        or not azure_openai_key
        or not azure_openai_api_version
    ):
        container_api.log(
            LogLevel.ERROR,
            "Some settings are empty. Please check data service configuration in the platform",
        )
        sys.exit(1)

    container_api.log(LogLevel.DEBUG, f"System prompt: {system_prompt}")
    container_api.log(LogLevel.DEBUG, f"User prompt prefix: {user_prompt_prefix}")
    container_api.log(LogLevel.DEBUG, f"Data separator: {data_separator}")
    container_api.log(LogLevel.DEBUG, f"Data item prefix: {data_item_prefix}")
    container_api.log(LogLevel.DEBUG, f"New column prefix: {new_column_prefix}")

    source_columns_list: list = [field.strip() for field in source_columns.split(",")]
    container_api.log(LogLevel.INFO, f"Extract from columns {source_columns_list}")

    for batch in container_api.yield_from_file_batch(InputFile.FULL, 50):
        container_api.log(LogLevel.DEBUG, json.dumps(batch))

        container_api.log(LogLevel.DEBUG, f"Batch type: {type(batch)}")

        for id, product in enumerate(batch):
            # product[new_column] = product[source_column]
            container_api.log(LogLevel.DEBUG, id)
            container_api.log(LogLevel.DEBUG, json.dumps(product))

        container_api.append_many_to_file(OutputFile.OUTPUT, batch)
