# ptcc/__init__.py

"""
ptcc

A utility package to remove `.pytest_cache` folders recursively.
"""

from .cleaner import remove_pytest_cache

__all__ = ["remove_pytest_cache"]
