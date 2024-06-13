# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import time
import anyio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import PromptFoundry, AsyncPromptFoundry


class SyncAPIResource:
    _client: PromptFoundry

    def __init__(self, client: PromptFoundry) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list

    def _sleep(self, seconds: float) -> None:
        time.sleep(seconds)


class AsyncAPIResource:
    _client: AsyncPromptFoundry

    def __init__(self, client: AsyncPromptFoundry) -> None:
        self._client = client
        self._get = client.get
        self._post = client.post
        self._patch = client.patch
        self._put = client.put
        self._delete = client.delete
        self._get_api_list = client.get_api_list

    async def _sleep(self, seconds: float) -> None:
        await anyio.sleep(seconds)