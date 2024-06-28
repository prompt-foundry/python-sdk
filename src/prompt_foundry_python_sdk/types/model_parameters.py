# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ModelParameters",
    "UnionMember0",
    "UnionMember0Parameters",
    "UnionMember0ParametersMessage",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestSystemMessage",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessage",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessage",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestToolMessage",
    "UnionMember0ParametersMessageOpenAIChatCompletionRequestFunctionMessage",
    "UnionMember0ParametersResponseFormat",
    "UnionMember0ParametersStreamOptions",
    "UnionMember0ParametersToolChoice",
    "UnionMember0ParametersToolChoiceOpenAIChatCompletionNamedToolChoice",
    "UnionMember0ParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction",
    "UnionMember0ParametersTool",
    "UnionMember0ParametersToolFunction",
    "UnionMember1",
    "UnionMember1Parameters",
    "UnionMember1ParametersMessage",
    "UnionMember1ParametersMessageContentUnionMember1",
    "UnionMember1ParametersMessageContentUnionMember1UnionMember0",
    "UnionMember1ParametersMessageContentUnionMember1UnionMember1",
    "UnionMember1ParametersMessageContentUnionMember1UnionMember1Source",
    "UnionMember1ParametersMessageContentUnionMember1UnionMember2",
    "UnionMember1ParametersMessageContentUnionMember1UnionMember3",
    "UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1",
    "UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1UnionMember0",
    "UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1UnionMember1",
    "UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1UnionMember1Source",
    "UnionMember1ParametersMetadata",
    "UnionMember1ParametersToolChoice",
    "UnionMember1ParametersToolChoiceType",
    "UnionMember1ParametersToolChoiceUnionMember2",
    "UnionMember1ParametersTool",
    "UnionMember1ParametersToolInputSchema",
]


class UnionMember0ParametersMessageOpenAIChatCompletionRequestSystemMessage(BaseModel):
    content: str

    role: Literal["system"]

    name: Optional[str] = None


class UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText(
    BaseModel
):
    text: str

    type: Literal["text"]


class UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage(
    BaseModel
):
    image_url: UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL

    type: Literal["image_url"]


UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1 = Union[
    UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText,
    UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage,
]


class UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessage(BaseModel):
    content: Union[str, List[UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1]]

    role: Literal["user"]

    name: Optional[str] = None


class UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall(BaseModel):
    arguments: str

    name: str


class UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction(BaseModel):
    arguments: str

    name: str


class UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall(BaseModel):
    id: str

    function: UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction

    type: Literal["function"]


class UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessage(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall] = None

    name: Optional[str] = None

    tool_calls: Optional[List[UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall]] = None


class UnionMember0ParametersMessageOpenAIChatCompletionRequestToolMessage(BaseModel):
    content: str

    role: Literal["tool"]

    tool_call_id: str


class UnionMember0ParametersMessageOpenAIChatCompletionRequestFunctionMessage(BaseModel):
    content: Optional[str] = None

    name: str

    role: Literal["function"]


UnionMember0ParametersMessage = Union[
    UnionMember0ParametersMessageOpenAIChatCompletionRequestSystemMessage,
    UnionMember0ParametersMessageOpenAIChatCompletionRequestUserMessage,
    UnionMember0ParametersMessageOpenAIChatCompletionRequestAssistantMessage,
    UnionMember0ParametersMessageOpenAIChatCompletionRequestToolMessage,
    UnionMember0ParametersMessageOpenAIChatCompletionRequestFunctionMessage,
]


class UnionMember0ParametersResponseFormat(BaseModel):
    type: Optional[Literal["text", "json_object"]] = None


class UnionMember0ParametersStreamOptions(BaseModel):
    include_usage: bool


class UnionMember0ParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction(BaseModel):
    name: str


class UnionMember0ParametersToolChoiceOpenAIChatCompletionNamedToolChoice(BaseModel):
    function: UnionMember0ParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction

    type: Literal["function"]


UnionMember0ParametersToolChoice = Union[
    Literal["none", "auto", "required"], UnionMember0ParametersToolChoiceOpenAIChatCompletionNamedToolChoice
]


class UnionMember0ParametersToolFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[Dict[str, Optional[object]]] = None


class UnionMember0ParametersTool(BaseModel):
    function: UnionMember0ParametersToolFunction

    type: Literal["function"]


