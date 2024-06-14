# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "ModelParameters",
    "Parameters",
    "ParametersMessage",
    "ParametersMessageOpenAIChatCompletionRequestSystemMessage",
    "ParametersMessageOpenAIChatCompletionRequestUserMessage",
    "ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1",
    "ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText",
    "ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage",
    "ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL",
    "ParametersMessageOpenAIChatCompletionRequestAssistantMessage",
    "ParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall",
    "ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall",
    "ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction",
    "ParametersMessageOpenAIChatCompletionRequestToolMessage",
    "ParametersMessageOpenAIChatCompletionRequestFunctionMessage",
    "ParametersResponseFormat",
    "ParametersStreamOptions",
    "ParametersToolChoice",
    "ParametersToolChoiceOpenAIChatCompletionNamedToolChoice",
    "ParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction",
    "ParametersTool",
    "ParametersToolFunction",
]


class ParametersMessageOpenAIChatCompletionRequestSystemMessage(BaseModel):
    content: str

    role: Literal["system"]

    name: Optional[str] = None


class ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText(
    BaseModel
):
    text: str

    type: Literal["text"]


class ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL(
    BaseModel
):
    url: str

    detail: Optional[Literal["auto", "low", "high"]] = None


class ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage(
    BaseModel
):
    image_url: ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImageImageURL

    type: Literal["image_url"]


ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1 = Union[
    ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartText,
    ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1OpenAIChatCompletionRequestMessageContentPartImage,
]


class ParametersMessageOpenAIChatCompletionRequestUserMessage(BaseModel):
    content: Union[str, List[ParametersMessageOpenAIChatCompletionRequestUserMessageContentUnionMember1]]

    role: Literal["user"]

    name: Optional[str] = None


class ParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall(BaseModel):
    arguments: str

    name: str


class ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction(BaseModel):
    arguments: str

    name: str


class ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall(BaseModel):
    id: str

    function: ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCallFunction

    type: Literal["function"]


class ParametersMessageOpenAIChatCompletionRequestAssistantMessage(BaseModel):
    role: Literal["assistant"]

    content: Optional[str] = None

    function_call: Optional[ParametersMessageOpenAIChatCompletionRequestAssistantMessageFunctionCall] = None

    name: Optional[str] = None

    tool_calls: Optional[List[ParametersMessageOpenAIChatCompletionRequestAssistantMessageToolCall]] = None


class ParametersMessageOpenAIChatCompletionRequestToolMessage(BaseModel):
    content: str

    role: Literal["tool"]

    tool_call_id: str


class ParametersMessageOpenAIChatCompletionRequestFunctionMessage(BaseModel):
    content: Optional[str] = None

    name: str

    role: Literal["function"]


ParametersMessage = Union[
    ParametersMessageOpenAIChatCompletionRequestSystemMessage,
    ParametersMessageOpenAIChatCompletionRequestUserMessage,
    ParametersMessageOpenAIChatCompletionRequestAssistantMessage,
    ParametersMessageOpenAIChatCompletionRequestToolMessage,
    ParametersMessageOpenAIChatCompletionRequestFunctionMessage,
]


class ParametersResponseFormat(BaseModel):
    type: Optional[Literal["text", "json_object"]] = None


class ParametersStreamOptions(BaseModel):
    include_usage: bool


class ParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction(BaseModel):
    name: str


class ParametersToolChoiceOpenAIChatCompletionNamedToolChoice(BaseModel):
    function: ParametersToolChoiceOpenAIChatCompletionNamedToolChoiceFunction

    type: Literal["function"]


ParametersToolChoice = Union[
    Literal["none", "auto", "required"], ParametersToolChoiceOpenAIChatCompletionNamedToolChoice
]


class ParametersToolFunction(BaseModel):
    name: str

    description: Optional[str] = None

    parameters: Optional[Dict[str, Optional[object]]] = None


class ParametersTool(BaseModel):
    function: ParametersToolFunction

    type: Literal["function"]


class Parameters(BaseModel):
    messages: List[ParametersMessage]

    model: str

    frequency_penalty: Optional[float] = None

    logit_bias: Optional[Dict[str, int]] = None

    logprobs: Optional[bool] = None

    max_tokens: Optional[int] = None

    n: Optional[int] = None

    parallel_tool_calls: Optional[bool] = None

    presence_penalty: Optional[float] = None

    response_format: Optional[ParametersResponseFormat] = None

    seed: Optional[int] = None

    stop: Union[str, List[str], None] = None

    stream: Optional[bool] = None

    stream_options: Optional[ParametersStreamOptions] = None

    temperature: Optional[float] = None

    tool_choice: Optional[ParametersToolChoice] = None

    tools: Optional[List[ParametersTool]] = None

    top_logprobs: Optional[int] = None

    top_p: Optional[float] = None

    user: Optional[str] = None


class ModelParameters(BaseModel):
    name: str

    parameters: Parameters

    provider: Literal["openai"]
