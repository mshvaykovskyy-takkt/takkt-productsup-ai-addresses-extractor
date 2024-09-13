from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.read_input_file_next_batch_response_200 import (
    ReadInputFileNextBatchResponse200,
)
from ...models.read_input_file_next_batch_response_400 import (
    ReadInputFileNextBatchResponse400,
)
from ...models.read_input_file_next_batch_response_404 import (
    ReadInputFileNextBatchResponse404,
)
from ...models.read_input_file_next_batch_response_500 import (
    ReadInputFileNextBatchResponse500,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    type: str,
    *,
    client: Client,
    size: Union[Unset, None, int] = UNSET,
    show_hidden: Union[Unset, None, bool] = UNSET,
    classification_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/input/{type}/next_batch".format(client.base_url, type=type)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["size"] = size

    params["show-hidden"] = show_hidden

    params["classification-id"] = classification_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[
    Union[
        ReadInputFileNextBatchResponse200,
        ReadInputFileNextBatchResponse400,
        ReadInputFileNextBatchResponse404,
        ReadInputFileNextBatchResponse500,
    ]
]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ReadInputFileNextBatchResponse200.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ReadInputFileNextBatchResponse400.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ReadInputFileNextBatchResponse404.from_dict(response.json())

        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = ReadInputFileNextBatchResponse500.from_dict(response.json())

        return response_500
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[
    Union[
        ReadInputFileNextBatchResponse200,
        ReadInputFileNextBatchResponse400,
        ReadInputFileNextBatchResponse404,
        ReadInputFileNextBatchResponse500,
    ]
]:
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
    size: Union[Unset, None, int] = UNSET,
    show_hidden: Union[Unset, None, bool] = UNSET,
    classification_id: Union[Unset, None, int] = UNSET,
) -> Response[
    Union[
        ReadInputFileNextBatchResponse200,
        ReadInputFileNextBatchResponse400,
        ReadInputFileNextBatchResponse404,
        ReadInputFileNextBatchResponse500,
    ]
]:
    """Fetch the next batch from the specified file

     Will return the next batch of items from the file, if no more: empty response.

    Args:
        type (str):
        size (Union[Unset, None, int]):
        show_hidden (Union[Unset, None, bool]):
        classification_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ReadInputFileNextBatchResponse200, ReadInputFileNextBatchResponse400, ReadInputFileNextBatchResponse404, ReadInputFileNextBatchResponse500]]
    """

    kwargs = _get_kwargs(
        type=type,
        client=client,
        size=size,
        show_hidden=show_hidden,
        classification_id=classification_id,
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
    size: Union[Unset, None, int] = UNSET,
    show_hidden: Union[Unset, None, bool] = UNSET,
    classification_id: Union[Unset, None, int] = UNSET,
) -> Optional[
    Union[
        ReadInputFileNextBatchResponse200,
        ReadInputFileNextBatchResponse400,
        ReadInputFileNextBatchResponse404,
        ReadInputFileNextBatchResponse500,
    ]
]:
    """Fetch the next batch from the specified file

     Will return the next batch of items from the file, if no more: empty response.

    Args:
        type (str):
        size (Union[Unset, None, int]):
        show_hidden (Union[Unset, None, bool]):
        classification_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReadInputFileNextBatchResponse200, ReadInputFileNextBatchResponse400, ReadInputFileNextBatchResponse404, ReadInputFileNextBatchResponse500]
    """

    return sync_detailed(
        type=type,
        client=client,
        size=size,
        show_hidden=show_hidden,
        classification_id=classification_id,
    ).parsed


async def asyncio_detailed(
    type: str,
    *,
    client: Client,
    size: Union[Unset, None, int] = UNSET,
    show_hidden: Union[Unset, None, bool] = UNSET,
    classification_id: Union[Unset, None, int] = UNSET,
) -> Response[
    Union[
        ReadInputFileNextBatchResponse200,
        ReadInputFileNextBatchResponse400,
        ReadInputFileNextBatchResponse404,
        ReadInputFileNextBatchResponse500,
    ]
]:
    """Fetch the next batch from the specified file

     Will return the next batch of items from the file, if no more: empty response.

    Args:
        type (str):
        size (Union[Unset, None, int]):
        show_hidden (Union[Unset, None, bool]):
        classification_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ReadInputFileNextBatchResponse200, ReadInputFileNextBatchResponse400, ReadInputFileNextBatchResponse404, ReadInputFileNextBatchResponse500]]
    """

    kwargs = _get_kwargs(
        type=type,
        client=client,
        size=size,
        show_hidden=show_hidden,
        classification_id=classification_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type: str,
    *,
    client: Client,
    size: Union[Unset, None, int] = UNSET,
    show_hidden: Union[Unset, None, bool] = UNSET,
    classification_id: Union[Unset, None, int] = UNSET,
) -> Optional[
    Union[
        ReadInputFileNextBatchResponse200,
        ReadInputFileNextBatchResponse400,
        ReadInputFileNextBatchResponse404,
        ReadInputFileNextBatchResponse500,
    ]
]:
    """Fetch the next batch from the specified file

     Will return the next batch of items from the file, if no more: empty response.

    Args:
        type (str):
        size (Union[Unset, None, int]):
        show_hidden (Union[Unset, None, bool]):
        classification_id (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ReadInputFileNextBatchResponse200, ReadInputFileNextBatchResponse400, ReadInputFileNextBatchResponse404, ReadInputFileNextBatchResponse500]
    """

    return (
        await asyncio_detailed(
            type=type,
            client=client,
            size=size,
            show_hidden=show_hidden,
            classification_id=classification_id,
        )
    ).parsed
