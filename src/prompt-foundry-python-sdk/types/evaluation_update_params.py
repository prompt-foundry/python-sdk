# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required, Literal

from typing import Iterable, Dict, Optional

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["EvaluationUpdateParams", "AppendedMessage", "AppendedMessageToolCall", "AppendedMessageToolCallFunction"]


class EvaluationUpdateParams(TypedDict, total=False):
    appended_messages: Required[Annotated[Iterable[AppendedMessage], PropertyInfo(alias="appendedMessages")]]
    """The messages to append to the completion messages when running the evaluation."""

    prompt_id: Required[Annotated[str, PropertyInfo(alias="promptId")]]

    variables: Required[Dict[str, Optional[object]]]
    """The variables to in the prompt when evaluating the prompt."""


class AppendedMessageToolCallFunction(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class AppendedMessageToolCall(TypedDict, total=False):
    function: Required[AppendedMessageToolCallFunction]

    tool_call_id: Required[Annotated[str, PropertyInfo(alias="toolCallId")]]
    """TOOL_CALL_1"""

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class AppendedMessage(TypedDict, total=False):
    content: Required[Optional[str]]
    """Example: "Hello, {{city}}!" """

    role: Required[Literal["USER", "ASSISTANT", "SYSTEM", "TOOL"]]

    tool_call_id: Required[Annotated[Optional[str], PropertyInfo(alias="toolCallId")]]

    tool_calls: Required[Annotated[Optional[Iterable[AppendedMessageToolCall]], PropertyInfo(alias="toolCalls")]]