# tests/test_cli.py

"""
Tests for the ptcc.cli module.
"""

import sys
import pytest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ptcc.cli import main


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


def test_main_default_path() -> None:
    """
    Test the main function with the default path.
    """
    with ExitStack() as stack:
        stack.enter_context(patch.object(sys, "argv", ["ptcc"]))
        mock_remove = stack.enter_context(patch("ptcc.cli.remove_pytest_cache"))
        mock_print = stack.enter_context(patch("builtins.print"))
        mock_exit = stack.enter_context(patch("sys.exit"))

        mock_remove.return_value = 3
        main()
        mock_remove.assert_called_once_with(".")
        mock_print.assert_called_once_with("Removed 3 `.pytest_cache` folder(s).")
        mock_exit.assert_called_once_with(0)


def test_main_custom_path() -> None:
    """
    Test the main function with a custom path.
    """
    with ExitStack() as stack:
        stack.enter_context(patch.object(sys, "argv", ["ptcc", "/tmp/test_path"]))
        mock_remove = stack.enter_context(patch("ptcc.cli.remove_pytest_cache"))
        mock_print = stack.enter_context(patch("builtins.print"))
        mock_exit = stack.enter_context(patch("sys.exit"))

        mock_remove.return_value = 5
        main()
        mock_remove.assert_called_once_with("/tmp/test_path")
        mock_print.assert_called_once_with("Removed 5 `.pytest_cache` folder(s).")
        mock_exit.assert_called_once_with(0)


def test_main_end_to_end(tmp_path: Path, capsys) -> None:
    """
    Test the main function end-to-end.
    """
    depths = [1, 2, 3]
    expected_count = create_test_project(tmp_path, depths)

    with patch.object(sys, "argv", ["ptcc", str(tmp_path)]):
        with pytest.raises(SystemExit) as e:
            main()

    captured = capsys.readouterr()
    assert f"Removed {expected_count} `.pytest_cache` folder(s)." in captured.out
    assert e.value.code == 0
    for cache_dir in tmp_path.rglob(".pytest_cache"):
        assert not cache_dir.exists()


def test_main_no_cache_found(tmp_path: Path, capsys) -> None:
    """
    Test the main function when no .pytest_cache folders are found.
    """
    with patch.object(sys, "argv", ["ptcc", str(tmp_path)]):
        with pytest.raises(SystemExit) as e:
            main()

    captured = capsys.readouterr()
    assert "Removed 0 `.pytest_cache` folder(s)." in captured.out
    assert e.value.code == 0


def test_main_help(capsys) -> None:
    """
    Test the main function with the --help argument.
    """
    with patch.object(sys, "argv", ["ptcc", "--help"]):
        with pytest.raises(SystemExit) as e:
            main()

    captured = capsys.readouterr()
    assert "show this help message and exit" in captured.out
    assert e.value.code == 0