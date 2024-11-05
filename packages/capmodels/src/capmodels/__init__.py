import datetime as dt
import typing as t

from pydantic_xml import BaseXmlModel, element

NSMAP = {"": "urn:oasis:names:tc:emergency:cap:1.2"}


class EventCode(BaseXmlModel, tag="eventCode", nsmap=NSMAP):
    valueName: str = element()
    value: str = element()


class Parameter(BaseXmlModel, tag="parameter", nsmap=NSMAP):
    valueName: str = element()
    value: str = element()


class Geocode(BaseXmlModel, tag="geocode", nsmap=NSMAP):
    valueName: str = element()
    value: str = element()


class Area(BaseXmlModel, tag="area", nsmap=NSMAP):
    areaDesc: str = element()
    polygons: list[str] = element(tag="polygon")
    geocode: Geocode = element(tag="geocode")


class Info(BaseXmlModel, tag="info", nsmap=NSMAP):
    language: str = element()
    category: str = element()
    event: str = element()
    responseType: str = element()
    urgency: str = element()
    severity: str = element()
    certainty: str = element()
    eventCode: EventCode = element()
    effective: dt.datetime = element()
    onset: dt.datetime = element()
    expires: dt.datetime = element()
    senderName: str = element()
    headline: str = element()
    description: t.Annotated[str | None, element()] = None
    instruction: t.Annotated[str | None, element()] = None
    web: str = element()
    contact: str = element()
    parameter: list[Parameter] = element(tag="parameter")
    area: Area = element()


class Alert(BaseXmlModel, tag="alert", nsmap=NSMAP):
    identifier: str = element()
    sender: str = element()
    sent: dt.datetime = element()
    status: str = element()
    msgType: str = element()
    scope: str = element()
    references: t.Annotated[str | None, element()] = None
    infos: list[Info] = element(tag="info")
