# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .errors.invalid_api_key import InvalidApiKey
from .types.credits_response import CreditsResponse
from .types.invalid_api_key_body import InvalidApiKeyBody


class RawCreditsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def credits_usage_api(
        self, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreditsResponse]:
        """
        You need credits to use Whois and DNS APIs. You can use this API to see your remaining credits for your API Key.

        Parameters
        ----------
        api_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreditsResponse]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1.0/whoisapi/usage",
            base_url=self._client_wrapper.get_environment().apis,
            method="GET",
            params={
                "apiKey": api_key,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreditsResponse,
                    parse_obj_as(
                        type_=CreditsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise InvalidApiKey(
                    typing.cast(
                        InvalidApiKeyBody,
                        parse_obj_as(
                            type_=InvalidApiKeyBody,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response.text)
        raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response_json)


class AsyncRawCreditsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def credits_usage_api(
        self, *, api_key: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreditsResponse]:
        """
        You need credits to use Whois and DNS APIs. You can use this API to see your remaining credits for your API Key.

        Parameters
        ----------
        api_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreditsResponse]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1.0/whoisapi/usage",
            base_url=self._client_wrapper.get_environment().apis,
            method="GET",
            params={
                "apiKey": api_key,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreditsResponse,
                    parse_obj_as(
                        type_=CreditsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise InvalidApiKey(
                    typing.cast(
                        InvalidApiKeyBody,
                        parse_obj_as(
                            type_=InvalidApiKeyBody,  # type: ignore
                            object_=_response.json(),
                        ),
                    )
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response.text)
        raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response_json)