class UnionMember0Parameters(BaseModel):
    messages: List[UnionMember0ParametersMessage]

    model: str

    frequency_penalty: Optional[float] = None

    logit_bias: Optional[Dict[str, int]] = None

    logprobs: Optional[bool] = None

    max_tokens: Optional[int] = None

    n: Optional[int] = None

    parallel_tool_calls: Optional[bool] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[UnionMember0ParametersResponseFormat] = None

    seed: Optional[int] = None

    stop: Union[str, List[str], None] = None

    stream: Optional[bool] = None

    stream_options: Optional[UnionMember0ParametersStreamOptions] = None

    temperature: Optional[float] = None

    tool_choice: Optional[UnionMember0ParametersToolChoice] = None

    tools: Optional[List[UnionMember0ParametersTool]] = None

    top_logprobs: Optional[int] = None

    top_p: Optional[float] = None

    user: Optional[str] = None


class UnionMember0(BaseModel):
    name: str

    parameters: UnionMember0Parameters

    provider: Literal["openai"]


class UnionMember1ParametersMessageContentUnionMember1UnionMember0(BaseModel):
    text: str

    type: Literal["text"]


class UnionMember1ParametersMessageContentUnionMember1UnionMember1Source(BaseModel):
    data: str

    media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

    type: Literal["base64"]


class UnionMember1ParametersMessageContentUnionMember1UnionMember1(BaseModel):
    source: UnionMember1ParametersMessageContentUnionMember1UnionMember1Source

    type: Literal["image"]


class UnionMember1ParametersMessageContentUnionMember1UnionMember2(BaseModel):
    id: str

    input: Dict[str, str]

    name: str

    type: Literal["tool_use"]


class UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1UnionMember0(BaseModel):
    text: str

    type: Literal["text"]


class UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1UnionMember1Source(BaseModel):
    data: str

    media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

    type: Literal["base64"]


class UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1UnionMember1(BaseModel):
    source: UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1UnionMember1Source

    type: Literal["image"]


UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1 = Union[
    UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1UnionMember0,
    UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1UnionMember1,
]


class UnionMember1ParametersMessageContentUnionMember1UnionMember3(BaseModel):
    tool_use_id: str

    type: Literal["tool_result"]

    content: Union[
        str, List[UnionMember1ParametersMessageContentUnionMember1UnionMember3ContentUnionMember1], None
    ] = None

    is_error: Optional[bool] = None


UnionMember1ParametersMessageContentUnionMember1 = Union[
    UnionMember1ParametersMessageContentUnionMember1UnionMember0,
    UnionMember1ParametersMessageContentUnionMember1UnionMember1,
    UnionMember1ParametersMessageContentUnionMember1UnionMember2,
    UnionMember1ParametersMessageContentUnionMember1UnionMember3,
]


class UnionMember1ParametersMessage(BaseModel):
    content: Union[str, List[UnionMember1ParametersMessageContentUnionMember1]]

    role: Literal["user", "assistant"]


class UnionMember1ParametersMetadata(BaseModel):
    user_id: Optional[str] = None


class UnionMember1ParametersToolChoiceType(BaseModel):
    type: Literal["auto"]


class UnionMember1ParametersToolChoiceUnionMember2(BaseModel):
    name: str

    type: Literal["tool"]


UnionMember1ParametersToolChoice = Union[
    UnionMember1ParametersToolChoiceType,
    UnionMember1ParametersToolChoiceType,
    UnionMember1ParametersToolChoiceUnionMember2,
]


class UnionMember1ParametersToolInputSchema(BaseModel):
    type: Literal["object"]

    properties: Optional[object] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]:
            ...


class UnionMember1ParametersTool(BaseModel):
    input_schema: UnionMember1ParametersToolInputSchema

    name: str

    description: Optional[str] = None


class UnionMember1Parameters(BaseModel):
    max_tokens: float

    messages: List[UnionMember1ParametersMessage]

    model: Union[
        str,
        Literal[
            "claude-3-5-sonnet-20240620",
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
        ],
    ]

    metadata: Optional[UnionMember1ParametersMetadata] = None

    stop_sequences: Optional[List[str]] = None

    stream: Optional[bool] = None

    system: Optional[str] = None

    temperature: Optional[float] = None

    tool_choice: Optional[UnionMember1ParametersToolChoice] = None

    tools: Optional[List[UnionMember1ParametersTool]] = None

    top_k: Optional[float] = None

    top_p: Optional[float] = None


class UnionMember1(BaseModel):
    name: str

    parameters: UnionMember1Parameters

    provider: Literal["anthropic"]


ModelParameters = Union[UnionMember0, UnionMember1]
