# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prompt_foundry_python_sdk import PromptFoundry, AsyncPromptFoundry
from prompt_foundry_python_sdk.types import CompletionCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCompletion:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PromptFoundry) -> None:
        completion = client.completion.create(
            id="1212121",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: PromptFoundry) -> None:
        completion = client.completion.create(
            id="1212121",
            append_messages=[
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
            ],
            override_messages=[
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
            ],
            user="user",
            variables={"foo": "string"},
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PromptFoundry) -> None:
        response = client.completion.with_raw_response.create(
            id="1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PromptFoundry) -> None:
        with client.completion.with_streaming_response.create(
            id="1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.completion.with_raw_response.create(
                id="",
            )


class TestAsyncCompletion:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPromptFoundry) -> None:
        completion = await async_client.completion.create(
            id="1212121",
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncPromptFoundry) -> None:
        completion = await async_client.completion.create(
            id="1212121",
            append_messages=[
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
            ],
            override_messages=[
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
                {
                    "content": [
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                        {
                            "type": "TEXT",
                            "text": "text",
                        },
                    ],
                    "role": "assistant",
                },
            ],
            user="user",
            variables={"foo": "string"},
        )
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.completion.with_raw_response.create(
            id="1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        completion = await response.parse()
        assert_matches_type(CompletionCreateResponse, completion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.completion.with_streaming_response.create(
            id="1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            completion = await response.parse()
            assert_matches_type(CompletionCreateResponse, completion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.completion.with_raw_response.create(
                id="",
            )
