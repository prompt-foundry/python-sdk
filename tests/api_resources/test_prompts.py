# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prompt_foundry_python_sdk import PromptFoundry, AsyncPromptFoundry
from prompt_foundry_python_sdk.types import (
    ModelParameters,
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
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
        )
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PromptFoundry) -> None:
        response = client.prompts.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
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
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: PromptFoundry) -> None:
        prompt = client.prompts.update(
            "1212121",
            messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
        )
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: PromptFoundry) -> None:
        response = client.prompts.with_raw_response.update(
            "1212121",
            messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.update(
            "1212121",
            messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
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
                "",
                messages=[
                    {
                        "content": "string",
                        "role": "assistant",
                        "tool_call_id": "string",
                        "tool_calls": [
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                        ],
                    },
                    {
                        "content": "string",
                        "role": "assistant",
                        "tool_call_id": "string",
                        "tool_calls": [
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                        ],
                    },
                    {
                        "content": "string",
                        "role": "assistant",
                        "tool_call_id": "string",
                        "tool_calls": [
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                        ],
                    },
                ],
                name="string",
                parameters={
                    "model_provider": "OPENAI",
                    "model_name": "string",
                    "response_format": "JSON",
                    "temperature": 0,
                    "top_p": 0,
                    "frequency_penalty": 0,
                    "presence_penalty": 0,
                    "max_tokens": 0,
                    "seed": 0,
                    "tool_choice": "string",
                    "stream": True,
                    "parallel_tool_calls": True,
                },
                tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
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
            "1212121",
        )
        assert_matches_type(ModelParameters, prompt, path=["response"])

    @parametrize
    def test_method_get_parameters_with_all_params(self, client: PromptFoundry) -> None:
        prompt = client.prompts.get_parameters(
            "1212121",
            append_messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            override_messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            user="string",
            variables={"foo": "string"},
        )
        assert_matches_type(ModelParameters, prompt, path=["response"])

    @parametrize
    def test_raw_response_get_parameters(self, client: PromptFoundry) -> None:
        response = client.prompts.with_raw_response.get_parameters(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = response.parse()
        assert_matches_type(ModelParameters, prompt, path=["response"])

    @parametrize
    def test_streaming_response_get_parameters(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.get_parameters(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = response.parse()
            assert_matches_type(ModelParameters, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get_parameters(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.prompts.with_raw_response.get_parameters(
                "",
            )


class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.create(
            messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
        )
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.prompts.with_raw_response.create(
            messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
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
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.update(
            "1212121",
            messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
        )
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.prompts.with_raw_response.update(
            "1212121",
            messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.update(
            "1212121",
            messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            name="string",
            parameters={
                "model_provider": "OPENAI",
                "model_name": "string",
                "response_format": "JSON",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
                "stream": True,
                "parallel_tool_calls": True,
            },
            tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
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
                "",
                messages=[
                    {
                        "content": "string",
                        "role": "assistant",
                        "tool_call_id": "string",
                        "tool_calls": [
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                        ],
                    },
                    {
                        "content": "string",
                        "role": "assistant",
                        "tool_call_id": "string",
                        "tool_calls": [
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                        ],
                    },
                    {
                        "content": "string",
                        "role": "assistant",
                        "tool_call_id": "string",
                        "tool_calls": [
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                            {
                                "tool_call_id": "string",
                                "type": "function",
                                "function": {
                                    "arguments": "string",
                                    "name": "string",
                                },
                            },
                        ],
                    },
                ],
                name="string",
                parameters={
                    "model_provider": "OPENAI",
                    "model_name": "string",
                    "response_format": "JSON",
                    "temperature": 0,
                    "top_p": 0,
                    "frequency_penalty": 0,
                    "presence_penalty": 0,
                    "max_tokens": 0,
                    "seed": 0,
                    "tool_choice": "string",
                    "stream": True,
                    "parallel_tool_calls": True,
                },
                tools=[{"tool_id": "string"}, {"tool_id": "string"}, {"tool_id": "string"}],
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
            "1212121",
        )
        assert_matches_type(ModelParameters, prompt, path=["response"])

    @parametrize
    async def test_method_get_parameters_with_all_params(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.get_parameters(
            "1212121",
            append_messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            override_messages=[
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
                {
                    "content": "string",
                    "role": "assistant",
                    "tool_call_id": "string",
                    "tool_calls": [
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                        {
                            "tool_call_id": "string",
                            "type": "function",
                            "function": {
                                "arguments": "string",
                                "name": "string",
                            },
                        },
                    ],
                },
            ],
            user="string",
            variables={"foo": "string"},
        )
        assert_matches_type(ModelParameters, prompt, path=["response"])

    @parametrize
    async def test_raw_response_get_parameters(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.prompts.with_raw_response.get_parameters(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prompt = await response.parse()
        assert_matches_type(ModelParameters, prompt, path=["response"])

    @parametrize
    async def test_streaming_response_get_parameters(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.get_parameters(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prompt = await response.parse()
            assert_matches_type(ModelParameters, prompt, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get_parameters(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.prompts.with_raw_response.get_parameters(
                "",
            )
