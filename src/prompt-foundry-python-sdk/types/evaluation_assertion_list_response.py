# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .evaluation_assertion import EvaluationAssertion

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from ..types import shared

__all__ = ["EvaluationAssertionListResponse"]

EvaluationAssertionListResponse = List[EvaluationAssertion]