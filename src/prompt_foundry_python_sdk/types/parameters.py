# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "Parameters",
    "AnthropicModelParameters",
    "AnthropicModelParametersParameters",
    "AnthropicModelParametersParametersMessage",
    "AnthropicModelParametersParametersMessageContentUnionMember1",
    "AnthropicModelParametersParametersMessageContentUnionMember1TextBlockParam",
    "AnthropicModelParametersParametersMessageContentUnionMember1ImageBlockParam",
    "AnthropicModelParametersParametersMessageContentUnionMember1ImageBlockParamSource",
    "AnthropicModelParametersParametersMessageContentUnionMember1ToolUseBlockParam",
    "AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParam",
    "AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1",
    "AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1TextBlockParam",
    "AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParam",
    "AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParamSource",
    "AnthropicModelParametersParametersMetadata",
    "AnthropicModelParametersParametersToolChoice",
    "AnthropicModelParametersParametersToolChoiceMessageCreateParamsToolChoiceAuto",
    "AnthropicModelParametersParametersToolChoiceMessageCreateParamsToolChoiceAny",
    "AnthropicModelParametersParametersToolChoiceMessageCreateParamsToolChoiceTool",
    "AnthropicModelParametersParametersTool",
    "AnthropicModelParametersParametersToolInputSchema",
    "OpenAIModelParameters",
    "OpenAIModelParametersParameters",
    "OpenAIModelParametersParametersMessage",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestSystemMessage",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessage",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessage",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestToolMessage",
    "OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestFunctionMessage",
    "OpenAIModelParametersParametersResponseFormat",
    "OpenAIModelParametersParametersStreamOptions",
    "OpenAIModelParametersParametersToolChoice",
    "OpenAIModelParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoice",
    "OpenAIModelParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction",
    "OpenAIModelParametersParametersTool",
    "OpenAIModelParametersParametersToolFunction",
]


class AnthropicModelParametersParametersMessageContentUnionMember1TextBlockParam(BaseModel):
    text: str

    type: Literal["text"]


class AnthropicModelParametersParametersMessageContentUnionMember1ImageBlockParamSource(BaseModel):
    data: str

    media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

    type: Literal["base64"]


class AnthropicModelParametersParametersMessageContentUnionMember1ImageBlockParam(BaseModel):
    source: AnthropicModelParametersParametersMessageContentUnionMember1ImageBlockParamSource

    type: Literal["image"]


class AnthropicModelParametersParametersMessageContentUnionMember1ToolUseBlockParam(BaseModel):
    id: str

    input: Dict[str, str]

    name: str

    type: Literal["tool_use"]


class AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1TextBlockParam(
    BaseModel
):
    text: str

    type: Literal["text"]


class AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParamSource(
    BaseModel
):
    data: str

    media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

    type: Literal["base64"]


class AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParam(
    BaseModel
):
    source: AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParamSource

    type: Literal["image"]


AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1: TypeAlias = Union[
    AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1TextBlockParam,
    AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParam,
]


class AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParam(BaseModel):
    tool_use_id: str

    type: Literal["tool_result"]

    content: Union[
        str,
        List[AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1],
        None,
    ] = None

    is_error: Optional[bool] = None


AnthropicModelParametersParametersMessageContentUnionMember1: TypeAlias = Union[
    AnthropicModelParametersParametersMessageContentUnionMember1TextBlockParam,
    AnthropicModelParametersParametersMessageContentUnionMember1ImageBlockParam,
    AnthropicModelParametersParametersMessageContentUnionMember1ToolUseBlockParam,
    AnthropicModelParametersParametersMessageContentUnionMember1ToolResultBlockParam,
]


class AnthropicModelParametersParametersMessage(BaseModel):
    content: Union[str, List[AnthropicModelParametersParametersMessageContentUnionMember1]]

    role: Literal["user", "assistant"]


class AnthropicModelParametersParametersMetadata(BaseModel):
    user_id: Optional[str] = None


class AnthropicModelParametersParametersToolChoiceMessageCreateParamsToolChoiceAuto(BaseModel):
    type: Literal["auto"]


class AnthropicModelParametersParametersToolChoiceMessageCreateParamsToolChoiceAny(BaseModel):
    type: Literal["any"]


class AnthropicModelParametersParametersToolChoiceMessageCreateParamsToolChoiceTool(BaseModel):
    name: str

    type: Literal["tool"]


AnthropicModelParametersParametersToolChoice: TypeAlias = Union[
    AnthropicModelParametersParametersToolChoiceMessageCreateParamsToolChoiceAuto,
    AnthropicModelParametersParametersToolChoiceMessageCreateParamsToolChoiceAny,
    AnthropicModelParametersParametersToolChoiceMessageCreateParamsToolChoiceTool,
]


