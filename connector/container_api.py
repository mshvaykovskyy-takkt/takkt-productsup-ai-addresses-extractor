import typing

from enum import StrEnum

from .cde_container_api_client import Client

from .cde_container_api_client.models import (
    WriteToOutputFileInput,
    WriteToOutputFileInputMeta,
    WriteToOutputFileInputDataItem,
    WriteToOutputFileResponse400,
)
from .cde_container_api_client.api.file import write_to_output_file

from .cde_container_api_client.models import (
    WriteLogInput,
    WriteLogInputContext,
    WriteLogResponse400,
)
from .cde_container_api_client.api.log import write_log

from .cde_container_api_client.api.file import (
    read_input_file_next,
    read_input_file_next_batch,
)
from .cde_container_api_client.models import ReadInputFileNextBatchResponse400


class ContainerApiError(Exception):
    def __init__(self, message: str):
        self.message = message


class OutputFile(StrEnum):
    OUTPUT = "output"
    FEEDBACK = "feedback"


class InputFile(StrEnum):
    FULL = "full"


class LogLevel(StrEnum):
    SUCCESS = "success"
    DEBUG = "debug"
    INFO = "info"
    NOTICE = "notice"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"
    ALERT = "alert"
    EMERGENCY = "emergency"
    REPORT = "report"


class ContainerApi:
    client: Client

    def __init__(self):
        self.client = Client(base_url="http://cde-container-api")

    def append_to_file(
        self, file: OutputFile, item: dict, separator: typing.Optional[str] = None
    ):
        return self.append_many_to_file(file, [item], separator)

    def append_many_to_file(
        self, file: OutputFile, items: list, separator: typing.Optional[str] = None
    ):
        body = WriteToOutputFileInput()
        body.data = [WriteToOutputFileInputDataItem.from_dict(item) for item in items]

        if separator is not None:
            meta = WriteToOutputFileInputMeta()
            meta.separator = separator
            body.meta = meta

        response = write_to_output_file.sync(file, client=self.client, json_body=body)
        if type(response) is WriteToOutputFileResponse400:
            raise ContainerApiError(
                "{} {}".format(response.message, response.errors.to_dict())
            )

        return response

    def read_from_file(self, file: InputFile):
        response = read_input_file_next.sync(file, client=self.client)

        if response is None:
            return None

        return response.data.to_dict()

    def read_from_file_batch(self, file: InputFile, batch_size: int = 100):
        response = read_input_file_next_batch.sync(
            file, client=self.client, size=batch_size
        )

        if response is None or not response.data:
            return None

        if type(response) is ReadInputFileNextBatchResponse400:
            raise ContainerApiError(
                "{} {}".format(response.message, response.errors.to_dict())
            )

        return [response_item.to_dict() for response_item in response.data]

    def yield_from_file_batch(self, file: InputFile, batch_size: int = 100):
        while True:
            products = self.read_from_file_batch(file, batch_size)

            if products is None:
                break

            yield products

    def log(self, level: str, message: str, context: typing.Optional[dict] = None):
        body = WriteLogInput()
        body.message = message

        if context is not None:
            body.context = WriteLogInputContext.from_dict(context)

        response = write_log.sync(level, client=self.client, json_body=body)
        if type(response) is WriteLogResponse400:
            raise ContainerApiError(
                "{} {}".format(response.message, response.errors.to_dict())
            )

        return response
