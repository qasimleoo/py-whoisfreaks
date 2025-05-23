# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.bulk_domain_availability_response import BulkDomainAvailabilityResponse
from .types.domain_availability_response import DomainAvailabilityResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawDomainAvailabilityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def domain_availability_lookup(
        self,
        *,
        api_key: str,
        domain: str,
        sug: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DomainAvailabilityResponse]:
        """
        Check availability of a Domain Name

        Parameters
        ----------
        api_key : str

        domain : str

        sug : typing.Optional[bool]

        count : typing.Optional[int]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DomainAvailabilityResponse]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1.0/domain/availability",
            base_url=self._client_wrapper.get_environment().apis,
            method="GET",
            params={
                "apiKey": api_key,
                "domain": domain,
                "sug": sug,
                "count": count,
                "format": format,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DomainAvailabilityResponse,
                    parse_obj_as(
                        type_=DomainAvailabilityResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response.text)
        raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response_json)

    def bulk_domain_availability_lookup(
        self,
        *,
        api_key: str,
        domain_names: typing.Sequence[str],
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkDomainAvailabilityResponse]:
        """
        Check availability of multiple Domain Names

        Parameters
        ----------
        api_key : str

        domain_names : typing.Sequence[str]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkDomainAvailabilityResponse]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1.0/domain/availability",
            base_url=self._client_wrapper.get_environment().apis,
            method="POST",
            params={
                "apiKey": api_key,
                "format": format,
            },
            json={
                "domainNames": domain_names,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkDomainAvailabilityResponse,
                    parse_obj_as(
                        type_=BulkDomainAvailabilityResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response.text)
        raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response_json)

    def bulk_domain_availability_lookup_with_custom_tl_ds(
        self,
        *,
        api_key: str,
        domain: str,
        tld: typing.Sequence[str],
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BulkDomainAvailabilityResponse]:
        """
        Check availability of multiple Domain Names with custom TLDs

        Parameters
        ----------
        api_key : str

        domain : str

        tld : typing.Sequence[str]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BulkDomainAvailabilityResponse]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1.0/domain/availability",
            base_url=self._client_wrapper.get_environment().apis,
            method="POST",
            params={
                "apiKey": api_key,
                "domain": domain,
                "format": format,
            },
            json={
                "tld": tld,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkDomainAvailabilityResponse,
                    parse_obj_as(
                        type_=BulkDomainAvailabilityResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response.text)
        raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response_json)


class AsyncRawDomainAvailabilityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def domain_availability_lookup(
        self,
        *,
        api_key: str,
        domain: str,
        sug: typing.Optional[bool] = None,
        count: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DomainAvailabilityResponse]:
        """
        Check availability of a Domain Name

        Parameters
        ----------
        api_key : str

        domain : str

        sug : typing.Optional[bool]

        count : typing.Optional[int]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DomainAvailabilityResponse]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1.0/domain/availability",
            base_url=self._client_wrapper.get_environment().apis,
            method="GET",
            params={
                "apiKey": api_key,
                "domain": domain,
                "sug": sug,
                "count": count,
                "format": format,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DomainAvailabilityResponse,
                    parse_obj_as(
                        type_=DomainAvailabilityResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response.text)
        raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response_json)

    async def bulk_domain_availability_lookup(
        self,
        *,
        api_key: str,
        domain_names: typing.Sequence[str],
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkDomainAvailabilityResponse]:
        """
        Check availability of multiple Domain Names

        Parameters
        ----------
        api_key : str

        domain_names : typing.Sequence[str]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkDomainAvailabilityResponse]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1.0/domain/availability",
            base_url=self._client_wrapper.get_environment().apis,
            method="POST",
            params={
                "apiKey": api_key,
                "format": format,
            },
            json={
                "domainNames": domain_names,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkDomainAvailabilityResponse,
                    parse_obj_as(
                        type_=BulkDomainAvailabilityResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response.text)
        raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response_json)

    async def bulk_domain_availability_lookup_with_custom_tl_ds(
        self,
        *,
        api_key: str,
        domain: str,
        tld: typing.Sequence[str],
        format: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BulkDomainAvailabilityResponse]:
        """
        Check availability of multiple Domain Names with custom TLDs

        Parameters
        ----------
        api_key : str

        domain : str

        tld : typing.Sequence[str]

        format : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BulkDomainAvailabilityResponse]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1.0/domain/availability",
            base_url=self._client_wrapper.get_environment().apis,
            method="POST",
            params={
                "apiKey": api_key,
                "domain": domain,
                "format": format,
            },
            json={
                "tld": tld,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BulkDomainAvailabilityResponse,
                    parse_obj_as(
                        type_=BulkDomainAvailabilityResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response.text)
        raise ApiError(headers=dict(_response.headers), status_code=_response.status_code, body=_response_json)