class AnthropicModelParametersParametersToolInputSchema(BaseModel):
    type: Literal["object"]

    properties: Optional[object] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class AnthropicModelParametersParametersTool(BaseModel):
    input_schema: AnthropicModelParametersParametersToolInputSchema

    name: str

    description: Optional[str] = None


class AnthropicModelParametersParameters(BaseModel):
    max_tokens: float

    messages: List[AnthropicModelParametersParametersMessage]

    model: Union[
        str,
        Literal[
            "claude-3-5-sonnet-20240620",
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
        ],
    ]

    metadata: Optional[AnthropicModelParametersParametersMetadata] = None

    stop_sequences: Optional[List[str]] = None

    stream: Optional[bool] = None

    system: Optional[str] = None

    temperature: Optional[float] = None

    tool_choice: Optional[AnthropicModelParametersParametersToolChoice] = None

    tools: Optional[List[AnthropicModelParametersParametersTool]] = None

    top_k: Optional[float] = None

    top_p: Optional[float] = None


class AnthropicModelParameters(BaseModel):
    name: str

    parameters: AnthropicModelParametersParameters

    provider: Literal["anthropic"]


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestSystemMessage(BaseModel):
    content: str

    role: Literal["system"]

    name: Optional[str] = None


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText(
    BaseModel
):
    text: str

    type: Literal["text"]


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage(
    BaseModel
):
    image_url: OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL

    type: Literal["image_url"]


OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1: TypeAlias = Union[
    OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText,
    OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage,
]


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessage(BaseModel):
    content: Union[
        str, List[OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1]
    ]

    role: Literal["user"]

    name: Optional[str] = None


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall(BaseModel):
    arguments: str

    name: str


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction(BaseModel):
    arguments: str

    name: str


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall(BaseModel):
    id: str

    function: OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction

    type: Literal["function"]


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessage(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[
        OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall
    ] = None

    name: Optional[str] = None

    tool_calls: Optional[
        List[OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall]
    ] = None


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestToolMessage(BaseModel):
    content: str

    role: Literal["tool"]

    tool_call_id: str


class OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestFunctionMessage(BaseModel):
    content: Optional[str] = None

    name: str

    role: Literal["function"]


OpenAIModelParametersParametersMessage: TypeAlias = Union[
    OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestSystemMessage,
    OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestUserMessage,
    OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestAssistantMessage,
    OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestToolMessage,
    OpenAIModelParametersParametersMessageOpenAIChatCompletionRequestFunctionMessage,
]


class OpenAIModelParametersParametersResponseFormat(BaseModel):
    type: Optional[Literal["text", "json_object"]] = None


class OpenAIModelParametersParametersStreamOptions(BaseModel):
    include_usage: bool


class OpenAIModelParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction(BaseModel):
    name: str


class OpenAIModelParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoice(BaseModel):
    function: OpenAIModelParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction

    type: Literal["function"]


OpenAIModelParametersParametersToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"], OpenAIModelParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoice
]


class OpenAIModelParametersParametersToolFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[Dict[str, Optional[object]]] = None


class OpenAIModelParametersParametersTool(BaseModel):
    function: OpenAIModelParametersParametersToolFunction

    type: Literal["function"]


class OpenAIModelParametersParameters(BaseModel):
    messages: List[OpenAIModelParametersParametersMessage]

    model: str

    frequency_penalty: Optional[float] = None

    logit_bias: Optional[Dict[str, int]] = None

    logprobs: Optional[bool] = None

    max_tokens: Optional[int] = None

    n: Optional[int] = None

    parallel_tool_calls: Optional[bool] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[OpenAIModelParametersParametersResponseFormat] = None

    seed: Optional[int] = None

    stop: Union[str, List[str], None] = None

    stream: Optional[bool] = None

    stream_options: Optional[OpenAIModelParametersParametersStreamOptions] = None

    temperature: Optional[float] = None

    tool_choice: Optional[OpenAIModelParametersParametersToolChoice] = None

    tools: Optional[List[OpenAIModelParametersParametersTool]] = None

    top_logprobs: Optional[int] = None

    top_p: Optional[float] = None

    user: Optional[str] = None


class OpenAIModelParameters(BaseModel):
    name: str

    parameters: OpenAIModelParametersParameters

    provider: Literal["openai"]


Parameters: TypeAlias = Union[AnthropicModelParameters, OpenAIModelParameters]
