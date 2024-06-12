# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from prompt-foundry-sdk import PromptFoundrySdk, AsyncPromptFoundrySdk

from prompt-foundry-sdk.types import EvaluationAssertion, EvaluationAssertionListResponse, EvaluationAssertionDeleteResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from prompt-foundry-sdk import PromptFoundrySdk, AsyncPromptFoundrySdk
from tests.utils import assert_matches_type
from prompt-foundry-sdk.types import evaluation_assertion_create_params
from prompt-foundry-sdk.types import evaluation_assertion_update_params
from prompt-foundry-sdk.types import evaluation_assertion_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestEvaluationAssertions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: PromptFoundrySdk) -> None:
        evaluation_assertion = client.evaluation_assertions.create(
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: PromptFoundrySdk) -> None:

        response = client.evaluation_assertions.with_raw_response.create(
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation_assertion = response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: PromptFoundrySdk) -> None:
        with client.evaluation_assertions.with_streaming_response.create(
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation_assertion = response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: PromptFoundrySdk) -> None:
        evaluation_assertion = client.evaluation_assertions.retrieve(
            "1212121",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: PromptFoundrySdk) -> None:

        response = client.evaluation_assertions.with_raw_response.retrieve(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation_assertion = response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: PromptFoundrySdk) -> None:
        with client.evaluation_assertions.with_streaming_response.retrieve(
            "1212121",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation_assertion = response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.evaluation_assertions.with_raw_response.retrieve(
              "",
          )

    @parametrize
    def test_method_update(self, client: PromptFoundrySdk) -> None:
        evaluation_assertion = client.evaluation_assertions.update(
            "1212121",
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: PromptFoundrySdk) -> None:

        response = client.evaluation_assertions.with_raw_response.update(
            "1212121",
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation_assertion = response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: PromptFoundrySdk) -> None:
        with client.evaluation_assertions.with_streaming_response.update(
            "1212121",
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation_assertion = response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: PromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.evaluation_assertions.with_raw_response.update(
              "",
              evaluation_id="string",
              matcher={
                  "type": "CONTAINS",
                  "json_path": "string",
              },
              target="string",
          )

    @parametrize
    def test_method_list(self, client: PromptFoundrySdk) -> None:
        evaluation_assertion = client.evaluation_assertions.list()
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=['response'])

    @parametrize
    def test_method_list_with_all_params(self, client: PromptFoundrySdk) -> None:
        evaluation_assertion = client.evaluation_assertions.list(
            evaluation_id="eval-1234",
        )
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: PromptFoundrySdk) -> None:

        response = client.evaluation_assertions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation_assertion = response.parse()
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: PromptFoundrySdk) -> None:
        with client.evaluation_assertions.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation_assertion = response.parse()
            assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: PromptFoundrySdk) -> None:
        evaluation_assertion = client.evaluation_assertions.delete(
            "1212121",
        )
        assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: PromptFoundrySdk) -> None:

        response = client.evaluation_assertions.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation_assertion = response.parse()
        assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: PromptFoundrySdk) -> None:
        with client.evaluation_assertions.with_streaming_response.delete(
            "1212121",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation_assertion = response.parse()
            assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: PromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.evaluation_assertions.with_raw_response.delete(
              "",
          )
class TestAsyncEvaluationAssertions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.create(
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPromptFoundrySdk) -> None:

        response = await async_client.evaluation_assertions.with_raw_response.create(
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation_assertion = await response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPromptFoundrySdk) -> None:
        async with async_client.evaluation_assertions.with_streaming_response.create(
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation_assertion = await response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.retrieve(
            "1212121",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPromptFoundrySdk) -> None:

        response = await async_client.evaluation_assertions.with_raw_response.retrieve(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation_assertion = await response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPromptFoundrySdk) -> None:
        async with async_client.evaluation_assertions.with_streaming_response.retrieve(
            "1212121",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation_assertion = await response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.evaluation_assertions.with_raw_response.retrieve(
              "",
          )

    @parametrize
    async def test_method_update(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.update(
            "1212121",
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        )
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPromptFoundrySdk) -> None:

        response = await async_client.evaluation_assertions.with_raw_response.update(
            "1212121",
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation_assertion = await response.parse()
        assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPromptFoundrySdk) -> None:
        async with async_client.evaluation_assertions.with_streaming_response.update(
            "1212121",
            evaluation_id="string",
            matcher={
                "type": "CONTAINS",
                "json_path": "string",
            },
            target="string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation_assertion = await response.parse()
            assert_matches_type(EvaluationAssertion, evaluation_assertion, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.evaluation_assertions.with_raw_response.update(
              "",
              evaluation_id="string",
              matcher={
                  "type": "CONTAINS",
                  "json_path": "string",
              },
              target="string",
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.list()
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=['response'])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.list(
            evaluation_id="eval-1234",
        )
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPromptFoundrySdk) -> None:

        response = await async_client.evaluation_assertions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation_assertion = await response.parse()
        assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPromptFoundrySdk) -> None:
        async with async_client.evaluation_assertions.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation_assertion = await response.parse()
            assert_matches_type(EvaluationAssertionListResponse, evaluation_assertion, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation_assertion = await async_client.evaluation_assertions.delete(
            "1212121",
        )
        assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPromptFoundrySdk) -> None:

        response = await async_client.evaluation_assertions.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation_assertion = await response.parse()
        assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPromptFoundrySdk) -> None:
        async with async_client.evaluation_assertions.with_streaming_response.delete(
            "1212121",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation_assertion = await response.parse()
            assert_matches_type(EvaluationAssertionDeleteResponse, evaluation_assertion, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.evaluation_assertions.with_raw_response.delete(
              "",
          )