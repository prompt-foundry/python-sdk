# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "PromptGetParametersResponse",
    "AnthropicModelNonStreamingParameters",
    "AnthropicModelNonStreamingParametersParameters",
    "AnthropicModelNonStreamingParametersParametersMessage",
    "AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1",
    "AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1TextBlockParam",
    "AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ImageBlockParam",
    "AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ImageBlockParamSource",
    "AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolUseBlockParam",
    "AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParam",
    "AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1",
    "AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1TextBlockParam",
    "AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParam",
    "AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParamSource",
    "AnthropicModelNonStreamingParametersParametersMetadata",
    "AnthropicModelNonStreamingParametersParametersToolChoice",
    "AnthropicModelNonStreamingParametersParametersToolChoiceMessageCreateParamsToolChoiceAuto",
    "AnthropicModelNonStreamingParametersParametersToolChoiceMessageCreateParamsToolChoiceAny",
    "AnthropicModelNonStreamingParametersParametersToolChoiceMessageCreateParamsToolChoiceTool",
    "AnthropicModelNonStreamingParametersParametersTool",
    "AnthropicModelNonStreamingParametersParametersToolInputSchema",
    "OpenAIModelNonStreamingParameters",
    "OpenAIModelNonStreamingParametersParameters",
    "OpenAIModelNonStreamingParametersParametersMessage",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestSystemMessage",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessage",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessage",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestToolMessage",
    "OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestFunctionMessage",
    "OpenAIModelNonStreamingParametersParametersResponseFormat",
    "OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatText",
    "OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatJsonObject",
    "OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatJsonSchema",
    "OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema",
    "OpenAIModelNonStreamingParametersParametersToolChoice",
    "OpenAIModelNonStreamingParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoice",
    "OpenAIModelNonStreamingParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction",
    "OpenAIModelNonStreamingParametersParametersTool",
    "OpenAIModelNonStreamingParametersParametersToolFunction",
]


class AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1TextBlockParam(BaseModel):
    text: str

    type: Literal["text"]


class AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ImageBlockParamSource(BaseModel):
    data: str

    media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

    type: Literal["base64"]


class AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ImageBlockParam(BaseModel):
    source: AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ImageBlockParamSource

    type: Literal["image"]


class AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolUseBlockParam(BaseModel):
    id: str

    input: Dict[str, str]

    name: str

    type: Literal["tool_use"]


class AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1TextBlockParam(
    BaseModel
):
    text: str

    type: Literal["text"]


class AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParamSource(
    BaseModel
):
    data: str

    media_type: Literal["image/jpeg", "image/png", "image/gif", "image/webp"]

    type: Literal["base64"]


class AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParam(
    BaseModel
):
    source: AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParamSource

    type: Literal["image"]


AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1: TypeAlias = Union[
    AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1TextBlockParam,
    AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1ImageBlockParam,
]


class AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParam(BaseModel):
    tool_use_id: str

    type: Literal["tool_result"]

    content: Union[
        str,
        List[
            AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParamContentUnionMember1
        ],
        None,
    ] = None

    is_error: Optional[bool] = None


AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1: TypeAlias = Union[
    AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1TextBlockParam,
    AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ImageBlockParam,
    AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolUseBlockParam,
    AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1ToolResultBlockParam,
]


class AnthropicModelNonStreamingParametersParametersMessage(BaseModel):
    content: Union[str, List[AnthropicModelNonStreamingParametersParametersMessageContentUnionMember1]]

    role: Literal["user", "assistant"]


class AnthropicModelNonStreamingParametersParametersMetadata(BaseModel):
    user_id: Optional[str] = None


class AnthropicModelNonStreamingParametersParametersToolChoiceMessageCreateParamsToolChoiceAuto(BaseModel):
    type: Literal["auto"]


class AnthropicModelNonStreamingParametersParametersToolChoiceMessageCreateParamsToolChoiceAny(BaseModel):
    type: Literal["any"]


class AnthropicModelNonStreamingParametersParametersToolChoiceMessageCreateParamsToolChoiceTool(BaseModel):
    name: str

    type: Literal["tool"]


AnthropicModelNonStreamingParametersParametersToolChoice: TypeAlias = Union[
    AnthropicModelNonStreamingParametersParametersToolChoiceMessageCreateParamsToolChoiceAuto,
    AnthropicModelNonStreamingParametersParametersToolChoiceMessageCreateParamsToolChoiceAny,
    AnthropicModelNonStreamingParametersParametersToolChoiceMessageCreateParamsToolChoiceTool,
]


class AnthropicModelNonStreamingParametersParametersToolInputSchema(BaseModel):
    type: Literal["object"]

    properties: Optional[object] = None

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> Optional[object]: ...


class AnthropicModelNonStreamingParametersParametersTool(BaseModel):
    input_schema: AnthropicModelNonStreamingParametersParametersToolInputSchema

    name: str

    description: Optional[str] = None


