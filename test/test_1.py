"""
Tests for Day 1 using the example input from Advent of Code
"""
import pytest
import importlib
from pathlib import Path
import sys

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.day1 import part1, part2

EXAMPLE_INPUT = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_part1_example():
    """Test part 1 with the example input."""
    result = part1(EXAMPLE_INPUT)[0]
    expected = 3
    assert result == expected, f"Expected {expected}, got {result}"


def test_part2_example():
    """Test part 2 with the example input."""
    result = part2(EXAMPLE_INPUT)
    expected = 6
    assert result == expected, f"Expected {expected}, got {result}"

