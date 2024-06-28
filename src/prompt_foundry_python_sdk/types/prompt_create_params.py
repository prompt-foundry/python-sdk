# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PromptCreateParams", "Message", "MessageToolCall", "MessageToolCallFunction", "Parameters", "Tool"]


class PromptCreateParams(TypedDict, total=False):
    messages: Required[Iterable[Message]]

    name: Required[str]

    parameters: Required[Parameters]

    tools: Required[Iterable[Tool]]


class MessageToolCallFunction(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class MessageToolCall(TypedDict, total=False):
    function: Required[MessageToolCallFunction]

    tool_call_id: Required[Annotated[str, PropertyInfo(alias="toolCallId")]]
    """TOOL_CALL_1"""

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class Message(TypedDict, total=False):
    content: Required[Optional[str]]
    """Example: "Hello, {{city}}!" """

    role: Required[Literal["assistant", "system", "tool", "user"]]

    tool_call_id: Required[Annotated[Optional[str], PropertyInfo(alias="toolCallId")]]

    tool_calls: Required[Annotated[Optional[Iterable[MessageToolCall]], PropertyInfo(alias="toolCalls")]]


class Parameters(TypedDict, total=False):
    frequency_penalty: Required[Annotated[float, PropertyInfo(alias="frequencyPenalty")]]
    """Example: 0"""

    max_tokens: Required[Annotated[Optional[float], PropertyInfo(alias="maxTokens")]]
    """Example: 100"""

    model_name: Required[Annotated[str, PropertyInfo(alias="modelName")]]
    """Example: "gpt-3.5-turbo" """

    model_provider: Required[Annotated[Literal["ANTHROPIC", "OPENAI"], PropertyInfo(alias="modelProvider")]]
    """The provider of the provided model."""

    parallel_tool_calls: Required[Annotated[bool, PropertyInfo(alias="parallelToolCalls")]]

    presence_penalty: Required[Annotated[float, PropertyInfo(alias="presencePenalty")]]
    """Example: 0"""

    response_format: Required[Annotated[Literal["JSON", "TEXT"], PropertyInfo(alias="responseFormat")]]
    """Example: PromptResponseFormat.TEXT"""

    seed: Required[Optional[float]]
    """Example: 97946543"""

    stream: Required[bool]

    temperature: Required[float]
    """Example: 1"""

    tool_choice: Required[Annotated[Optional[str], PropertyInfo(alias="toolChoice")]]

    top_p: Required[Annotated[float, PropertyInfo(alias="topP")]]
    """Example: 1"""


class Tool(TypedDict, total=False):
    tool_id: Required[Annotated[str, PropertyInfo(alias="toolId")]]
