# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prompt_foundry_python_sdk import PromptFoundry, AsyncPromptFoundry
from prompt_foundry_python_sdk.types import (
    Evaluation,
    EvaluationListResponse,
    EvaluationDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PromptFoundry) -> None:
        evaluation = client.evaluations.create(
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        )
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PromptFoundry) -> None:
        response = client.evaluations.with_raw_response.create(
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PromptFoundry) -> None:
        with client.evaluations.with_streaming_response.create(
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(Evaluation, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: PromptFoundry) -> None:
        evaluation = client.evaluations.update(
            id="1212121",
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        )
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: PromptFoundry) -> None:
        response = client.evaluations.with_raw_response.update(
            id="1212121",
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: PromptFoundry) -> None:
        with client.evaluations.with_streaming_response.update(
            id="1212121",
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(Evaluation, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.evaluations.with_raw_response.update(
                id="",
                appended_messages=[
                    {
                        "content": "content",
                        "role": "assistant",
                        "tool_call_id": "toolCallId",
                        "tool_calls": [
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                        ],
                    },
                    {
                        "content": "content",
                        "role": "assistant",
                        "tool_call_id": "toolCallId",
                        "tool_calls": [
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                        ],
                    },
                    {
                        "content": "content",
                        "role": "assistant",
                        "tool_call_id": "toolCallId",
                        "tool_calls": [
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                        ],
                    },
                ],
                prompt_id="promptId",
                variables={"foo": "string"},
            )

    @parametrize
    def test_method_list(self, client: PromptFoundry) -> None:
        evaluation = client.evaluations.list()
        assert_matches_type(EvaluationListResponse, evaluation, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: PromptFoundry) -> None:
        response = client.evaluations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(EvaluationListResponse, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: PromptFoundry) -> None:
        with client.evaluations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(EvaluationListResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: PromptFoundry) -> None:
        evaluation = client.evaluations.delete(
            "1212121",
        )
        assert_matches_type(EvaluationDeleteResponse, evaluation, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: PromptFoundry) -> None:
        response = client.evaluations.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(EvaluationDeleteResponse, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: PromptFoundry) -> None:
        with client.evaluations.with_streaming_response.delete(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(EvaluationDeleteResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.evaluations.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: PromptFoundry) -> None:
        evaluation = client.evaluations.get(
            "1212121",
        )
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: PromptFoundry) -> None:
        response = client.evaluations.with_raw_response.get(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = response.parse()
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: PromptFoundry) -> None:
        with client.evaluations.with_streaming_response.get(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = response.parse()
            assert_matches_type(Evaluation, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.evaluations.with_raw_response.get(
                "",
            )


class TestAsyncEvaluations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPromptFoundry) -> None:
        evaluation = await async_client.evaluations.create(
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        )
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.evaluations.with_raw_response.create(
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.evaluations.with_streaming_response.create(
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(Evaluation, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncPromptFoundry) -> None:
        evaluation = await async_client.evaluations.update(
            id="1212121",
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        )
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.evaluations.with_raw_response.update(
            id="1212121",
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.evaluations.with_streaming_response.update(
            id="1212121",
            appended_messages=[
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
                {
                    "content": "content",
                    "role": "assistant",
                    "tool_call_id": "toolCallId",
                    "tool_calls": [
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                        {
                            "tool_call_id": "toolCallId",
                            "type": "function",
                            "function": {
                                "arguments": "arguments",
                                "name": "name",
                            },
                        },
                    ],
                },
            ],
            prompt_id="promptId",
            variables={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(Evaluation, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.evaluations.with_raw_response.update(
                id="",
                appended_messages=[
                    {
                        "content": "content",
                        "role": "assistant",
                        "tool_call_id": "toolCallId",
                        "tool_calls": [
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                        ],
                    },
                    {
                        "content": "content",
                        "role": "assistant",
                        "tool_call_id": "toolCallId",
                        "tool_calls": [
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                        ],
                    },
                    {
                        "content": "content",
                        "role": "assistant",
                        "tool_call_id": "toolCallId",
                        "tool_calls": [
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                            {
                                "tool_call_id": "toolCallId",
                                "type": "function",
                                "function": {
                                    "arguments": "arguments",
                                    "name": "name",
                                },
                            },
                        ],
                    },
                ],
                prompt_id="promptId",
                variables={"foo": "string"},
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPromptFoundry) -> None:
        evaluation = await async_client.evaluations.list()
        assert_matches_type(EvaluationListResponse, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.evaluations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(EvaluationListResponse, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.evaluations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(EvaluationListResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPromptFoundry) -> None:
        evaluation = await async_client.evaluations.delete(
            "1212121",
        )
        assert_matches_type(EvaluationDeleteResponse, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.evaluations.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(EvaluationDeleteResponse, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.evaluations.with_streaming_response.delete(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(EvaluationDeleteResponse, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.evaluations.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPromptFoundry) -> None:
        evaluation = await async_client.evaluations.get(
            "1212121",
        )
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.evaluations.with_raw_response.get(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation = await response.parse()
        assert_matches_type(Evaluation, evaluation, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.evaluations.with_streaming_response.get(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation = await response.parse()
            assert_matches_type(Evaluation, evaluation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.evaluations.with_raw_response.get(
                "",
            )
