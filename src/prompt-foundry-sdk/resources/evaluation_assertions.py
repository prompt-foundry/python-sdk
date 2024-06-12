# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._compat import cached_property

from ..types.evaluation_assertion import EvaluationAssertion

from .._utils import maybe_transform, async_maybe_transform

from ..types.evaluation_assertion_list_response import EvaluationAssertionListResponse

from ..types.evaluation_assertion_delete_response import EvaluationAssertionDeleteResponse

from .._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

from ..types import evaluation_assertion_create_params, evaluation_assertion_update_params

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from .._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from .._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from .._resource import SyncAPIResource, AsyncAPIResource
from .._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ..types import shared_params
from ..types import evaluation_assertion_create_params
from ..types import evaluation_assertion_update_params
from ..types import evaluation_assertion_list_params

__all__ = ["EvaluationAssertionsResource", "AsyncEvaluationAssertionsResource"]


class EvaluationAssertionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationAssertionsResourceWithRawResponse:
        return EvaluationAssertionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationAssertionsResourceWithStreamingResponse:
        return EvaluationAssertionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        evaluation_id: str,
        matcher: evaluation_assertion_create_params.Matcher,
        target: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertion:
        """
        Creates a new evaluation assertion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sdk/v1/evaluation-assertions",
            body=maybe_transform(
                {
                    "evaluation_id": evaluation_id,
                    "matcher": matcher,
                    "target": target,
                },
                evaluation_assertion_create_params.EvaluationAssertionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationAssertion,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertion:
        """
        Retrieve the details of an evaluation assertion using its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/sdk/v1/evaluation-assertions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationAssertion,
        )

    def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        matcher: evaluation_assertion_update_params.Matcher,
        target: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertion:
        """
        Update an existing evaluation assertion by providing its ID and new data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/sdk/v1/evaluation-assertions/{id}",
            body=maybe_transform(
                {
                    "evaluation_id": evaluation_id,
                    "matcher": matcher,
                    "target": target,
                },
                evaluation_assertion_update_params.EvaluationAssertionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationAssertion,
        )

    def list(
        self,
        *,
        evaluation_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertionListResponse:
        """
        Retrieve all evaluation assertions optionally filtered by evaluation ID

        Args:
          evaluation_id: Optional ID to filter the assertions by specific evaluation ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/sdk/v1/evaluation-assertions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"evaluation_id": evaluation_id}, evaluation_assertion_list_params.EvaluationAssertionListParams
                ),
            ),
            cast_to=EvaluationAssertionListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertionDeleteResponse:
        """
        Delete an evaluation assertion by providing its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/sdk/v1/evaluation-assertions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationAssertionDeleteResponse,
        )


class AsyncEvaluationAssertionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationAssertionsResourceWithRawResponse:
        return AsyncEvaluationAssertionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationAssertionsResourceWithStreamingResponse:
        return AsyncEvaluationAssertionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        evaluation_id: str,
        matcher: evaluation_assertion_create_params.Matcher,
        target: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertion:
        """
        Creates a new evaluation assertion

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sdk/v1/evaluation-assertions",
            body=await async_maybe_transform(
                {
                    "evaluation_id": evaluation_id,
                    "matcher": matcher,
                    "target": target,
                },
                evaluation_assertion_create_params.EvaluationAssertionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationAssertion,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertion:
        """
        Retrieve the details of an evaluation assertion using its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/sdk/v1/evaluation-assertions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationAssertion,
        )

    async def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        matcher: evaluation_assertion_update_params.Matcher,
        target: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertion:
        """
        Update an existing evaluation assertion by providing its ID and new data.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/sdk/v1/evaluation-assertions/{id}",
            body=await async_maybe_transform(
                {
                    "evaluation_id": evaluation_id,
                    "matcher": matcher,
                    "target": target,
                },
                evaluation_assertion_update_params.EvaluationAssertionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationAssertion,
        )

    async def list(
        self,
        *,
        evaluation_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertionListResponse:
        """
        Retrieve all evaluation assertions optionally filtered by evaluation ID

        Args:
          evaluation_id: Optional ID to filter the assertions by specific evaluation ID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/sdk/v1/evaluation-assertions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"evaluation_id": evaluation_id}, evaluation_assertion_list_params.EvaluationAssertionListParams
                ),
            ),
            cast_to=EvaluationAssertionListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertionDeleteResponse:
        """
        Delete an evaluation assertion by providing its ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/sdk/v1/evaluation-assertions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=EvaluationAssertionDeleteResponse,
        )


class EvaluationAssertionsResourceWithRawResponse:
    def __init__(self, evaluation_assertions: EvaluationAssertionsResource) -> None:
        self._evaluation_assertions = evaluation_assertions

        self.create = to_raw_response_wrapper(
            evaluation_assertions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            evaluation_assertions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            evaluation_assertions.update,
        )
        self.list = to_raw_response_wrapper(
            evaluation_assertions.list,
        )
        self.delete = to_raw_response_wrapper(
            evaluation_assertions.delete,
        )


class AsyncEvaluationAssertionsResourceWithRawResponse:
    def __init__(self, evaluation_assertions: AsyncEvaluationAssertionsResource) -> None:
        self._evaluation_assertions = evaluation_assertions

        self.create = async_to_raw_response_wrapper(
            evaluation_assertions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            evaluation_assertions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            evaluation_assertions.update,
        )
        self.list = async_to_raw_response_wrapper(
            evaluation_assertions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            evaluation_assertions.delete,
        )


class EvaluationAssertionsResourceWithStreamingResponse:
    def __init__(self, evaluation_assertions: EvaluationAssertionsResource) -> None:
        self._evaluation_assertions = evaluation_assertions

        self.create = to_streamed_response_wrapper(
            evaluation_assertions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            evaluation_assertions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            evaluation_assertions.update,
        )
        self.list = to_streamed_response_wrapper(
            evaluation_assertions.list,
        )
        self.delete = to_streamed_response_wrapper(
            evaluation_assertions.delete,
        )


class AsyncEvaluationAssertionsResourceWithStreamingResponse:
    def __init__(self, evaluation_assertions: AsyncEvaluationAssertionsResource) -> None:
        self._evaluation_assertions = evaluation_assertions

        self.create = async_to_streamed_response_wrapper(
            evaluation_assertions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            evaluation_assertions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            evaluation_assertions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            evaluation_assertions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            evaluation_assertions.delete,
        )
