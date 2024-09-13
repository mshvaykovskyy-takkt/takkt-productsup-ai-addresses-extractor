from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx

from ... import errors
from ...client import Client
from ...models.items_count_input_file_response_200 import ItemsCountInputFileResponse200
from ...types import Response


def _get_kwargs(
    type: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/items/{type}/count".format(client.base_url, type=type)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[ItemsCountInputFileResponse200]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ItemsCountInputFileResponse200.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[ItemsCountInputFileResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    type: str,
    *,
    client: Client,
) -> Response[ItemsCountInputFileResponse200]:
    """Fetch row count for specified file

     Will return the row count of the file.

    Args:
        type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ItemsCountInputFileResponse200]
    """

    kwargs = _get_kwargs(
        type=type,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    type: str,
    *,
    client: Client,
) -> Optional[ItemsCountInputFileResponse200]:
    """Fetch row count for specified file

     Will return the row count of the file.

    Args:
        type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ItemsCountInputFileResponse200
    """

    return sync_detailed(
        type=type,
        client=client,
    ).parsed


async def asyncio_detailed(
    type: str,
    *,
    client: Client,
) -> Response[ItemsCountInputFileResponse200]:
    """Fetch row count for specified file

     Will return the row count of the file.

    Args:
        type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ItemsCountInputFileResponse200]
    """

    kwargs = _get_kwargs(
        type=type,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type: str,
    *,
    client: Client,
) -> Optional[ItemsCountInputFileResponse200]:
    """Fetch row count for specified file

     Will return the row count of the file.

    Args:
        type (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ItemsCountInputFileResponse200
    """

    return (
        await asyncio_detailed(
            type=type,
            client=client,
        )
    ).parsed
