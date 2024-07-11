# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from prompt_foundry_python_sdk import PromptFoundry, AsyncPromptFoundry
from prompt_foundry_python_sdk.types import (
    EvaluationAssertion,
    EvaluationAssertionListResponse,
    EvaluationAssertionDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvaluationAssertions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: PromptFoundry) -> None:
        evaluation_assertion = client.evaluation_assertions.create(
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: PromptFoundry) -> None:
        response = client.evaluation_assertions.with_raw_response.create(
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_assertion = response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: PromptFoundry) -> None:
        with client.evaluation_assertions.with_streaming_response.create(
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_assertion = response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: PromptFoundry) -> None:
        evaluation_assertion = client.evaluation_assertions.update(
            id="1212121",
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: PromptFoundry) -> None:
        response = client.evaluation_assertions.with_raw_response.update(
            id="1212121",
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_assertion = response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: PromptFoundry) -> None:
        with client.evaluation_assertions.with_streaming_response.update(
            id="1212121",
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_assertion = response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.evaluation_assertions.with_raw_response.update(
                id="",
                evaluation_id="evaluationId",
                json_path="jsonPath",
                target_value="targetValue",
                tool_name="toolName",
                type="CONTAINS",
            )

    @parametrize
    def test_method_list(self, client: PromptFoundry) -> None:
        evaluation_assertion = client.evaluation_assertions.list()
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: PromptFoundry) -> None:
        evaluation_assertion = client.evaluation_assertions.list(
            evaluation_id="eval-1234",
        )
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: PromptFoundry) -> None:
        response = client.evaluation_assertions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_assertion = response.parse()
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: PromptFoundry) -> None:
        with client.evaluation_assertions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_assertion = response.parse()
            assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: PromptFoundry) -> None:
        evaluation_assertion = client.evaluation_assertions.delete(
            "1212121",
        )
        assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: PromptFoundry) -> None:
        response = client.evaluation_assertions.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_assertion = response.parse()
        assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: PromptFoundry) -> None:
        with client.evaluation_assertions.with_streaming_response.delete(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_assertion = response.parse()
            assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.evaluation_assertions.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_get(self, client: PromptFoundry) -> None:
        evaluation_assertion = client.evaluation_assertions.get(
            "1212121",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: PromptFoundry) -> None:
        response = client.evaluation_assertions.with_raw_response.get(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_assertion = response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: PromptFoundry) -> None:
        with client.evaluation_assertions.with_streaming_response.get(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_assertion = response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.evaluation_assertions.with_raw_response.get(
                "",
            )


class TestAsyncEvaluationAssertions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncPromptFoundry) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.create(
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.evaluation_assertions.with_raw_response.create(
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_assertion = await response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.evaluation_assertions.with_streaming_response.create(
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_assertion = await response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncPromptFoundry) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.update(
            id="1212121",
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.evaluation_assertions.with_raw_response.update(
            id="1212121",
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_assertion = await response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.evaluation_assertions.with_streaming_response.update(
            id="1212121",
            evaluation_id="evaluationId",
            json_path="jsonPath",
            target_value="targetValue",
            tool_name="toolName",
            type="CONTAINS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_assertion = await response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.evaluation_assertions.with_raw_response.update(
                id="",
                evaluation_id="evaluationId",
                json_path="jsonPath",
                target_value="targetValue",
                tool_name="toolName",
                type="CONTAINS",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncPromptFoundry) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.list()
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPromptFoundry) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.list(
            evaluation_id="eval-1234",
        )
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.evaluation_assertions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_assertion = await response.parse()
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.evaluation_assertions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_assertion = await response.parse()
            assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPromptFoundry) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.delete(
            "1212121",
        )
        assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.evaluation_assertions.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_assertion = await response.parse()
        assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.evaluation_assertions.with_streaming_response.delete(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_assertion = await response.parse()
            assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.evaluation_assertions.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncPromptFoundry) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.get(
            "1212121",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncPromptFoundry) -> None:
        response = await async_client.evaluation_assertions.with_raw_response.get(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        evaluation_assertion = await response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.evaluation_assertions.with_streaming_response.get(
            "1212121",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            evaluation_assertion = await response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.evaluation_assertions.with_raw_response.get(
                "",
            )
