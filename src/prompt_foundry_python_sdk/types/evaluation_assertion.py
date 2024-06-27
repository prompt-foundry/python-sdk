# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
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

    target_value: Optional[str] = FieldInfo(alias="targetValue", default=None)

    tool_name: Optional[str] = FieldInfo(alias="toolName", default=None)
    """The name of the tool to match.

    Only required when type is `TOOL_CALLED` or `TOOL_CALLED_WITH`.
    """

    type: Literal["CONTAINS", "EXACT_MATCH", "JSON_CONTAINS", "JSON_EXACT_MATCH", "TOOL_CALLED", "TOOL_CALLED_WITH"]
    """The type of evaluation matcher to use."""
