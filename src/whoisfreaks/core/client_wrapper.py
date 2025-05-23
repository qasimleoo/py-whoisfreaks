# This file was auto-generated by Fern from our API Definition.

import typing

import httpx
from ..environment import WhoisfreaksApiEnvironment
from .http_client import AsyncHttpClient, HttpClient


class BaseClientWrapper:
    def __init__(self, *, environment: WhoisfreaksApiEnvironment, timeout: typing.Optional[float] = None):
        self._environment = environment
        self._timeout = timeout

    def get_headers(self) -> typing.Dict[str, str]:
        headers: typing.Dict[str, str] = {
            "X-Fern-Language": "Python",
            "X-Fern-SDK-Name": "py-whoisfreaks",
            "X-Fern-SDK-Version": "0.0.36",
        }
        return headers

    def get_environment(self) -> WhoisfreaksApiEnvironment:
        return self._environment

    def get_timeout(self) -> typing.Optional[float]:
        return self._timeout


class SyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        environment: WhoisfreaksApiEnvironment,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.Client,
    ):
        super().__init__(environment=environment, timeout=timeout)
        self.httpx_client = HttpClient(
            httpx_client=httpx_client, base_headers=self.get_headers, base_timeout=self.get_timeout
        )


class AsyncClientWrapper(BaseClientWrapper):
    def __init__(
        self,
        *,
        environment: WhoisfreaksApiEnvironment,
        timeout: typing.Optional[float] = None,
        httpx_client: httpx.AsyncClient,
    ):
        super().__init__(environment=environment, timeout=timeout)
        self.httpx_client = AsyncHttpClient(
            httpx_client=httpx_client, base_headers=self.get_headers, base_timeout=self.get_timeout
        )
