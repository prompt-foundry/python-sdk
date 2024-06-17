# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvaluationAssertionCreateParams"]


class EvaluationAssertionCreateParams(TypedDict, total=False):
    evaluation_id: Required[Annotated[str, PropertyInfo(alias="evaluationId")]]

    json_path: Required[Annotated[Optional[str], PropertyInfo(alias="jsonPath")]]
    """A JSON path to use when matching the response.

    Only required when type is `JSON_EXACT_MATCH` or `JSON_CONTAINS`.
    """

    target_value: Required[Annotated[str, PropertyInfo(alias="targetValue")]]

    tool_name: Required[Annotated[Optional[str], PropertyInfo(alias="toolName")]]
    """The name of the tool to match.

    Only required when type is `TOOL_CALLED` or `TOOL_CALLED_WITH`.
    """

    type: Required[
        Literal["EXACT_MATCH", "CONTAINS", "JSON_EXACT_MATCH", "JSON_CONTAINS", "TOOL_CALLED", "TOOL_CALLED_WITH"]
    ]
    """The type of evaluation matcher to use."""
