# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from typing_extensions import Literal

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["EvaluationAssertion", "Matcher"]


class Matcher(BaseModel):
    json_path: Optional[str] = FieldInfo(alias="jsonPath", default=None)
    """A JSON path to use when matching the response.

    Only required when type is `jsonPath`.
    """

    type: Literal["CONTAINS", "EQUALS", "JSON"]
    """The type of evaluation matcher to use."""


class EvaluationAssertion(BaseModel):
    id: str

    evaluation_id: str = FieldInfo(alias="evaluationId")

    matcher: Matcher

    target: str
