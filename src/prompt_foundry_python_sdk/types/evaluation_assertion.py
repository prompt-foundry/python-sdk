# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "EvaluationAssertion",
    "EvaluationAssertionExactMatch",
    "EvaluationAssertionContainsAll",
    "EvaluationAssertionContainsAny",
    "EvaluationAssertionStartsWith",
    "EvaluationAssertionCost",
    "EvaluationAssertionLatency",
    "EvaluationAssertionToolCalled",
    "EvaluationAssertionToolCalledWith",
]


class EvaluationAssertionExactMatch(BaseModel):
    id: str

    evaluation_id: str = FieldInfo(alias="evaluationId")

    target_value: str = FieldInfo(alias="targetValue")
    """The value to match."""

    type: Literal["EXACT_MATCH"]

    ignore_case: Optional[bool] = FieldInfo(alias="ignoreCase", default=None)
    """Whether to ignore case when comparing strings."""

    json_path: Optional[str] = FieldInfo(alias="jsonPath", default=None)
    """A JSON path to use when matching a JSON response."""

    negate: Optional[bool] = None
    """Whether to negate the assertion. "true" means the assertion must NOT be true."""

    weight: Optional[float] = None
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionContainsAll(BaseModel):
    id: str

    evaluation_id: str = FieldInfo(alias="evaluationId")

    target_values: List[str] = FieldInfo(alias="targetValues")
    """List of values any of which may be present."""

    type: Literal["CONTAINS_ALL"]

    ignore_case: Optional[bool] = FieldInfo(alias="ignoreCase", default=None)
    """Whether to ignore case when comparing strings."""

    json_path: Optional[str] = FieldInfo(alias="jsonPath", default=None)
    """A JSON path to use when matching a JSON response."""

    negate: Optional[bool] = None
    """Whether to negate the assertion. "true" means the assertion must NOT be true."""

    weight: Optional[float] = None
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionContainsAny(BaseModel):
    id: str

    evaluation_id: str = FieldInfo(alias="evaluationId")

    target_values: List[str] = FieldInfo(alias="targetValues")
    """List of values any of which may be present."""

    type: Literal["CONTAINS_ANY"]

    ignore_case: Optional[bool] = FieldInfo(alias="ignoreCase", default=None)
    """Whether to ignore case when comparing strings."""

    json_path: Optional[str] = FieldInfo(alias="jsonPath", default=None)
    """A JSON path to use when matching a JSON response."""

    negate: Optional[bool] = None
    """Whether to negate the assertion. "true" means the assertion must NOT be true."""

    weight: Optional[float] = None
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionStartsWith(BaseModel):
    id: str

    evaluation_id: str = FieldInfo(alias="evaluationId")

    target_value: str = FieldInfo(alias="targetValue")
    """The value that the response should start with."""

    type: Literal["STARTS_WITH"]

    ignore_case: Optional[bool] = FieldInfo(alias="ignoreCase", default=None)
    """Whether to ignore case when comparing strings."""

    json_path: Optional[str] = FieldInfo(alias="jsonPath", default=None)
    """A JSON path to use when matching a JSON response."""

    negate: Optional[bool] = None
    """Whether to negate the assertion. "true" means the assertion must NOT be true."""

    weight: Optional[float] = None
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionCost(BaseModel):
    id: str

    evaluation_id: str = FieldInfo(alias="evaluationId")

    target_threshold: float = FieldInfo(alias="targetThreshold")
    """The cost threshold to be evaluated against."""

    type: Literal["COST"]

    weight: Optional[float] = None
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionLatency(BaseModel):
    id: str

    evaluation_id: str = FieldInfo(alias="evaluationId")

    target_threshold: float = FieldInfo(alias="targetThreshold")
    """The latency threshold to be evaluated against."""

    type: Literal["LATENCY"]

    weight: Optional[float] = None
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionToolCalled(BaseModel):
    id: str

    evaluation_id: str = FieldInfo(alias="evaluationId")

    tool_name: str = FieldInfo(alias="toolName")
    """The name of the tool that should have been called."""

    type: Literal["TOOL_CALLED"]

    weight: Optional[float] = None
    """How heavily to weigh the assertion within the evaluation."""


class EvaluationAssertionToolCalledWith(BaseModel):
    id: str

    arg_key_name: str = FieldInfo(alias="argKeyName")
    """The argument name to be matched."""

    evaluation_id: str = FieldInfo(alias="evaluationId")

    tool_name: str = FieldInfo(alias="toolName")
    """The name of the tool that should have been called."""

    type: Literal["TOOL_CALLED_WITH"]

    ignore_case: Optional[bool] = FieldInfo(alias="ignoreCase", default=None)
    """Whether to ignore case when comparing argument names."""

    negate: Optional[bool] = None
    """Whether to negate the assertion. "true" means the assertion must NOT be true."""

    weight: Optional[float] = None
    """How heavily to weigh the assertion within the evaluation."""


EvaluationAssertion: TypeAlias = Annotated[
    Union[
        EvaluationAssertionExactMatch,
        EvaluationAssertionContainsAll,
        EvaluationAssertionContainsAny,
        EvaluationAssertionStartsWith,
        EvaluationAssertionCost,
        EvaluationAssertionLatency,
        EvaluationAssertionToolCalled,
        EvaluationAssertionToolCalledWith,
    ],
    PropertyInfo(discriminator="type"),
]
