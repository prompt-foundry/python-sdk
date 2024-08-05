# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .prompt_configuration import PromptConfiguration

__all__ = ["PromptListResponse"]

PromptListResponse: TypeAlias = List[PromptConfiguration]
