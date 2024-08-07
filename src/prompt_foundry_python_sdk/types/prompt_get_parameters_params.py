# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "PromptGetParametersParams",
    "AppendMessage",
    "AppendMessageContent",
    "AppendMessageContentTextContentBlock",
    "AppendMessageContentImageBase64ContentBlock",
    "AppendMessageContentToolCallContentBlock",
    "AppendMessageContentToolCallContentBlockToolCall",
    "AppendMessageContentToolCallContentBlockToolCallFunction",
    "AppendMessageContentToolResultContentBlock",
    "OverrideMessage",
    "OverrideMessageContent",
    "OverrideMessageContentTextContentBlock",
    "OverrideMessageContentImageBase64ContentBlock",
    "OverrideMessageContentToolCallContentBlock",
    "OverrideMessageContentToolCallContentBlockToolCall",
    "OverrideMessageContentToolCallContentBlockToolCallFunction",
    "OverrideMessageContentToolResultContentBlock",
]


class PromptGetParametersParams(TypedDict, total=False):
    append_messages: Annotated[Iterable[AppendMessage], PropertyInfo(alias="appendMessages")]
    """
    Appended the the end of the configured prompt messages before running the
    prompt.
    """

    override_messages: Annotated[Iterable[OverrideMessage], PropertyInfo(alias="overrideMessages")]
    """Replaces the configured prompt messages when running the prompt."""

    user: str
    """
    A unique identifier representing your end-user, which can help monitor and
    detect abuse.
    """

    variables: Dict[str, Optional[str]]
    """The template variables added to the prompt when executing the prompt."""


class AppendMessageContentTextContentBlock(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["TEXT"]]


class AppendMessageContentImageBase64ContentBlock(TypedDict, total=False):
    image_base64: Required[Annotated[str, PropertyInfo(alias="imageBase64")]]

    media_type: Required[Annotated[str, PropertyInfo(alias="mediaType")]]

    type: Required[Literal["IMAGE_BASE64"]]


class AppendMessageContentToolCallContentBlockToolCallFunction(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class AppendMessageContentToolCallContentBlockToolCall(TypedDict, total=False):
    function: Required[AppendMessageContentToolCallContentBlockToolCallFunction]

    tool_call_id: Required[Annotated[str, PropertyInfo(alias="toolCallId")]]
    """TOOL_CALL_1"""

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class AppendMessageContentToolCallContentBlock(TypedDict, total=False):
    tool_call: Required[Annotated[AppendMessageContentToolCallContentBlockToolCall, PropertyInfo(alias="toolCall")]]

    type: Required[Literal["TOOL_CALL"]]


class AppendMessageContentToolResultContentBlock(TypedDict, total=False):
    result: Required[str]

    tool_call_id: Required[Annotated[str, PropertyInfo(alias="toolCallId")]]

    type: Required[Literal["TOOL_RESULT"]]


AppendMessageContent: TypeAlias = Union[
    AppendMessageContentTextContentBlock,
    AppendMessageContentImageBase64ContentBlock,
    AppendMessageContentToolCallContentBlock,
    AppendMessageContentToolResultContentBlock,
]


class AppendMessage(TypedDict, total=False):
    content: Required[Iterable[AppendMessageContent]]

    role: Required[Literal["assistant", "system", "tool", "user"]]


class OverrideMessageContentTextContentBlock(TypedDict, total=False):
    text: Required[str]

    type: Required[Literal["TEXT"]]


class OverrideMessageContentImageBase64ContentBlock(TypedDict, total=False):
    image_base64: Required[Annotated[str, PropertyInfo(alias="imageBase64")]]

    media_type: Required[Annotated[str, PropertyInfo(alias="mediaType")]]

    type: Required[Literal["IMAGE_BASE64"]]


class OverrideMessageContentToolCallContentBlockToolCallFunction(TypedDict, total=False):
    arguments: Required[str]
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: Required[str]
    """The name of the function to call."""


class OverrideMessageContentToolCallContentBlockToolCall(TypedDict, total=False):
    function: Required[OverrideMessageContentToolCallContentBlockToolCallFunction]

    tool_call_id: Required[Annotated[str, PropertyInfo(alias="toolCallId")]]
    """TOOL_CALL_1"""

    type: Required[Literal["function"]]
    """The type of the tool. Currently, only `function` is supported."""


class OverrideMessageContentToolCallContentBlock(TypedDict, total=False):
    tool_call: Required[Annotated[OverrideMessageContentToolCallContentBlockToolCall, PropertyInfo(alias="toolCall")]]

    type: Required[Literal["TOOL_CALL"]]


class OverrideMessageContentToolResultContentBlock(TypedDict, total=False):
    result: Required[str]

    tool_call_id: Required[Annotated[str, PropertyInfo(alias="toolCallId")]]

    type: Required[Literal["TOOL_RESULT"]]


OverrideMessageContent: TypeAlias = Union[
    OverrideMessageContentTextContentBlock,
    OverrideMessageContentImageBase64ContentBlock,
    OverrideMessageContentToolCallContentBlock,
    OverrideMessageContentToolResultContentBlock,
]


class OverrideMessage(TypedDict, total=False):
    content: Required[Iterable[OverrideMessageContent]]

    role: Required[Literal["assistant", "system", "tool", "user"]]
