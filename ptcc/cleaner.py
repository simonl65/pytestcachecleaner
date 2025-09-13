# ptcc/cleaner.py

"""
ptcc.cleaner

Provides functionality to remove all `.pytest_cache` folders
from a given root directory and its subdirectories.
"""

import shutil
from pathlib import Path


def remove_pytest_cache(root: str) -> int:
    """
    Recursively find and remove all `.pytest_cache` folders
    under the given root directory.

    Args:
        root (str): Root directory path to start the search.

    Returns:
        int: Number of `.pytest_cache` folders removed.
    """
    root_path = Path(root).resolve()
    count = 0

    for cache_dir in root_path.rglob(".pytest_cache"):
        if cache_dir.is_dir():
            shutil.rmtree(cache_dir, ignore_errors=True)
            count += 1

    return count
