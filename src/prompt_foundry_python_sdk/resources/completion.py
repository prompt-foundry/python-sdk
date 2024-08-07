# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ..types import completion_create_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.completion_create_response import CompletionCreateResponse

__all__ = ["CompletionResource", "AsyncCompletionResource"]


class CompletionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CompletionResourceWithRawResponse:
        return CompletionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CompletionResourceWithStreamingResponse:
        return CompletionResourceWithStreamingResponse(self)

    def create(
        self,
        id: str,
        *,
        append_messages: Iterable[completion_create_params.AppendMessage] | NotGiven = NOT_GIVEN,
        override_messages: Iterable[completion_create_params.OverrideMessage] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        variables: Dict[str, Optional[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        Initiates a completion request to the configured LLM provider using specified
        parameters and provided variables. This endpoint abstracts the integration with
        different model providers, enabling seamless switching between models while
        maintaining a consistent data model for your application.

        Args:
          append_messages: Appended the the end of the configured prompt messages before running the
              prompt.

          override_messages: Replaces the configured prompt messages when running the prompt.

          user: A unique identifier representing your end-user, which can help monitor and
              detect abuse.

          variables: The template variables added to the prompt when executing the prompt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/sdk/v1/prompts/{id}/completion",
            body=maybe_transform(
                {
                    "append_messages": append_messages,
                    "override_messages": override_messages,
                    "user": user,
                    "variables": variables,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )


class AsyncCompletionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCompletionResourceWithRawResponse:
        return AsyncCompletionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCompletionResourceWithStreamingResponse:
        return AsyncCompletionResourceWithStreamingResponse(self)

    async def create(
        self,
        id: str,
        *,
        append_messages: Iterable[completion_create_params.AppendMessage] | NotGiven = NOT_GIVEN,
        override_messages: Iterable[completion_create_params.OverrideMessage] | NotGiven = NOT_GIVEN,
        user: str | NotGiven = NOT_GIVEN,
        variables: Dict[str, Optional[str]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CompletionCreateResponse:
        """
        Initiates a completion request to the configured LLM provider using specified
        parameters and provided variables. This endpoint abstracts the integration with
        different model providers, enabling seamless switching between models while
        maintaining a consistent data model for your application.

        Args:
          append_messages: Appended the the end of the configured prompt messages before running the
              prompt.

          override_messages: Replaces the configured prompt messages when running the prompt.

          user: A unique identifier representing your end-user, which can help monitor and
              detect abuse.

          variables: The template variables added to the prompt when executing the prompt.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/sdk/v1/prompts/{id}/completion",
            body=await async_maybe_transform(
                {
                    "append_messages": append_messages,
                    "override_messages": override_messages,
                    "user": user,
                    "variables": variables,
                },
                completion_create_params.CompletionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CompletionCreateResponse,
        )


class CompletionResourceWithRawResponse:
    def __init__(self, completion: CompletionResource) -> None:
        self._completion = completion

        self.create = to_raw_response_wrapper(
            completion.create,
        )


class AsyncCompletionResourceWithRawResponse:
    def __init__(self, completion: AsyncCompletionResource) -> None:
        self._completion = completion

        self.create = async_to_raw_response_wrapper(
            completion.create,
        )


class CompletionResourceWithStreamingResponse:
    def __init__(self, completion: CompletionResource) -> None:
        self._completion = completion

        self.create = to_streamed_response_wrapper(
            completion.create,
        )


class AsyncCompletionResourceWithStreamingResponse:
    def __init__(self, completion: AsyncCompletionResource) -> None:
        self._completion = completion

        self.create = async_to_streamed_response_wrapper(
            completion.create,
        )
