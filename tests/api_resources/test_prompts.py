# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from prompt-foundry-sdk import PromptFoundry, AsyncPromptFoundry

from prompt-foundry-sdk.types import PromptConfiguration, PromptDeleteResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from prompt-foundry-sdk import PromptFoundry, AsyncPromptFoundry
from tests.utils import assert_matches_type
from prompt-foundry-sdk.types import prompt_create_params
from prompt-foundry-sdk.types import prompt_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestPrompts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: PromptFoundry) -> None:
        prompt = client.prompts.create(
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        )
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: PromptFoundry) -> None:

        response = client.prompts.with_raw_response.create(
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        prompt = response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.create(
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            prompt = response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: PromptFoundry) -> None:
        prompt = client.prompts.retrieve(
            "string",
        )
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    def test_raw_response_retrieve(self, client: PromptFoundry) -> None:

        response = client.prompts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        prompt = response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    def test_streaming_response_retrieve(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.retrieve(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            prompt = response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
          client.prompts.with_raw_response.retrieve(
              "",
          )

    @parametrize
    def test_method_update(self, client: PromptFoundry) -> None:
        prompt = client.prompts.update(
            "string",
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        )
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: PromptFoundry) -> None:

        response = client.prompts.with_raw_response.update(
            "string",
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        prompt = response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.update(
            "string",
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            prompt = response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
          client.prompts.with_raw_response.update(
              "",
              messages=[{
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
              name="string",
              parameters={
                  "model_name": "string",
                  "response_format": "TEXT",
                  "temperature": 0,
                  "top_p": 0,
                  "frequency_penalty": 0,
                  "presence_penalty": 0,
                  "max_tokens": 0,
                  "seed": 0,
                  "tool_choice": "string",
              },
              tools=[{
                  "tool_id": "string"
              }, {
                  "tool_id": "string"
              }, {
                  "tool_id": "string"
              }],
          )

    @parametrize
    def test_method_delete(self, client: PromptFoundry) -> None:
        prompt = client.prompts.delete(
            "1212121",
        )
        assert_matches_type(PromptDeleteResponse, prompt, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: PromptFoundry) -> None:

        response = client.prompts.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        prompt = response.parse()
        assert_matches_type(PromptDeleteResponse, prompt, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: PromptFoundry) -> None:
        with client.prompts.with_streaming_response.delete(
            "1212121",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            prompt = response.parse()
            assert_matches_type(PromptDeleteResponse, prompt, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: PromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          client.prompts.with_raw_response.delete(
              "",
          )
class TestAsyncPrompts:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.create(
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        )
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncPromptFoundry) -> None:

        response = await async_client.prompts.with_raw_response.create(
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        prompt = await response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.create(
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            prompt = await response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.retrieve(
            "string",
        )
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncPromptFoundry) -> None:

        response = await async_client.prompts.with_raw_response.retrieve(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        prompt = await response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.retrieve(
            "string",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            prompt = await response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
          await async_client.prompts.with_raw_response.retrieve(
              "",
          )

    @parametrize
    async def test_method_update(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.update(
            "string",
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        )
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncPromptFoundry) -> None:

        response = await async_client.prompts.with_raw_response.update(
            "string",
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        prompt = await response.parse()
        assert_matches_type(PromptConfiguration, prompt, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.update(
            "string",
            messages=[{
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
            name="string",
            parameters={
                "model_name": "string",
                "response_format": "TEXT",
                "temperature": 0,
                "top_p": 0,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "max_tokens": 0,
                "seed": 0,
                "tool_choice": "string",
            },
            tools=[{
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }, {
                "tool_id": "string"
            }],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            prompt = await response.parse()
            assert_matches_type(PromptConfiguration, prompt, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prompt_id` but received ''"):
          await async_client.prompts.with_raw_response.update(
              "",
              messages=[{
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
              name="string",
              parameters={
                  "model_name": "string",
                  "response_format": "TEXT",
                  "temperature": 0,
                  "top_p": 0,
                  "frequency_penalty": 0,
                  "presence_penalty": 0,
                  "max_tokens": 0,
                  "seed": 0,
                  "tool_choice": "string",
              },
              tools=[{
                  "tool_id": "string"
              }, {
                  "tool_id": "string"
              }, {
                  "tool_id": "string"
              }],
          )

    @parametrize
    async def test_method_delete(self, async_client: AsyncPromptFoundry) -> None:
        prompt = await async_client.prompts.delete(
            "1212121",
        )
        assert_matches_type(PromptDeleteResponse, prompt, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncPromptFoundry) -> None:

        response = await async_client.prompts.with_raw_response.delete(
            "1212121",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        prompt = await response.parse()
        assert_matches_type(PromptDeleteResponse, prompt, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncPromptFoundry) -> None:
        async with async_client.prompts.with_streaming_response.delete(
            "1212121",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            prompt = await response.parse()
            assert_matches_type(PromptDeleteResponse, prompt, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncPromptFoundry) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
          await async_client.prompts.with_raw_response.delete(
              "",
          )