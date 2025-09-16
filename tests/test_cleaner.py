# tests/test_cleaner.py

"""
Tests for the ptcc.cleaner module.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ptcc.cleaner import remove_pytest_cache

def create_test_project(root: Path, depths: list[int]) -> int:
    """
    Create a test project structure with .pytest_cache folders.
    """
    count = 0
    for i, depth in enumerate(depths):
        path = root / f"project_{i}"
        for d in range(depth):
            path = path / f"level_{d}"
        path.mkdir(parents=True, exist_ok=True)
        (path / ".pytest_cache").mkdir()
        count += 1
    return count

def test_remove_pytest_cache(tmp_path: Path) -> None:
    """
    Test the remove_pytest_cache function.
    """
    # Create a test project structure
    depths = [1, 2, 3]
    expected_count = create_test_project(tmp_path, depths)

    # Run the cleaner
    removed_count = remove_pytest_cache(str(tmp_path))

    # Check the result
    assert removed_count == expected_count
    for cache_dir in tmp_path.rglob(".pytest_cache"):
        assert not cache_dir.exists()
