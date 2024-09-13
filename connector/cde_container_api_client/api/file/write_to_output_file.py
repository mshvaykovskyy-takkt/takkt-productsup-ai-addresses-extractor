from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.write_to_output_file_input import WriteToOutputFileInput
from ...models.write_to_output_file_response_201 import WriteToOutputFileResponse201
from ...models.write_to_output_file_response_400 import WriteToOutputFileResponse400
from ...types import Response


def _get_kwargs(
    type: str,
    *,
    client: Client,
    json_body: WriteToOutputFileInput,
) -> Dict[str, Any]:
    url = "{}/output/{type}".format(client.base_url, type=type)

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
) -> Optional[Union[WriteToOutputFileResponse201, WriteToOutputFileResponse400]]:
    if response.status_code == HTTPStatus.CREATED:
        response_201 = WriteToOutputFileResponse201.from_dict(response.json())

        return response_201
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = WriteToOutputFileResponse400.from_dict(response.json())

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[WriteToOutputFileResponse201, WriteToOutputFileResponse400]]:
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
    json_body: WriteToOutputFileInput,
) -> Response[Union[WriteToOutputFileResponse201, WriteToOutputFileResponse400]]:
    """Write to output file

    Args:
        type (str):
        json_body (WriteToOutputFileInput):  Example: {'meta': {'separator': '-'}, 'data': [{'id':
            1, 'taxon-0-id': 11, 'taxon-0-name': 'taxon0'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WriteToOutputFileResponse201, WriteToOutputFileResponse400]]
    """

    kwargs = _get_kwargs(
        type=type,
        client=client,
        json_body=json_body,
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
    json_body: WriteToOutputFileInput,
) -> Optional[Union[WriteToOutputFileResponse201, WriteToOutputFileResponse400]]:
    """Write to output file

    Args:
        type (str):
        json_body (WriteToOutputFileInput):  Example: {'meta': {'separator': '-'}, 'data': [{'id':
            1, 'taxon-0-id': 11, 'taxon-0-name': 'taxon0'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WriteToOutputFileResponse201, WriteToOutputFileResponse400]
    """

    return sync_detailed(
        type=type,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    type: str,
    *,
    client: Client,
    json_body: WriteToOutputFileInput,
) -> Response[Union[WriteToOutputFileResponse201, WriteToOutputFileResponse400]]:
    """Write to output file

    Args:
        type (str):
        json_body (WriteToOutputFileInput):  Example: {'meta': {'separator': '-'}, 'data': [{'id':
            1, 'taxon-0-id': 11, 'taxon-0-name': 'taxon0'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[WriteToOutputFileResponse201, WriteToOutputFileResponse400]]
    """

    kwargs = _get_kwargs(
        type=type,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    type: str,
    *,
    client: Client,
    json_body: WriteToOutputFileInput,
) -> Optional[Union[WriteToOutputFileResponse201, WriteToOutputFileResponse400]]:
    """Write to output file

    Args:
        type (str):
        json_body (WriteToOutputFileInput):  Example: {'meta': {'separator': '-'}, 'data': [{'id':
            1, 'taxon-0-id': 11, 'taxon-0-name': 'taxon0'}]}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[WriteToOutputFileResponse201, WriteToOutputFileResponse400]
    """

    return (
        await asyncio_detailed(
            type=type,
            client=client,
            json_body=json_body,
        )
    ).parsed
