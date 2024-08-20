# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["ToolUpdateParams"]


class ToolUpdateParams(TypedDict, total=False):
    description: Required[str]
    """
    A description of what the tool does, used by the model to choose when and how to
    call the tool.
    """

    name: Required[str]
    """The name of the tool to be called.

    Must be a-z, A-Z, 0-9, or contain underscores and dashes, with a maximum length
    of 64.
    """

    parameters: Required[Dict[str, Optional[object]]]
    """The parameters the functions accepts, described as a JSON Schema object.

    This schema is designed to match the TypeScript Record<string, unknown>,
    allowing for any properties with values of any type.
    """
