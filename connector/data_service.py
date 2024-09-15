import sys
import os

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
    azure_batch_size: int = os.environ.get("AZURE_BATCH_SIZE")

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

    for batch in container_api.yield_from_file_batch(InputFile.FULL):
        for azure_batch in [
            batch[i : i + azure_batch_size]
            for i in range(0, len(batch), azure_batch_size)
        ]:
            addresses_to_process: list = [
                f"{data_item_prefix}_{address_index}: {', '.join([value for key, value in item.items() if key in source_columns_list and value])}"
                for address_index, item in enumerate(azure_batch)
            ]
            user_prompt: str = (
                f"{user_prompt_prefix} {data_separator.join(addresses_to_process)}"
            )

            result: ApiResponse = azure_openai_api.make_api_call(
                system_prompt, user_prompt
            )

            if not result.success:
                container_api.log(
                    LogLevel.ERROR, f"Error while making API call: {result.error}"
                )
                sys.exit(1)

            container_api.log(
                LogLevel.INFO,
                f"OpenAI API call successful. Used {result.usage.total_tokens} tokens: {result.usage.prompt_tokens} for prompt tokens and {result.usage.completion_tokens} for completion tokens",
            )

            for i, product in enumerate(azure_batch):
                product.update(
                    {
                        f"{new_column_prefix}_{key}": value
                        for key, value in result.data[f"{data_item_prefix}_{i}"].items()
                    }
                )

        container_api.append_many_to_file(OutputFile.OUTPUT, batch)
        container_api.log(LogLevel.SUCCESS, f"{len(batch)} items processed.")
