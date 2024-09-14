import re
import json
from typing import Optional

from openai import AzureOpenAI


class ApiResponseUsage:
    def __init__(
        self, prompt_tokens: int = 0, completion_tokens: int = 0, total_tokens: int = 0
    ):
        """
        Construct an ApiResponseUsage instance.

        :param prompt_tokens: The number of prompt tokens used.
        :param completion_tokens: The number of completion tokens used.
        :param total_tokens: The total number of tokens used.
        """
        self.prompt_tokens: int = prompt_tokens
        self.completion_tokens: int = completion_tokens
        self.total_tokens: int = total_tokens


class ApiResponse:
    def __init__(
        self,
        success: bool,
        data: Optional[dict] = None,
        error: Optional[str] = None,
        usage: ApiResponseUsage = ApiResponseUsage(),
    ):
        """
        Construct an ApiResponse instance.

        :param success: A boolean indicating if the API call was successful.
        :param data: The data returned from the API call. This is None if the API call was not successful.
        :param error: The error returned from the API call. This is None if the API call was successful.
        """
        self.success: bool = success
        self.data: Optional[dict] = data
        self.error: Optional[str] = error
        self.usage: ApiResponseUsage = usage


class AzureOpenAIApi:
    def __init__(self, model: str, endpoint: str, api_key: str, api_version: str):
        """
        Construct an AzureOpenAIApi instance.

        :param model: The name of the OpenAI model to use.
        :param endpoint: The URL of the Azure OpenAI endpoint.
        :param api_key: The API key to use for authentication.
        :param api_version: The version of the Azure OpenAI API to use.
        """

        self.model: str = model
        self.endpoint: str = endpoint
        self.api_key: str = api_key
        self.api_version: str = api_version

    def __get_response_format(self) -> Optional[dict]:
        """
        Check if the model name matches any of the supported models that return json data.

        :return: A dictionary with a single key-value pair, where the key is "type" and the value is "json_object" if the model returns json data, otherwise None.
        """
        model_name: str = self.model.lower()

        json_supported_models: list = [
            r"gpt-4-\d{4}-preview",
            r"gpt-4o",
            r"gpt-4o-mini",
            r"gpt-3.5-turbo-\d{4}",
        ]

        for pattern in json_supported_models:
            if re.match(pattern, model_name):
                return {"type": "json_object"}

        return None

    def make_api_call(self, system_prompt: str, user_prompt: str) -> ApiResponse:
        """
        Make an API call to Azure OpenAI using the specified system and user prompts.

        :param system_prompt: The system prompt to send to the API.
        :param user_prompt: The user prompt to send to the API.
        :return: An ApiResponse object containing the response from the API, or an error message if the call was not successful.
        """
        client = AzureOpenAI(
            azure_endpoint=self.endpoint,
            api_key=self.api_key,
            api_version=self.api_version,
        )

        response = client.chat.completions.create(
            model=self.model,
            response_format=self.__get_response_format(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
        )

        if not response:
            return ApiResponse(success=False, error="Empty response")

        try:
            usage: ApiResponseUsage = ApiResponseUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            )
            return ApiResponse(
                success=True,
                data=json.loads(response.choices[0].message.content),
                usage=usage,
            )
        except Exception as e:
            return ApiResponse(success=False, error=str(e))
