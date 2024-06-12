# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Annotated

from .._utils import PropertyInfo

from typing import List, Union, Dict, Optional
from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo
from ..types import shared_params

__all__ = ["EvaluationAssertionListParams"]


class EvaluationAssertionListParams(TypedDict, total=False):
    evaluation_id: Annotated[str, PropertyInfo(alias="evaluationId")]
    """Optional ID to filter the assertions by specific evaluation ID"""
