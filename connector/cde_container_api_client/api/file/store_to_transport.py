from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.store_to_transport_input import StoreToTransportInput
from ...models.store_to_transport_response_202 import StoreToTransportResponse202
from ...models.store_to_transport_response_400 import StoreToTransportResponse400
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: StoreToTransportInput,
) -> Dict[str, Any]:
    url = "{}/store/to-transport".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "json": json_json_body,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[StoreToTransportResponse202, StoreToTransportResponse400]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = StoreToTransportResponse202.from_dict(response.json())

        return response_202
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = StoreToTransportResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[StoreToTransportResponse202, StoreToTransportResponse400]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: StoreToTransportInput,
) -> Response[Union[StoreToTransportResponse202, StoreToTransportResponse400]]:
    """Store folder content to transport

    Args:
        json_body (StoreToTransportInput):  Example: {'source_file': '/example-
            subdirectory/example_file.txt', 'remote_file': '/remote-folder/remote_file.txt'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StoreToTransportResponse202, StoreToTransportResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: StoreToTransportInput,
) -> Optional[Union[StoreToTransportResponse202, StoreToTransportResponse400]]:
    """Store folder content to transport

    Args:
        json_body (StoreToTransportInput):  Example: {'source_file': '/example-
            subdirectory/example_file.txt', 'remote_file': '/remote-folder/remote_file.txt'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StoreToTransportResponse202, StoreToTransportResponse400]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: StoreToTransportInput,
) -> Response[Union[StoreToTransportResponse202, StoreToTransportResponse400]]:
    """Store folder content to transport

    Args:
        json_body (StoreToTransportInput):  Example: {'source_file': '/example-
            subdirectory/example_file.txt', 'remote_file': '/remote-folder/remote_file.txt'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[StoreToTransportResponse202, StoreToTransportResponse400]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: StoreToTransportInput,
) -> Optional[Union[StoreToTransportResponse202, StoreToTransportResponse400]]:
    """Store folder content to transport

    Args:
        json_body (StoreToTransportInput):  Example: {'source_file': '/example-
            subdirectory/example_file.txt', 'remote_file': '/remote-folder/remote_file.txt'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[StoreToTransportResponse202, StoreToTransportResponse400]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
