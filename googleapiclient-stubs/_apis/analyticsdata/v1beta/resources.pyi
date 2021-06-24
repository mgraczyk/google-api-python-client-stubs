import typing

import httplib2  # type: ignore
import typing_extensions

import googleapiclient.discovery
import googleapiclient.http  # type: ignore

from .schemas import *

@typing.type_check_only
class AnalyticsDataResource(googleapiclient.discovery.Resource):
    @typing.type_check_only
    class PropertiesResource(googleapiclient.discovery.Resource):
        def batchRunPivotReports(
            self,
            *,
            property: str,
            body: BatchRunPivotReportsRequest = ...,
            **kwargs: typing.Any
        ) -> BatchRunPivotReportsResponseHttpRequest: ...
        def batchRunReports(
            self,
            *,
            property: str,
            body: BatchRunReportsRequest = ...,
            **kwargs: typing.Any
        ) -> BatchRunReportsResponseHttpRequest: ...
        def getMetadata(
            self, *, name: str, **kwargs: typing.Any
        ) -> MetadataHttpRequest: ...
        def runPivotReport(
            self,
            *,
            property: str,
            body: RunPivotReportRequest = ...,
            **kwargs: typing.Any
        ) -> RunPivotReportResponseHttpRequest: ...
        def runRealtimeReport(
            self,
            *,
            property: str,
            body: RunRealtimeReportRequest = ...,
            **kwargs: typing.Any
        ) -> RunRealtimeReportResponseHttpRequest: ...
        def runReport(
            self, *, property: str, body: RunReportRequest = ..., **kwargs: typing.Any
        ) -> RunReportResponseHttpRequest: ...
    def properties(self) -> PropertiesResource: ...

@typing.type_check_only
class BatchRunPivotReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BatchRunPivotReportsResponse: ...

@typing.type_check_only
class BatchRunReportsResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> BatchRunReportsResponse: ...

@typing.type_check_only
class MetadataHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> Metadata: ...

@typing.type_check_only
class RunPivotReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RunPivotReportResponse: ...

@typing.type_check_only
class RunRealtimeReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RunRealtimeReportResponse: ...

@typing.type_check_only
class RunReportResponseHttpRequest(googleapiclient.http.HttpRequest):
    def execute(
        self,
        http: typing.Optional[
            typing.Union[httplib2.Http, googleapiclient.http.HttpMock]
        ] = ...,
        num_retries: int = ...,
    ) -> RunReportResponse: ...