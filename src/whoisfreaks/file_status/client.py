# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFileStatusClient, RawFileStatusClient
from .types.file_status_api_response import FileStatusApiResponse


class FileStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFileStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFileStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFileStatusClient
        """
        return self._raw_client

    def file_status_api(self, *, request_options: typing.Optional[RequestOptions] = None) -> FileStatusApiResponse:
        """
        The Whois Files Status API provides comprehensive details about the availability and update status of various Whois datasets. It includes several key datasets, such as:
        - Newly registered domains: Includes cleaned gTLDs, cleaned ccTLDs, gTLDs, DNS records, and ccTLDs.
        - Expired domains: Covers both cleaned and regular expired domains.
        - Dropped domains: Details on domains that have been removed or dropped.

        In addition to these datasets, the API offers information on the update frequency of Whois and DNS data. Updates are available in three time intervals:
        - Daily: Regularly updated Whois and DNS data.
        - Weekly: Whois and DNS data refreshed on a weekly basis.
        - Monthly: Monthly updates are provided for Whois data, though DNS updates may not always be available.
        This structure enables users to track the currency and availability of various domain datasets, ensuring access to the latest WHOIS and DNS information.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileStatusApiResponse

        Examples
        --------
        from whoisfreaks import WhoisfreaksApi
        from whoisfreaks.environment import WhoisfreaksApiEnvironment
        client = WhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
        client.file_status.file_status_api()
        """
        _response = self._raw_client.file_status_api(request_options=request_options)
        return _response.data


class AsyncFileStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFileStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFileStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFileStatusClient
        """
        return self._raw_client

    async def file_status_api(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FileStatusApiResponse:
        """
        The Whois Files Status API provides comprehensive details about the availability and update status of various Whois datasets. It includes several key datasets, such as:
        - Newly registered domains: Includes cleaned gTLDs, cleaned ccTLDs, gTLDs, DNS records, and ccTLDs.
        - Expired domains: Covers both cleaned and regular expired domains.
        - Dropped domains: Details on domains that have been removed or dropped.

        In addition to these datasets, the API offers information on the update frequency of Whois and DNS data. Updates are available in three time intervals:
        - Daily: Regularly updated Whois and DNS data.
        - Weekly: Whois and DNS data refreshed on a weekly basis.
        - Monthly: Monthly updates are provided for Whois data, though DNS updates may not always be available.
        This structure enables users to track the currency and availability of various domain datasets, ensuring access to the latest WHOIS and DNS information.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileStatusApiResponse

        Examples
        --------
        from whoisfreaks import AsyncWhoisfreaksApi
        from whoisfreaks.environment import WhoisfreaksApiEnvironment
        import asyncio
        client = AsyncWhoisfreaksApi(environment=WhoisfreaksApiEnvironment.PRODUCTION, )
        async def main() -> None:
            await client.file_status.file_status_api()
        asyncio.run(main())
        """
        _response = await self._raw_client.file_status_api(request_options=request_options)
        return _response.data
