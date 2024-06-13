# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["EvaluationAssertionListParams"]


class EvaluationAssertionListParams(TypedDict, total=False):
    evaluation_id: Annotated[str, PropertyInfo(alias="evaluationId")]
    """Optional ID to filter the assertions by specific evaluation ID"""
