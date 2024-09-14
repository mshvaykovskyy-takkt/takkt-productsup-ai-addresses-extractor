import sys
import os
import json

from .container_api import (
    ContainerApi,
    OutputFile,
    LogLevel,
    InputFile,
)
from .container_utils import AzureOpenAIApi, ApiResponse

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

    source_columns_list: list = [field.strip() for field in source_columns.split(",")]

    azure_openai_api: AzureOpenAIApi = AzureOpenAIApi(
        model=ai_model,
        endpoint=azure_openai_endpoint,
        api_key=azure_openai_key,
        api_version=azure_openai_api_version,
    )

    for batch in container_api.yield_from_file_batch(InputFile.FULL, 50):
        addresses_to_process: list = []

        for address_index, item in enumerate(batch):
            valid_values = [
                value
                for key, value in item.items()
                if key in source_columns_list and value
            ]
            concatenated_address: str = ", ".join(valid_values)
            concatenated_address = (
                f"{data_item_prefix}_{address_index}: {concatenated_address}"
            )
            addresses_to_process.append(concatenated_address)

        user_prompt: str = (
            f"{user_prompt_prefix} {data_separator.join(addresses_to_process)}"
        )

        result: ApiResponse = azure_openai_api.make_api_call(system_prompt, user_prompt)

        if not result.success:
            container_api.log(
                LogLevel.ERROR, "Error while making API call: " + result.error
            )
            sys.exit(1)

        container_api.log(
            LogLevel.SUCCESS, "OpenAI API call successful. Used: " + str(result.usage.total_tokens)
        )
        container_api.log(LogLevel.DEBUG, "API response: " + json.dumps(result.data))

        # product[new_column] = product[source_column]

        container_api.append_many_to_file(OutputFile.OUTPUT, batch)
