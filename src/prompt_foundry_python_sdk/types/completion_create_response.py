# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "CompletionCreateResponse",
    "Message",
    "MessageContent",
    "MessageContentTextContentBlock",
    "MessageContentImageBase64ContentBlock",
    "MessageContentToolCallContentBlock",
    "MessageContentToolCallContentBlockToolCall",
    "MessageContentToolCallContentBlockToolCallFunction",
    "MessageContentToolResultContentBlock",
    "Stats",
]


class MessageContentTextContentBlock(BaseModel):
    text: str

    type: Literal["TEXT"]


class MessageContentImageBase64ContentBlock(BaseModel):
    image_base64: str = FieldInfo(alias="imageBase64")

    media_type: str = FieldInfo(alias="mediaType")

    type: Literal["IMAGE_BASE64"]


class MessageContentToolCallContentBlockToolCallFunction(BaseModel):
    arguments: str
    """
    The arguments to call the function with, as generated by the model in JSON
    format. Note that the model does not always generate valid JSON, and may
    hallucinate parameters not defined by your function schema. Validate the
    arguments in your code before calling your function.
    """

    name: str
    """The name of the function to call."""


class MessageContentToolCallContentBlockToolCall(BaseModel):
    function: MessageContentToolCallContentBlockToolCallFunction

    tool_call_id: str = FieldInfo(alias="toolCallId")
    """TOOL_CALL_1"""

    type: Literal["function"]
    """The type of the tool. Currently, only `function` is supported."""


class MessageContentToolCallContentBlock(BaseModel):
    tool_call: MessageContentToolCallContentBlockToolCall = FieldInfo(alias="toolCall")

    type: Literal["TOOL_CALL"]


class MessageContentToolResultContentBlock(BaseModel):
    result: str

    tool_call_id: str = FieldInfo(alias="toolCallId")

    type: Literal["TOOL_RESULT"]


MessageContent: TypeAlias = Annotated[
    Union[
        MessageContentTextContentBlock,
        MessageContentImageBase64ContentBlock,
        MessageContentToolCallContentBlock,
        MessageContentToolResultContentBlock,
    ],
    PropertyInfo(discriminator="type"),
]


class Message(BaseModel):
    content: List[MessageContent]

    role: Literal["assistant", "system", "tool", "user"]


class Stats(BaseModel):
    cost: float
    """The cost of generating the completion."""

    input_token_count: float = FieldInfo(alias="inputTokenCount")
    """The number of tokens in the input prompt."""

    latency: float
    """The time in milliseconds it took to generate the completion."""

    output_token_count: float = FieldInfo(alias="outputTokenCount")
    """The number of tokens in the output completion."""


class CompletionCreateResponse(BaseModel):
    message: Message
    """The completion message generated by the model."""

    name: str

    provider: Literal["ANTHROPIC", "OPENAI"]
    """The LLM model provider."""

    stats: Stats