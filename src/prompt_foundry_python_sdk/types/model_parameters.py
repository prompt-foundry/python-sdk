# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ModelParameters",
    "Parameters",
    "ParametersOpenAICreateCompletionNonStreamingRequest",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessage",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestSystemMessage",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessage",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessage",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCall",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestToolMessage",
    "ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestFunctionMessage",
    "ParametersOpenAICreateCompletionNonStreamingRequestResponseFormat",
    "ParametersOpenAICreateCompletionNonStreamingRequestToolChoice",
    "ParametersOpenAICreateCompletionNonStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoice",
    "ParametersOpenAICreateCompletionNonStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoiceFunction",
    "ParametersOpenAICreateCompletionNonStreamingRequestTool",
    "ParametersOpenAICreateCompletionNonStreamingRequestToolFunction",
    "ParametersOpenAICreateCompletionStreamingRequest",
    "ParametersOpenAICreateCompletionStreamingRequestMessage",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestSystemMessage",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessage",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessage",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCall",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestToolMessage",
    "ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestFunctionMessage",
    "ParametersOpenAICreateCompletionStreamingRequestResponseFormat",
    "ParametersOpenAICreateCompletionStreamingRequestStreamOptions",
    "ParametersOpenAICreateCompletionStreamingRequestToolChoice",
    "ParametersOpenAICreateCompletionStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoice",
    "ParametersOpenAICreateCompletionStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoiceFunction",
    "ParametersOpenAICreateCompletionStreamingRequestTool",
    "ParametersOpenAICreateCompletionStreamingRequestToolFunction",
]


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestSystemMessage(BaseModel):
    content: str

    role: Literal["system"]

    name: Optional[str] = None


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText(
    BaseModel
):
    text: str

    type: Literal["text"]


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage(
    BaseModel
):
    image_url: ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL

    type: Literal["image_url"]


ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1 = Union[
    ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText,
    ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage,
]


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessage(BaseModel):
    content: Union[
        str,
        List[
            ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1
        ],
    ]

    role: Literal["user"]

    name: Optional[str] = None


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall(
    BaseModel
):
    arguments: str

    name: str


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction(
    BaseModel
):
    arguments: str

    name: str


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCall(
    BaseModel
):
    id: str

    function: ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction

    type: Literal["function"]


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessage(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[
        ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall
    ] = None

    name: Optional[str] = None

    tool_calls: Optional[
        List[
            ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCall
        ]
    ] = None


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestToolMessage(BaseModel):
    content: str

    role: Literal["tool"]

    tool_call_id: str


class ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestFunctionMessage(BaseModel):
    content: Optional[str] = None

    name: str

    role: Literal["function"]


ParametersOpenAICreateCompletionNonStreamingRequestMessage = Union[
    ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestSystemMessage,
    ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestUserMessage,
    ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessage,
    ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestToolMessage,
    ParametersOpenAICreateCompletionNonStreamingRequestMessageOpenAIChatCompletionRequestFunctionMessage,
]


class ParametersOpenAICreateCompletionNonStreamingRequestResponseFormat(BaseModel):
    type: Optional[Literal["text", "json_object"]] = None


class ParametersOpenAICreateCompletionNonStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoiceFunction(
    BaseModel
):
    name: str


class ParametersOpenAICreateCompletionNonStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoice(BaseModel):
    function: ParametersOpenAICreateCompletionNonStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoiceFunction

    type: Literal["function"]


ParametersOpenAICreateCompletionNonStreamingRequestToolChoice = Union[
    Literal["none", "auto", "required"],
    ParametersOpenAICreateCompletionNonStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoice,
]


class ParametersOpenAICreateCompletionNonStreamingRequestToolFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[Dict[str, Optional[object]]] = None


class ParametersOpenAICreateCompletionNonStreamingRequestTool(BaseModel):
    function: ParametersOpenAICreateCompletionNonStreamingRequestToolFunction

    type: Literal["function"]


class ParametersOpenAICreateCompletionNonStreamingRequest(BaseModel):
    messages: List[ParametersOpenAICreateCompletionNonStreamingRequestMessage]

    model: str

    frequency_penalty: Optional[float] = None

    logit_bias: Optional[Dict[str, int]] = None

    logprobs: Optional[bool] = None

    max_tokens: Optional[int] = None

    n: Optional[int] = None

    parallel_tool_calls: Optional[bool] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[ParametersOpenAICreateCompletionNonStreamingRequestResponseFormat] = None

    seed: Optional[int] = None

    stop: Union[str, List[str], None] = None

    stream: Optional[Literal[False]] = None

    stream_options: Optional[object] = None

    temperature: Optional[float] = None

    tool_choice: Optional[ParametersOpenAICreateCompletionNonStreamingRequestToolChoice] = None

    tools: Optional[List[ParametersOpenAICreateCompletionNonStreamingRequestTool]] = None

    top_logprobs: Optional[int] = None

    top_p: Optional[float] = None

    user: Optional[str] = None


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestSystemMessage(BaseModel):
    content: str

    role: Literal["system"]

    name: Optional[str] = None


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText(
    BaseModel
):
    text: str

    type: Literal["text"]


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage(
    BaseModel
):
    image_url: ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL

    type: Literal["image_url"]


ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1 = Union[
    ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText,
    ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage,
]


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessage(BaseModel):
    content: Union[
        str,
        List[
            ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1
        ],
    ]

    role: Literal["user"]

    name: Optional[str] = None


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall(
    BaseModel
):
    arguments: str

    name: str


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction(
    BaseModel
):
    arguments: str

    name: str


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCall(
    BaseModel
):
    id: str

    function: ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction

    type: Literal["function"]


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessage(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[
        ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall
    ] = None

    name: Optional[str] = None

    tool_calls: Optional[
        List[ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessageToolCall]
    ] = None


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestToolMessage(BaseModel):
    content: str

    role: Literal["tool"]

    tool_call_id: str


class ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestFunctionMessage(BaseModel):
    content: Optional[str] = None

    name: str

    role: Literal["function"]


ParametersOpenAICreateCompletionStreamingRequestMessage = Union[
    ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestSystemMessage,
    ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestUserMessage,
    ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestAssistantMessage,
    ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestToolMessage,
    ParametersOpenAICreateCompletionStreamingRequestMessageOpenAIChatCompletionRequestFunctionMessage,
]


class ParametersOpenAICreateCompletionStreamingRequestResponseFormat(BaseModel):
    type: Optional[Literal["text", "json_object"]] = None


class ParametersOpenAICreateCompletionStreamingRequestStreamOptions(BaseModel):
    include_usage: bool


class ParametersOpenAICreateCompletionStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoiceFunction(BaseModel):
    name: str


class ParametersOpenAICreateCompletionStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoice(BaseModel):
    function: ParametersOpenAICreateCompletionStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoiceFunction

    type: Literal["function"]


ParametersOpenAICreateCompletionStreamingRequestToolChoice = Union[
    Literal["none", "auto", "required"],
    ParametersOpenAICreateCompletionStreamingRequestToolChoiceOpenAIChatCompletionNamedToolChoice,
]


class ParametersOpenAICreateCompletionStreamingRequestToolFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[Dict[str, Optional[object]]] = None


class ParametersOpenAICreateCompletionStreamingRequestTool(BaseModel):
    function: ParametersOpenAICreateCompletionStreamingRequestToolFunction

    type: Literal["function"]


class ParametersOpenAICreateCompletionStreamingRequest(BaseModel):
    messages: List[ParametersOpenAICreateCompletionStreamingRequestMessage]

    model: str

    stream: Literal[True]

    frequency_penalty: Optional[float] = None

    logit_bias: Optional[Dict[str, int]] = None

    logprobs: Optional[bool] = None

    max_tokens: Optional[int] = None

    n: Optional[int] = None

    parallel_tool_calls: Optional[bool] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[ParametersOpenAICreateCompletionStreamingRequestResponseFormat] = None

    seed: Optional[int] = None

    stop: Union[str, List[str], None] = None

    stream_options: Optional[ParametersOpenAICreateCompletionStreamingRequestStreamOptions] = None

    temperature: Optional[float] = None

    tool_choice: Optional[ParametersOpenAICreateCompletionStreamingRequestToolChoice] = None

    tools: Optional[List[ParametersOpenAICreateCompletionStreamingRequestTool]] = None

    top_logprobs: Optional[int] = None

    top_p: Optional[float] = None

    user: Optional[str] = None


Parameters = Union[
    ParametersOpenAICreateCompletionNonStreamingRequest, ParametersOpenAICreateCompletionStreamingRequest
]


class ModelParameters(BaseModel):
    name: str

    parameters: Parameters

    provider: Literal["openai"]
