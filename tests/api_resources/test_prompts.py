# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prompt_foundry_python_sdk import PromptFoundry, AsyncPromptFoundry
from prompt_foundry_python_sdk.types import (
    Parameters,
    PromptListResponse,
    PromptConfiguration,
    PromptDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PromptFoundry) -> None:
        prompt = client.prompts.create(
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        )
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PromptFoundry) -> None:
        response = client.prompts.with_raw_response.create(
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.create(
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: PromptFoundry) -> None:
        prompt = client.prompts.update(
            id="1212121",
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        )
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: PromptFoundry) -> None:
        response = client.prompts.with_raw_response.update(
            id="1212121",
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.update(
            id="1212121",
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.with_raw_response.update(
                id="",
                messages=[
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
                        "prompt_message_id": "promptMessageId",
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
                        "prompt_message_id": "promptMessageId",
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
                        "prompt_message_id": "promptMessageId",
                    },
                ],
                name="name",
                parameters={
                    "provider": "ANTHROPIC",
                    "name": "name",
                    "response_format": "JSON",
                    "temperature": 0,
                    "top_p": 0,
                    "top_k": 1,
                    "frequency_penalty": 0,
                    "presence_penalty": 0,
                    "max_tokens": 0,
                    "seed": 0,
                    "tool_choice": "toolChoice",
                    "stream": True,
                    "parallel_tool_calls": True,
                },
                tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
            )

    @parametrize
    def test_method_list(self, client: PromptFoundry) -> None:
        prompt = client.prompts.list()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: PromptFoundry) -> None:
        response = client.prompts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: PromptFoundry) -> None:
        prompt = client.prompts.delete(
            "1212121",
        )
        assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: PromptFoundry) -> None:
        response = client.prompts.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.delete(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: PromptFoundry) -> None:
        prompt = client.prompts.get(
            "1212121",
        )
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: PromptFoundry) -> None:
        response = client.prompts.with_raw_response.get(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.get(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_get_parameters(self, client: PromptFoundry) -> None:
        prompt = client.prompts.get_parameters(
            id="1212121",
        )
        assert_matches_type(Parameters, prompt, path=["response"])

    @parametrize
    def test_method_get_parameters_with_all_params(self, client: PromptFoundry) -> None:
        prompt = client.prompts.get_parameters(
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
        assert_matches_type(Parameters, prompt, path=["response"])

    @parametrize
    def test_raw_response_get_parameters(self, client: PromptFoundry) -> None:
        response = client.prompts.with_raw_response.get_parameters(
            id="1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(Parameters, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get_parameters(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.get_parameters(
            id="1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(Parameters, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_parameters(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.with_raw_response.get_parameters(
                id="",
            )


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.create(
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        )
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.prompts.with_raw_response.create(
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.create(
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.update(
            id="1212121",
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        )
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.prompts.with_raw_response.update(
            id="1212121",
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.update(
            id="1212121",
            messages=[
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
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
                    "prompt_message_id": "promptMessageId",
                },
            ],
            name="name",
            parameters={
                "provider": "ANTHROPIC",
                "name": "name",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "top_k": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "toolChoice",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.with_raw_response.update(
                id="",
                messages=[
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
                        "prompt_message_id": "promptMessageId",
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
                        "prompt_message_id": "promptMessageId",
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
                        "prompt_message_id": "promptMessageId",
                    },
                ],
                name="name",
                parameters={
                    "provider": "ANTHROPIC",
                    "name": "name",
                    "response_format": "JSON",
                    "temperature": 0,
                    "top_p": 0,
                    "top_k": 1,
                    "frequency_penalty": 0,
                    "presence_penalty": 0,
                    "max_tokens": 0,
                    "seed": 0,
                    "tool_choice": "toolChoice",
                    "stream": True,
                    "parallel_tool_calls": True,
                },
                tools=[{"tool_id": "toolId"}, {"tool_id": "toolId"}, {"tool_id": "toolId"}],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.list()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.prompts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptListResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptListResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.delete(
            "1212121",
        )
        assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.prompts.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.delete(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptDeleteResponse, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.get(
            "1212121",
        )
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.prompts.with_raw_response.get(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.get(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_get_parameters(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.get_parameters(
            id="1212121",
        )
        assert_matches_type(Parameters, prompt, path=["response"])

    @parametrize
    async def test_method_get_parameters_with_all_params(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.get_parameters(
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
        assert_matches_type(Parameters, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get_parameters(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.prompts.with_raw_response.get_parameters(
            id="1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(Parameters, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get_parameters(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.get_parameters(
            id="1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(Parameters, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_parameters(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.with_raw_response.get_parameters(
                id="",
            )
