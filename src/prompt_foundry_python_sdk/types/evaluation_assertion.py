# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["EvaluationAssertion"]


class EvaluationAssertion(BaseModel):
    id: str

    evaluation_id: str = FieldInfo(alias="evaluationId")

    json_path: Optional[str] = FieldInfo(alias="jsonPath", default=None)
    """A JSON path to use when matching the response.

    Only required when type is `JSON_EXACT_MATCH` or `JSON_CONTAINS`.
    """

    target_threshold: Optional[float] = FieldInfo(alias="targetThreshold", default=None)

    target_values: Optional[List[str]] = FieldInfo(alias="targetValues", default=None)

    tool_name: Optional[str] = FieldInfo(alias="toolName", default=None)
    """The name of the tool to match.

    Only required when type is `TOOL_CALLED` or `TOOL_CALLED_WITH`.
    """

    type: Literal[
        "CONTAINS_ALL",
        "CONTAINS_ANY",
        "COST",
        "EXACT_MATCH",
        "LATENCY",
        "STARTS_WITH",
        "TOOL_CALLED",
        "TOOL_CALLED_WITH",
    ]
    """The type of evaluation matcher to use."""

    ignore_case: Optional[bool] = FieldInfo(alias="ignoreCase", default=None)

    negate: Optional[bool] = None

    weight: Optional[float] = None
    """How heavily to weigh the assertion within the evaluation."""
