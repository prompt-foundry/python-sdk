# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, Optional, cast, overload
from typing_extensions import Literal

import httpx

from ..types import (
    evaluation_assertion_list_params,
    evaluation_assertion_create_params,
    evaluation_assertion_update_params,
)
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    required_args,
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
from ..types.evaluation_assertion import EvaluationAssertion
from ..types.evaluation_assertion_list_response import EvaluationAssertionListResponse
from ..types.evaluation_assertion_delete_response import EvaluationAssertionDeleteResponse

__all__ = ["EvaluationAssertionsResource", "AsyncEvaluationAssertionsResource"]


class EvaluationAssertionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EvaluationAssertionsResourceWithRawResponse:
        return EvaluationAssertionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EvaluationAssertionsResourceWithStreamingResponse:
        return EvaluationAssertionsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        evaluation_id: str,
        target_value: str,
        type: Literal["EXACT_MATCH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_value: The value to match.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        evaluation_id: str,
        target_values: List[str],
        type: Literal["CONTAINS_ALL"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_values: List of values any of which may be present.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        evaluation_id: str,
        target_values: List[str],
        type: Literal["CONTAINS_ANY"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_values: List of values any of which may be present.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        evaluation_id: str,
        target_value: str,
        type: Literal["STARTS_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_value: The value that the response should start with.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        evaluation_id: str,
        target_threshold: float,
        type: Literal["COST"],
        weight: float | NotGiven = NOT_GIVEN,
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
          target_threshold: The cost threshold to be evaluated against.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        evaluation_id: str,
        target_threshold: float,
        type: Literal["LATENCY"],
        weight: float | NotGiven = NOT_GIVEN,
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
          target_threshold: The latency threshold to be evaluated against.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        evaluation_id: str,
        tool_name: str,
        type: Literal["TOOL_CALLED"],
        weight: float | NotGiven = NOT_GIVEN,
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
          tool_name: The name of the tool that should have been called.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        arg_key_name: str,
        evaluation_id: str,
        tool_name: str,
        type: Literal["TOOL_CALLED_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          arg_key_name: The argument name to be matched.

          tool_name: The name of the tool that should have been called.

          ignore_case: Whether to ignore case when comparing argument names.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["evaluation_id", "target_value", "type"],
        ["evaluation_id", "target_values", "type"],
        ["evaluation_id", "target_threshold", "type"],
        ["evaluation_id", "tool_name", "type"],
        ["arg_key_name", "evaluation_id", "tool_name", "type"],
    )
    def create(
        self,
        *,
        evaluation_id: str,
        target_value: str | NotGiven = NOT_GIVEN,
        type: Literal["EXACT_MATCH"]
        | Literal["CONTAINS_ALL"]
        | Literal["CONTAINS_ANY"]
        | Literal["STARTS_WITH"]
        | Literal["COST"]
        | Literal["LATENCY"]
        | Literal["TOOL_CALLED"]
        | Literal["TOOL_CALLED_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
        target_values: List[str] | NotGiven = NOT_GIVEN,
        target_threshold: float | NotGiven = NOT_GIVEN,
        tool_name: str | NotGiven = NOT_GIVEN,
        arg_key_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertion:
        return cast(
            EvaluationAssertion,
            self._post(
                "/sdk/v1/evaluation-assertions",
                body=maybe_transform(
                    {
                        "evaluation_id": evaluation_id,
                        "target_value": target_value,
                        "type": type,
                        "ignore_case": ignore_case,
                        "json_path": json_path,
                        "negate": negate,
                        "weight": weight,
                        "target_values": target_values,
                        "target_threshold": target_threshold,
                        "tool_name": tool_name,
                        "arg_key_name": arg_key_name,
                    },
                    evaluation_assertion_create_params.EvaluationAssertionCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EvaluationAssertion
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_value: str,
        type: Literal["EXACT_MATCH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_value: The value to match.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_values: List[str],
        type: Literal["CONTAINS_ALL"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_values: List of values any of which may be present.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_values: List[str],
        type: Literal["CONTAINS_ANY"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_values: List of values any of which may be present.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_value: str,
        type: Literal["STARTS_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_value: The value that the response should start with.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_threshold: float,
        type: Literal["COST"],
        weight: float | NotGiven = NOT_GIVEN,
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
          target_threshold: The cost threshold to be evaluated against.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_threshold: float,
        type: Literal["LATENCY"],
        weight: float | NotGiven = NOT_GIVEN,
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
          target_threshold: The latency threshold to be evaluated against.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        tool_name: str,
        type: Literal["TOOL_CALLED"],
        weight: float | NotGiven = NOT_GIVEN,
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
          tool_name: The name of the tool that should have been called.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        arg_key_name: str,
        evaluation_id: str,
        tool_name: str,
        type: Literal["TOOL_CALLED_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          arg_key_name: The argument name to be matched.

          tool_name: The name of the tool that should have been called.

          ignore_case: Whether to ignore case when comparing argument names.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["evaluation_id", "target_value", "type"],
        ["evaluation_id", "target_values", "type"],
        ["evaluation_id", "target_threshold", "type"],
        ["evaluation_id", "tool_name", "type"],
        ["arg_key_name", "evaluation_id", "tool_name", "type"],
    )
    def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_value: str | NotGiven = NOT_GIVEN,
        type: Literal["EXACT_MATCH"]
        | Literal["CONTAINS_ALL"]
        | Literal["CONTAINS_ANY"]
        | Literal["STARTS_WITH"]
        | Literal["COST"]
        | Literal["LATENCY"]
        | Literal["TOOL_CALLED"]
        | Literal["TOOL_CALLED_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
        target_values: List[str] | NotGiven = NOT_GIVEN,
        target_threshold: float | NotGiven = NOT_GIVEN,
        tool_name: str | NotGiven = NOT_GIVEN,
        arg_key_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertion:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            EvaluationAssertion,
            self._put(
                f"/sdk/v1/evaluation-assertions/{id}",
                body=maybe_transform(
                    {
                        "evaluation_id": evaluation_id,
                        "target_value": target_value,
                        "type": type,
                        "ignore_case": ignore_case,
                        "json_path": json_path,
                        "negate": negate,
                        "weight": weight,
                        "target_values": target_values,
                        "target_threshold": target_threshold,
                        "tool_name": tool_name,
                        "arg_key_name": arg_key_name,
                    },
                    evaluation_assertion_update_params.EvaluationAssertionUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EvaluationAssertion
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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

    def get(
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
        return cast(
            EvaluationAssertion,
            self._get(
                f"/sdk/v1/evaluation-assertions/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EvaluationAssertion
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncEvaluationAssertionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEvaluationAssertionsResourceWithRawResponse:
        return AsyncEvaluationAssertionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEvaluationAssertionsResourceWithStreamingResponse:
        return AsyncEvaluationAssertionsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        evaluation_id: str,
        target_value: str,
        type: Literal["EXACT_MATCH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_value: The value to match.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        evaluation_id: str,
        target_values: List[str],
        type: Literal["CONTAINS_ALL"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_values: List of values any of which may be present.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        evaluation_id: str,
        target_values: List[str],
        type: Literal["CONTAINS_ANY"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_values: List of values any of which may be present.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        evaluation_id: str,
        target_value: str,
        type: Literal["STARTS_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_value: The value that the response should start with.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        evaluation_id: str,
        target_threshold: float,
        type: Literal["COST"],
        weight: float | NotGiven = NOT_GIVEN,
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
          target_threshold: The cost threshold to be evaluated against.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        evaluation_id: str,
        target_threshold: float,
        type: Literal["LATENCY"],
        weight: float | NotGiven = NOT_GIVEN,
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
          target_threshold: The latency threshold to be evaluated against.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        evaluation_id: str,
        tool_name: str,
        type: Literal["TOOL_CALLED"],
        weight: float | NotGiven = NOT_GIVEN,
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
          tool_name: The name of the tool that should have been called.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        arg_key_name: str,
        evaluation_id: str,
        tool_name: str,
        type: Literal["TOOL_CALLED_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          arg_key_name: The argument name to be matched.

          tool_name: The name of the tool that should have been called.

          ignore_case: Whether to ignore case when comparing argument names.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["evaluation_id", "target_value", "type"],
        ["evaluation_id", "target_values", "type"],
        ["evaluation_id", "target_threshold", "type"],
        ["evaluation_id", "tool_name", "type"],
        ["arg_key_name", "evaluation_id", "tool_name", "type"],
    )
    async def create(
        self,
        *,
        evaluation_id: str,
        target_value: str | NotGiven = NOT_GIVEN,
        type: Literal["EXACT_MATCH"]
        | Literal["CONTAINS_ALL"]
        | Literal["CONTAINS_ANY"]
        | Literal["STARTS_WITH"]
        | Literal["COST"]
        | Literal["LATENCY"]
        | Literal["TOOL_CALLED"]
        | Literal["TOOL_CALLED_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
        target_values: List[str] | NotGiven = NOT_GIVEN,
        target_threshold: float | NotGiven = NOT_GIVEN,
        tool_name: str | NotGiven = NOT_GIVEN,
        arg_key_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertion:
        return cast(
            EvaluationAssertion,
            await self._post(
                "/sdk/v1/evaluation-assertions",
                body=await async_maybe_transform(
                    {
                        "evaluation_id": evaluation_id,
                        "target_value": target_value,
                        "type": type,
                        "ignore_case": ignore_case,
                        "json_path": json_path,
                        "negate": negate,
                        "weight": weight,
                        "target_values": target_values,
                        "target_threshold": target_threshold,
                        "tool_name": tool_name,
                        "arg_key_name": arg_key_name,
                    },
                    evaluation_assertion_create_params.EvaluationAssertionCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EvaluationAssertion
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_value: str,
        type: Literal["EXACT_MATCH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_value: The value to match.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_values: List[str],
        type: Literal["CONTAINS_ALL"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_values: List of values any of which may be present.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_values: List[str],
        type: Literal["CONTAINS_ANY"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_values: List of values any of which may be present.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_value: str,
        type: Literal["STARTS_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          target_value: The value that the response should start with.

          ignore_case: Whether to ignore case when comparing strings.

          json_path: A JSON path to use when matching a JSON response.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_threshold: float,
        type: Literal["COST"],
        weight: float | NotGiven = NOT_GIVEN,
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
          target_threshold: The cost threshold to be evaluated against.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_threshold: float,
        type: Literal["LATENCY"],
        weight: float | NotGiven = NOT_GIVEN,
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
          target_threshold: The latency threshold to be evaluated against.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        tool_name: str,
        type: Literal["TOOL_CALLED"],
        weight: float | NotGiven = NOT_GIVEN,
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
          tool_name: The name of the tool that should have been called.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        arg_key_name: str,
        evaluation_id: str,
        tool_name: str,
        type: Literal["TOOL_CALLED_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
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
          arg_key_name: The argument name to be matched.

          tool_name: The name of the tool that should have been called.

          ignore_case: Whether to ignore case when comparing argument names.

          negate: Whether to negate the assertion. "true" means the assertion must NOT be true.

          weight: How heavily to weigh the assertion within the evaluation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["evaluation_id", "target_value", "type"],
        ["evaluation_id", "target_values", "type"],
        ["evaluation_id", "target_threshold", "type"],
        ["evaluation_id", "tool_name", "type"],
        ["arg_key_name", "evaluation_id", "tool_name", "type"],
    )
    async def update(
        self,
        id: str,
        *,
        evaluation_id: str,
        target_value: str | NotGiven = NOT_GIVEN,
        type: Literal["EXACT_MATCH"]
        | Literal["CONTAINS_ALL"]
        | Literal["CONTAINS_ANY"]
        | Literal["STARTS_WITH"]
        | Literal["COST"]
        | Literal["LATENCY"]
        | Literal["TOOL_CALLED"]
        | Literal["TOOL_CALLED_WITH"],
        ignore_case: bool | NotGiven = NOT_GIVEN,
        json_path: Optional[str] | NotGiven = NOT_GIVEN,
        negate: bool | NotGiven = NOT_GIVEN,
        weight: float | NotGiven = NOT_GIVEN,
        target_values: List[str] | NotGiven = NOT_GIVEN,
        target_threshold: float | NotGiven = NOT_GIVEN,
        tool_name: str | NotGiven = NOT_GIVEN,
        arg_key_name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EvaluationAssertion:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            EvaluationAssertion,
            await self._put(
                f"/sdk/v1/evaluation-assertions/{id}",
                body=await async_maybe_transform(
                    {
                        "evaluation_id": evaluation_id,
                        "target_value": target_value,
                        "type": type,
                        "ignore_case": ignore_case,
                        "json_path": json_path,
                        "negate": negate,
                        "weight": weight,
                        "target_values": target_values,
                        "target_threshold": target_threshold,
                        "tool_name": tool_name,
                        "arg_key_name": arg_key_name,
                    },
                    evaluation_assertion_update_params.EvaluationAssertionUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EvaluationAssertion
                ),  # Union types cannot be passed in as arguments in the type system
            ),
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

    async def get(
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
        return cast(
            EvaluationAssertion,
            await self._get(
                f"/sdk/v1/evaluation-assertions/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(
                    Any, EvaluationAssertion
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class EvaluationAssertionsResourceWithRawResponse:
    def __init__(self, evaluation_assertions: EvaluationAssertionsResource) -> None:
        self._evaluation_assertions = evaluation_assertions

        self.create = to_raw_response_wrapper(
            evaluation_assertions.create,
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
        self.get = to_raw_response_wrapper(
            evaluation_assertions.get,
        )


class AsyncEvaluationAssertionsResourceWithRawResponse:
    def __init__(self, evaluation_assertions: AsyncEvaluationAssertionsResource) -> None:
        self._evaluation_assertions = evaluation_assertions

        self.create = async_to_raw_response_wrapper(
            evaluation_assertions.create,
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
        self.get = async_to_raw_response_wrapper(
            evaluation_assertions.get,
        )


class EvaluationAssertionsResourceWithStreamingResponse:
    def __init__(self, evaluation_assertions: EvaluationAssertionsResource) -> None:
        self._evaluation_assertions = evaluation_assertions

        self.create = to_streamed_response_wrapper(
            evaluation_assertions.create,
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
        self.get = to_streamed_response_wrapper(
            evaluation_assertions.get,
        )


class AsyncEvaluationAssertionsResourceWithStreamingResponse:
    def __init__(self, evaluation_assertions: AsyncEvaluationAssertionsResource) -> None:
        self._evaluation_assertions = evaluation_assertions

        self.create = async_to_streamed_response_wrapper(
            evaluation_assertions.create,
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
        self.get = async_to_streamed_response_wrapper(
            evaluation_assertions.get,
        )
