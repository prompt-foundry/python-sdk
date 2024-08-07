# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "PromptConfiguration",
    "Message",
    "MessageContent",
    "MessageContentTextContentBlockSchema",
    "MessageContentImageBase64ContentBlock",
    "MessageContentToolCallContentBlock",
    "MessageContentToolCallContentBlockToolCall",
    "MessageContentToolCallContentBlockToolCallFunction",
    "MessageContentToolResultContentBlock",
    "Parameters",
    "Tool",
]


class MessageContentTextContentBlockSchema(BaseModel):
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
        MessageContentTextContentBlockSchema,
        MessageContentImageBase64ContentBlock,
        MessageContentToolCallContentBlock,
        MessageContentToolResultContentBlock,
    ],
    PropertyInfo(discriminator="type"),
]


class Message(BaseModel):
    content: List[MessageContent]

    role: Literal["assistant", "system", "tool", "user"]


class Parameters(BaseModel):
    frequency_penalty: float = FieldInfo(alias="frequencyPenalty")
    """Example: 0"""

    max_tokens: Optional[float] = FieldInfo(alias="maxTokens", default=None)
    """Example: 100"""

    api_model_name: str = FieldInfo(alias="modelName")
    """Example: "gpt-3.5-turbo" """

    api_model_provider: Literal["ANTHROPIC", "OPENAI"] = FieldInfo(alias="modelProvider")
    """The provider of the provided model."""

    parallel_tool_calls: bool = FieldInfo(alias="parallelToolCalls")

    presence_penalty: float = FieldInfo(alias="presencePenalty")
    """Example: 0"""

    response_format: Literal["JSON", "TEXT"] = FieldInfo(alias="responseFormat")
    """Example: PromptResponseFormat.TEXT"""

    seed: Optional[float] = None
    """Example: 97946543"""

    stream: bool

    temperature: float
    """Example: 1"""

    tool_choice: Optional[str] = FieldInfo(alias="toolChoice", default=None)

    top_k: Optional[float] = FieldInfo(alias="topK", default=None)
    """Example: 50"""

    top_p: float = FieldInfo(alias="topP")
    """Example: 1"""


class Tool(BaseModel):
    id: str
    """The initial messages to be included with your call to the LLM API."""

    description: str
    """
    A description of what the tool does, used by the model to choose when and how to
    call the tool.
    """

    name: str
    """The name of the tool to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    parameters: Dict[str, Optional[object]]
    """The parameters the functions accepts, described as a JSON Schema object.

    This schema is designed to match the TypeScript Record<string, unknown>,
    allowing for any properties with values of any type.
    """


class PromptConfiguration(BaseModel):
    id: str
    """Example: "PROMPT_1" """

    messages: List[Message]
    """The configured messages WITHOUT variables replaced."""

    name: str
    """Example: "Check the weather" """

    parameters: Parameters

    tools: List[Tool]
