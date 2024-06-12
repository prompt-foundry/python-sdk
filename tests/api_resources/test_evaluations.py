# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from prompt-foundry-sdk import PromptFoundrySdk, AsyncPromptFoundrySdk

from prompt-foundry-sdk.types import Evaluation, EvaluationListResponse, EvaluationDeleteResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from prompt-foundry-sdk import PromptFoundrySdk, AsyncPromptFoundrySdk
from tests.utils import assert_matches_type
from prompt-foundry-sdk.types import evaluation_create_params
from prompt-foundry-sdk.types import evaluation_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestEvaluations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: PromptFoundrySdk) -> None:
        evaluation = client.evaluations.create(
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        )
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: PromptFoundrySdk) -> None:

        response = client.evaluations.with_raw_response.create(
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation = response.parse()
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: PromptFoundrySdk) -> None:
        with client.evaluations.with_streaming_response.create(
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation = response.parse()
            assert_matches_type(Evaluation, evaluation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: PromptFoundrySdk) -> None:
        evaluation = client.evaluations.retrieve(
            "1212121",
        )
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: PromptFoundrySdk) -> None:

        response = client.evaluations.with_raw_response.retrieve(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation = response.parse()
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: PromptFoundrySdk) -> None:
        with client.evaluations.with_streaming_response.retrieve(
            "1212121",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation = response.parse()
            assert_matches_type(Evaluation, evaluation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.evaluations.with_raw_response.retrieve(
              "",
          )

    @parametrize
    def test_method_update(self, client: PromptFoundrySdk) -> None:
        evaluation = client.evaluations.update(
            "1212121",
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        )
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: PromptFoundrySdk) -> None:

        response = client.evaluations.with_raw_response.update(
            "1212121",
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation = response.parse()
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: PromptFoundrySdk) -> None:
        with client.evaluations.with_streaming_response.update(
            "1212121",
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation = response.parse()
            assert_matches_type(Evaluation, evaluation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: PromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.evaluations.with_raw_response.update(
              "",
              appended_messages=[{
                  "content": "string",
                  "role": "USER",
                  "tool_call_id": "string",
                  "tool_calls": [{
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }],
              }, {
                  "content": "string",
                  "role": "USER",
                  "tool_call_id": "string",
                  "tool_calls": [{
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }],
              }, {
                  "content": "string",
                  "role": "USER",
                  "tool_call_id": "string",
                  "tool_calls": [{
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }],
              }],
              prompt_id="string",
              variables={
                  "foo": {}
              },
          )

    @parametrize
    def test_method_list(self, client: PromptFoundrySdk) -> None:
        evaluation = client.evaluations.list()
        assert_matches_type(EvaluationListResponse, evaluation, path=['response'])

    @parametrize
    def test_raw_response_list(self, client: PromptFoundrySdk) -> None:

        response = client.evaluations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation = response.parse()
        assert_matches_type(EvaluationListResponse, evaluation, path=['response'])

    @parametrize
    def test_streaming_response_list(self, client: PromptFoundrySdk) -> None:
        with client.evaluations.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation = response.parse()
            assert_matches_type(EvaluationListResponse, evaluation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: PromptFoundrySdk) -> None:
        evaluation = client.evaluations.delete(
            "1212121",
        )
        assert_matches_type(EvaluationDeleteResponse, evaluation, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: PromptFoundrySdk) -> None:

        response = client.evaluations.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation = response.parse()
        assert_matches_type(EvaluationDeleteResponse, evaluation, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: PromptFoundrySdk) -> None:
        with client.evaluations.with_streaming_response.delete(
            "1212121",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation = response.parse()
            assert_matches_type(EvaluationDeleteResponse, evaluation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: PromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.evaluations.with_raw_response.delete(
              "",
          )
class TestAsyncEvaluations:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation = await async_client.evaluations.create(
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        )
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPromptFoundrySdk) -> None:

        response = await async_client.evaluations.with_raw_response.create(
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation = await response.parse()
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPromptFoundrySdk) -> None:
        async with async_client.evaluations.with_streaming_response.create(
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation = await response.parse()
            assert_matches_type(Evaluation, evaluation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation = await async_client.evaluations.retrieve(
            "1212121",
        )
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPromptFoundrySdk) -> None:

        response = await async_client.evaluations.with_raw_response.retrieve(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation = await response.parse()
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPromptFoundrySdk) -> None:
        async with async_client.evaluations.with_streaming_response.retrieve(
            "1212121",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation = await response.parse()
            assert_matches_type(Evaluation, evaluation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.evaluations.with_raw_response.retrieve(
              "",
          )

    @parametrize
    async def test_method_update(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation = await async_client.evaluations.update(
            "1212121",
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        )
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPromptFoundrySdk) -> None:

        response = await async_client.evaluations.with_raw_response.update(
            "1212121",
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation = await response.parse()
        assert_matches_type(Evaluation, evaluation, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPromptFoundrySdk) -> None:
        async with async_client.evaluations.with_streaming_response.update(
            "1212121",
            appended_messages=[{
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }, {
                "content": "string",
                "role": "USER",
                "tool_call_id": "string",
                "tool_calls": [{
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }, {
                    "tool_call_id": "string",
                    "type": "function",
                    "function": {
                        "arguments": "string",
                        "name": "string",
                    },
                }],
            }],
            prompt_id="string",
            variables={
                "foo": {}
            },
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation = await response.parse()
            assert_matches_type(Evaluation, evaluation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.evaluations.with_raw_response.update(
              "",
              appended_messages=[{
                  "content": "string",
                  "role": "USER",
                  "tool_call_id": "string",
                  "tool_calls": [{
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }],
              }, {
                  "content": "string",
                  "role": "USER",
                  "tool_call_id": "string",
                  "tool_calls": [{
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }],
              }, {
                  "content": "string",
                  "role": "USER",
                  "tool_call_id": "string",
                  "tool_calls": [{
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }, {
                      "tool_call_id": "string",
                      "type": "function",
                      "function": {
                          "arguments": "string",
                          "name": "string",
                      },
                  }],
              }],
              prompt_id="string",
              variables={
                  "foo": {}
              },
          )

    @parametrize
    async def test_method_list(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation = await async_client.evaluations.list()
        assert_matches_type(EvaluationListResponse, evaluation, path=['response'])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncPromptFoundrySdk) -> None:

        response = await async_client.evaluations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation = await response.parse()
        assert_matches_type(EvaluationListResponse, evaluation, path=['response'])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncPromptFoundrySdk) -> None:
        async with async_client.evaluations.with_streaming_response.list() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation = await response.parse()
            assert_matches_type(EvaluationListResponse, evaluation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncPromptFoundrySdk) -> None:
        evaluation = await async_client.evaluations.delete(
            "1212121",
        )
        assert_matches_type(EvaluationDeleteResponse, evaluation, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPromptFoundrySdk) -> None:

        response = await async_client.evaluations.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        evaluation = await response.parse()
        assert_matches_type(EvaluationDeleteResponse, evaluation, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPromptFoundrySdk) -> None:
        async with async_client.evaluations.with_streaming_response.delete(
            "1212121",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            evaluation = await response.parse()
            assert_matches_type(EvaluationDeleteResponse, evaluation, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPromptFoundrySdk) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.evaluations.with_raw_response.delete(
              "",
          )