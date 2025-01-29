# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Base classes for LLM and Embedding models."""

from abc import ABC, abstractmethod
from typing import Any, AsyncGenerator, Generator


class BaseLLMCallback:
    """Base class for LLM callbacks."""

    def __init__(self):
        self.response = []

    def on_llm_new_token(self, token: str):
        """Handle when a new token is generated."""
        self.response.append(token)


class BaseLLM(ABC):
    """The Base LLM implementation."""

    @abstractmethod
    def generate(
        self,
        messages: str | list[Any],
        streaming: bool = True,
        callbacks: list[BaseLLMCallback] | None = None,
        **kwargs: Any,
    ) -> str:
        """Generate a response."""

    @abstractmethod
    def stream_generate(
        self,
        messages: str | list[Any],
        callbacks: list[BaseLLMCallback] | None = None,
        **kwargs: Any,
    ) -> Generator[str, None, None]:
        """Generate a response with streaming."""
    
    @abstractmethod
    async def agenerate(
        self,
        messages: str | list[Any],
        streaming: bool = True,
        callbacks: list[BaseLLMCallback] | None = None,
        **kwargs: Any,
    ) -> str:
        """Generate a response asynchronously."""
    
    @abstractmethod
    async def astream_generate(
        self,
        messages: str | list[Any],
        callbacks: list[BaseLLMCallback] | None = None,
        **kwargs: Any,
    ) -> AsyncGenerator[str, None]:
        """Generate a response asynchronously with streaming."""

class BaseTextEmbedding(ABC):
    """The text embedding interface."""

    @abstractmethod
    def embed(self, text: str, **kwargs: Any) -> list[float]:
        """Embed a text string."""

    @abstractmethod
    async def aembed(self, text: str, **kwargs: Any) -> list[float]:
        """Embed a text string asynchronously."""
