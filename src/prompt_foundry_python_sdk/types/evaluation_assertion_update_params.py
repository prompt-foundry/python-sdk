# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "EvaluationAssertionUpdateParams",
    "EvaluationAssertionExactMatchBody",
    "EvaluationAssertionContainsAllBody",
    "EvaluationAssertionContainsAnyBody",
    "EvaluationAssertionStartsWithBody",
    "EvaluationAssertionCostBody",
    "EvaluationAssertionLatencyBody",
    "EvaluationAssertionToolCalledBody",
    "EvaluationAssertionToolCalledWithBody",
]


class EvaluationAssertionExactMatchBody(TypedDict, total=False):
    evaluation_id: Required[Annotated[str, PropertyInfo(alias="evaluationId")]]

    target_value: Required[Annotated[str, PropertyInfo(alias="targetValue")]]
    """The value to match."""

    type: Required[Literal["EXACT_MATCH"]]

    ignore_case: Annotated[bool, PropertyInfo(alias="ignoreCase")]
    """Whether to ignore case when comparing strings."""

    json_path: Annotated[Optional[str], PropertyInfo(alias="jsonPath")]
    """A JSON path to use when matching a JSON response."""

    negate: bool
    """Whether to negate the assertion. "true" means the assertion must NOT be true."""

    weight: float
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionContainsAllBody(TypedDict, total=False):
    evaluation_id: Required[Annotated[str, PropertyInfo(alias="evaluationId")]]

    target_values: Required[Annotated[List[str], PropertyInfo(alias="targetValues")]]
    """List of values any of which may be present."""

    type: Required[Literal["CONTAINS_ALL"]]

    ignore_case: Annotated[bool, PropertyInfo(alias="ignoreCase")]
    """Whether to ignore case when comparing strings."""

    json_path: Annotated[Optional[str], PropertyInfo(alias="jsonPath")]
    """A JSON path to use when matching a JSON response."""

    negate: bool
    """Whether to negate the assertion. "true" means the assertion must NOT be true."""

    weight: float
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionContainsAnyBody(TypedDict, total=False):
    evaluation_id: Required[Annotated[str, PropertyInfo(alias="evaluationId")]]

    target_values: Required[Annotated[List[str], PropertyInfo(alias="targetValues")]]
    """List of values any of which may be present."""

    type: Required[Literal["CONTAINS_ANY"]]

    ignore_case: Annotated[bool, PropertyInfo(alias="ignoreCase")]
    """Whether to ignore case when comparing strings."""

    json_path: Annotated[Optional[str], PropertyInfo(alias="jsonPath")]
    """A JSON path to use when matching a JSON response."""

    negate: bool
    """Whether to negate the assertion. "true" means the assertion must NOT be true."""

    weight: float
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionStartsWithBody(TypedDict, total=False):
    evaluation_id: Required[Annotated[str, PropertyInfo(alias="evaluationId")]]

    target_value: Required[Annotated[str, PropertyInfo(alias="targetValue")]]
    """The value that the response should start with."""

    type: Required[Literal["STARTS_WITH"]]

    ignore_case: Annotated[bool, PropertyInfo(alias="ignoreCase")]
    """Whether to ignore case when comparing strings."""

    json_path: Annotated[Optional[str], PropertyInfo(alias="jsonPath")]
    """A JSON path to use when matching a JSON response."""

    negate: bool
    """Whether to negate the assertion. "true" means the assertion must NOT be true."""

    weight: float
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionCostBody(TypedDict, total=False):
    evaluation_id: Required[Annotated[str, PropertyInfo(alias="evaluationId")]]

    target_threshold: Required[Annotated[float, PropertyInfo(alias="targetThreshold")]]
    """The cost threshold to be evaluated against."""

    type: Required[Literal["COST"]]

    weight: float
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionLatencyBody(TypedDict, total=False):
    evaluation_id: Required[Annotated[str, PropertyInfo(alias="evaluationId")]]

    target_threshold: Required[Annotated[float, PropertyInfo(alias="targetThreshold")]]
    """The latency threshold to be evaluated against."""

    type: Required[Literal["LATENCY"]]

    weight: float
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionToolCalledBody(TypedDict, total=False):
    evaluation_id: Required[Annotated[str, PropertyInfo(alias="evaluationId")]]

    tool_name: Required[Annotated[str, PropertyInfo(alias="toolName")]]
    """The name of the tool that should have been called."""

    type: Required[Literal["TOOL_CALLED"]]

    weight: float
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionToolCalledWithBody(TypedDict, total=False):
    arg_key_name: Required[Annotated[str, PropertyInfo(alias="argKeyName")]]
    """The argument name to be matched."""

    evaluation_id: Required[Annotated[str, PropertyInfo(alias="evaluationId")]]

    tool_name: Required[Annotated[str, PropertyInfo(alias="toolName")]]
    """The name of the tool that should have been called."""

    type: Required[Literal["TOOL_CALLED_WITH"]]

    ignore_case: Annotated[bool, PropertyInfo(alias="ignoreCase")]
    """Whether to ignore case when comparing argument names."""

    negate: bool
    """Whether to negate the assertion. "true" means the assertion must NOT be true."""

    weight: float
    """How heavily to weigh the assertion within the evaluation."""


EvaluationAssertionUpdateParams: TypeAlias = Union[
    EvaluationAssertionExactMatchBody,
    EvaluationAssertionContainsAllBody,
    EvaluationAssertionContainsAnyBody,
    EvaluationAssertionStartsWithBody,
    EvaluationAssertionCostBody,
    EvaluationAssertionLatencyBody,
    EvaluationAssertionToolCalledBody,
    EvaluationAssertionToolCalledWithBody,
]
