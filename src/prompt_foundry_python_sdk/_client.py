# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, PromptFoundryError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import tools, prompts, completion, evaluations, evaluation_assertions
    from .resources.tools import ToolsResource, AsyncToolsResource
    from .resources.prompts import PromptsResource, AsyncPromptsResource
    from .resources.completion import CompletionResource, AsyncCompletionResource
    from .resources.evaluations import EvaluationsResource, AsyncEvaluationsResource
    from .resources.evaluation_assertions import EvaluationAssertionsResource, AsyncEvaluationAssertionsResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "PromptFoundry",
    "AsyncPromptFoundry",
    "Client",
    "AsyncClient",
]


class PromptFoundry(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous PromptFoundry client instance.

        This automatically infers the `api_key` argument from the `PROMPT_FOUNDRY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PROMPT_FOUNDRY_API_KEY")
        if api_key is None:
            raise PromptFoundryError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PROMPT_FOUNDRY_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PROMPT_FOUNDRY_BASE_URL")
        if base_url is None:
            base_url = f"https://api.promptfoundry.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def completion(self) -> CompletionResource:
        from .resources.completion import CompletionResource

        return CompletionResource(self)

    @cached_property
    def prompts(self) -> PromptsResource:
        from .resources.prompts import PromptsResource

        return PromptsResource(self)

    @cached_property
    def tools(self) -> ToolsResource:
        from .resources.tools import ToolsResource

        return ToolsResource(self)

    @cached_property
    def evaluation_assertions(self) -> EvaluationAssertionsResource:
        from .resources.evaluation_assertions import EvaluationAssertionsResource

        return EvaluationAssertionsResource(self)

    @cached_property
    def evaluations(self) -> EvaluationsResource:
        from .resources.evaluations import EvaluationsResource

        return EvaluationsResource(self)

    @cached_property
    def with_raw_response(self) -> PromptFoundryWithRawResponse:
        return PromptFoundryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PromptFoundryWithStreamedResponse:
        return PromptFoundryWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-KEY": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncPromptFoundry(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncPromptFoundry client instance.

        This automatically infers the `api_key` argument from the `PROMPT_FOUNDRY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("PROMPT_FOUNDRY_API_KEY")
        if api_key is None:
            raise PromptFoundryError(
                "The api_key client option must be set either by passing api_key to the client or by setting the PROMPT_FOUNDRY_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("PROMPT_FOUNDRY_BASE_URL")
        if base_url is None:
            base_url = f"https://api.promptfoundry.ai"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def completion(self) -> AsyncCompletionResource:
        from .resources.completion import AsyncCompletionResource

        return AsyncCompletionResource(self)

    @cached_property
    def prompts(self) -> AsyncPromptsResource:
        from .resources.prompts import AsyncPromptsResource

        return AsyncPromptsResource(self)

    @cached_property
    def tools(self) -> AsyncToolsResource:
        from .resources.tools import AsyncToolsResource

        return AsyncToolsResource(self)

    @cached_property
    def evaluation_assertions(self) -> AsyncEvaluationAssertionsResource:
        from .resources.evaluation_assertions import AsyncEvaluationAssertionsResource

        return AsyncEvaluationAssertionsResource(self)

    @cached_property
    def evaluations(self) -> AsyncEvaluationsResource:
        from .resources.evaluations import AsyncEvaluationsResource

        return AsyncEvaluationsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncPromptFoundryWithRawResponse:
        return AsyncPromptFoundryWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPromptFoundryWithStreamedResponse:
        return AsyncPromptFoundryWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"X-API-KEY": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class PromptFoundryWithRawResponse:
    _client: PromptFoundry

    def __init__(self, client: PromptFoundry) -> None:
        self._client = client

    @cached_property
    def completion(self) -> completion.CompletionResourceWithRawResponse:
        from .resources.completion import CompletionResourceWithRawResponse

        return CompletionResourceWithRawResponse(self._client.completion)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithRawResponse:
        from .resources.prompts import PromptsResourceWithRawResponse

        return PromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithRawResponse:
        from .resources.tools import ToolsResourceWithRawResponse

        return ToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def evaluation_assertions(self) -> evaluation_assertions.EvaluationAssertionsResourceWithRawResponse:
        from .resources.evaluation_assertions import EvaluationAssertionsResourceWithRawResponse

        return EvaluationAssertionsResourceWithRawResponse(self._client.evaluation_assertions)

    @cached_property
    def evaluations(self) -> evaluations.EvaluationsResourceWithRawResponse:
        from .resources.evaluations import EvaluationsResourceWithRawResponse

        return EvaluationsResourceWithRawResponse(self._client.evaluations)


class AsyncPromptFoundryWithRawResponse:
    _client: AsyncPromptFoundry

    def __init__(self, client: AsyncPromptFoundry) -> None:
        self._client = client

    @cached_property
    def completion(self) -> completion.AsyncCompletionResourceWithRawResponse:
        from .resources.completion import AsyncCompletionResourceWithRawResponse

        return AsyncCompletionResourceWithRawResponse(self._client.completion)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithRawResponse:
        from .resources.prompts import AsyncPromptsResourceWithRawResponse

        return AsyncPromptsResourceWithRawResponse(self._client.prompts)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithRawResponse:
        from .resources.tools import AsyncToolsResourceWithRawResponse

        return AsyncToolsResourceWithRawResponse(self._client.tools)

    @cached_property
    def evaluation_assertions(self) -> evaluation_assertions.AsyncEvaluationAssertionsResourceWithRawResponse:
        from .resources.evaluation_assertions import AsyncEvaluationAssertionsResourceWithRawResponse

        return AsyncEvaluationAssertionsResourceWithRawResponse(self._client.evaluation_assertions)

    @cached_property
    def evaluations(self) -> evaluations.AsyncEvaluationsResourceWithRawResponse:
        from .resources.evaluations import AsyncEvaluationsResourceWithRawResponse

        return AsyncEvaluationsResourceWithRawResponse(self._client.evaluations)


class PromptFoundryWithStreamedResponse:
    _client: PromptFoundry

    def __init__(self, client: PromptFoundry) -> None:
        self._client = client

    @cached_property
    def completion(self) -> completion.CompletionResourceWithStreamingResponse:
        from .resources.completion import CompletionResourceWithStreamingResponse

        return CompletionResourceWithStreamingResponse(self._client.completion)

    @cached_property
    def prompts(self) -> prompts.PromptsResourceWithStreamingResponse:
        from .resources.prompts import PromptsResourceWithStreamingResponse

        return PromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def tools(self) -> tools.ToolsResourceWithStreamingResponse:
        from .resources.tools import ToolsResourceWithStreamingResponse

        return ToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def evaluation_assertions(self) -> evaluation_assertions.EvaluationAssertionsResourceWithStreamingResponse:
        from .resources.evaluation_assertions import EvaluationAssertionsResourceWithStreamingResponse

        return EvaluationAssertionsResourceWithStreamingResponse(self._client.evaluation_assertions)

    @cached_property
    def evaluations(self) -> evaluations.EvaluationsResourceWithStreamingResponse:
        from .resources.evaluations import EvaluationsResourceWithStreamingResponse

        return EvaluationsResourceWithStreamingResponse(self._client.evaluations)


class AsyncPromptFoundryWithStreamedResponse:
    _client: AsyncPromptFoundry

    def __init__(self, client: AsyncPromptFoundry) -> None:
        self._client = client

    @cached_property
    def completion(self) -> completion.AsyncCompletionResourceWithStreamingResponse:
        from .resources.completion import AsyncCompletionResourceWithStreamingResponse

        return AsyncCompletionResourceWithStreamingResponse(self._client.completion)

    @cached_property
    def prompts(self) -> prompts.AsyncPromptsResourceWithStreamingResponse:
        from .resources.prompts import AsyncPromptsResourceWithStreamingResponse

        return AsyncPromptsResourceWithStreamingResponse(self._client.prompts)

    @cached_property
    def tools(self) -> tools.AsyncToolsResourceWithStreamingResponse:
        from .resources.tools import AsyncToolsResourceWithStreamingResponse

        return AsyncToolsResourceWithStreamingResponse(self._client.tools)

    @cached_property
    def evaluation_assertions(self) -> evaluation_assertions.AsyncEvaluationAssertionsResourceWithStreamingResponse:
        from .resources.evaluation_assertions import AsyncEvaluationAssertionsResourceWithStreamingResponse

        return AsyncEvaluationAssertionsResourceWithStreamingResponse(self._client.evaluation_assertions)

    @cached_property
    def evaluations(self) -> evaluations.AsyncEvaluationsResourceWithStreamingResponse:
        from .resources.evaluations import AsyncEvaluationsResourceWithStreamingResponse

        return AsyncEvaluationsResourceWithStreamingResponse(self._client.evaluations)


Client = PromptFoundry

AsyncClient = AsyncPromptFoundry
