# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .inet_num import InetNum
from .ip_contact import IpContact
from .organization import Organization
from .status import Status


class IpWhoisResponse(UniversalBaseModel):
    status: typing.Optional[Status] = None
    ip_address: typing.Optional[str] = None
    query_time: typing.Optional[str] = None
    whois_server: typing.Optional[str] = None
    inet_nums: typing.Optional[typing.List[InetNum]] = None
    organization: typing.Optional[Organization] = None
    technical_contacts: typing.Optional[typing.List[IpContact]] = None
    abuse_contacts: typing.Optional[typing.List[IpContact]] = None
    whois_raw_response: typing.Optional[str] = None
    timestamp: typing.Optional[str] = None
    error: typing.Optional[str] = None
    message: typing.Optional[str] = None
    path: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
