"""The main point for importing pytest-asyncio items.

PYTEST_DONT_REWRITE
"""

from __future__ import annotations

from importlib.metadata import version

from .plugin import fixture, is_async_test

__version__ = version(__name__)

__all__ = ("fixture", "is_async_test")