class AnthropicModelNonStreamingParametersParameters(BaseModel):
    max_tokens: float

    messages: List[AnthropicModelNonStreamingParametersParametersMessage]

    model: Union[
        str,
        Literal[
            "claude-3-5-sonnet-20240620",
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
        ],
    ]

    stream: Literal[False]

    metadata: Optional[AnthropicModelNonStreamingParametersParametersMetadata] = None

    stop_sequences: Optional[List[str]] = None

    system: Optional[str] = None

    temperature: Optional[float] = None

    tool_choice: Optional[AnthropicModelNonStreamingParametersParametersToolChoice] = None

    tools: Optional[List[AnthropicModelNonStreamingParametersParametersTool]] = None

    top_k: Optional[float] = None

    top_p: Optional[float] = None


class AnthropicModelNonStreamingParameters(BaseModel):
    name: str

    parameters: AnthropicModelNonStreamingParametersParameters

    provider: Literal["anthropic"]


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestSystemMessage(BaseModel):
    content: str

    role: Literal["system"]

    name: Optional[str] = None


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText(
    BaseModel
):
    text: str

    type: Literal["text"]


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage(
    BaseModel
):
    image_url: OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL

    type: Literal["image_url"]


OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1: TypeAlias = Union[
    OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText,
    OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage,
]


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessage(BaseModel):
    content: Union[
        str,
        List[
            OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1
        ],
    ]

    role: Literal["user"]

    name: Optional[str] = None


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall(
    BaseModel
):
    arguments: str

    name: str


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction(
    BaseModel
):
    arguments: str

    name: str


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall(BaseModel):
    id: str

    function: (
        OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction
    )

    type: Literal["function"]


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessage(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[
        OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall
    ] = None

    name: Optional[str] = None

    tool_calls: Optional[
        List[OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall]
    ] = None


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestToolMessage(BaseModel):
    content: str

    role: Literal["tool"]

    tool_call_id: str


class OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestFunctionMessage(BaseModel):
    content: Optional[str] = None

    name: str

    role: Literal["function"]


OpenAIModelNonStreamingParametersParametersMessage: TypeAlias = Union[
    OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestSystemMessage,
    OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestUserMessage,
    OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestAssistantMessage,
    OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestToolMessage,
    OpenAIModelNonStreamingParametersParametersMessageOpenAIChatCompletionRequestFunctionMessage,
]


class OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatText(BaseModel):
    type: Literal["text"]


class OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatJsonObject(BaseModel):
    type: Literal["json_object"]


class OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema(BaseModel):
    name: str

    strict: Optional[bool] = None

    description: Optional[str] = None

    schema_: Optional[Dict[str, Optional[object]]] = FieldInfo(alias="schema", default=None)


class OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatJsonSchema(BaseModel):
    json_schema: OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatJsonSchemaJsonSchema

    type: Literal["json_schema"]


OpenAIModelNonStreamingParametersParametersResponseFormat: TypeAlias = Annotated[
    Union[
        OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatText,
        OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatJsonObject,
        OpenAIModelNonStreamingParametersParametersResponseFormatOpenAIResponseFormatJsonSchema,
    ],
    PropertyInfo(discriminator="type"),
]


class OpenAIModelNonStreamingParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction(BaseModel):
    name: str


class OpenAIModelNonStreamingParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoice(BaseModel):
    function: OpenAIModelNonStreamingParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction

    type: Literal["function"]


OpenAIModelNonStreamingParametersParametersToolChoice: TypeAlias = Union[
    Literal["none", "auto", "required"],
    OpenAIModelNonStreamingParametersParametersToolChoiceOpenAIChatCompletionNamedToolChoice,
]


class OpenAIModelNonStreamingParametersParametersToolFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[Dict[str, Optional[object]]] = None


class OpenAIModelNonStreamingParametersParametersTool(BaseModel):
    function: OpenAIModelNonStreamingParametersParametersToolFunction

    type: Literal["function"]


class OpenAIModelNonStreamingParametersParameters(BaseModel):
    messages: List[OpenAIModelNonStreamingParametersParametersMessage]

    model: str

    response_format: OpenAIModelNonStreamingParametersParametersResponseFormat

    stream: Literal[False]

    frequency_penalty: Optional[float] = None

    logit_bias: Optional[Dict[str, int]] = None

    logprobs: Optional[bool] = None

    max_tokens: Optional[int] = None

    n: Optional[int] = None

    parallel_tool_calls: Optional[bool] = None

    presence_penalty: Optional[float] = None

    seed: Optional[int] = None

    stop: Union[str, List[str], None] = None

    temperature: Optional[float] = None

    tool_choice: Optional[OpenAIModelNonStreamingParametersParametersToolChoice] = None

    tools: Optional[List[OpenAIModelNonStreamingParametersParametersTool]] = None

    top_logprobs: Optional[int] = None

    top_p: Optional[float] = None

    user: Optional[str] = None


class OpenAIModelNonStreamingParameters(BaseModel):
    name: str

    parameters: OpenAIModelNonStreamingParametersParameters

    provider: Literal["openai"]


PromptGetParametersResponse: TypeAlias = Union[AnthropicModelNonStreamingParameters, OpenAIModelNonStreamingParameters]
