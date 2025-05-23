# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.ssl_live_lookup_response import SslLiveLookupResponse


class RawSslClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def ssl_live_lookup(
        self,
        *,
        api_key: str,
        domain_name: str,
        chain: typing.Optional[bool] = None,
        ssl_raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SslLiveLookupResponse]:
        """
        Retrieve live SSL certificate details for a domain

        Parameters
        ----------
        api_key : str

        domain_name : str

        chain : typing.Optional[bool]

        ssl_raw : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SslLiveLookupResponse]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1.0/ssl/live",
            base_url=self._client_wrapper.get_environment().apis,
            method="GET",
            params={
                "apiKey": api_key,
                "domainName": domain_name,
                "chain": chain,
                "sslRaw": ssl_raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SslLiveLookupResponse,
                    parse_obj_as(
                        type_=SslLiveLookupResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response.text)
        raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response_json)


class AsyncRawSslClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def ssl_live_lookup(
        self,
        *,
        api_key: str,
        domain_name: str,
        chain: typing.Optional[bool] = None,
        ssl_raw: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SslLiveLookupResponse]:
        """
        Retrieve live SSL certificate details for a domain

        Parameters
        ----------
        api_key : str

        domain_name : str

        chain : typing.Optional[bool]

        ssl_raw : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SslLiveLookupResponse]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1.0/ssl/live",
            base_url=self._client_wrapper.get_environment().apis,
            method="GET",
            params={
                "apiKey": api_key,
                "domainName": domain_name,
                "chain": chain,
                "sslRaw": ssl_raw,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SslLiveLookupResponse,
                    parse_obj_as(
                        type_=SslLiveLookupResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response.text)
        raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response_json)
