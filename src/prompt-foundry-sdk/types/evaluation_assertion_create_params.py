# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated, Required, Literal

from .._utils import PropertyInfo

from typing import Optional

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["EvaluationAssertionCreateParams", "Matcher"]


class EvaluationAssertionCreateParams(TypedDict, total=False):
    evaluation_id: Required[Annotated[str, PropertyInfo(alias="evaluationId")]]

    matcher: Required[Matcher]

    target: Required[str]


class Matcher(TypedDict, total=False):
    json_path: Required[Annotated[Optional[str], PropertyInfo(alias="jsonPath")]]
    """A JSON path to use when matching the response.

    Only required when type is `jsonPath`.
    """

    type: Required[Literal["CONTAINS", "EQUALS", "JSON"]]
    """The type of evaluation matcher to use."""
