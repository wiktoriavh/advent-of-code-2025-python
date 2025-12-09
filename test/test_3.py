"""
Tests for Day 3 using the example input from Advent of Code
"""
import pytest
import importlib
from pathlib import Path
import sys

project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.day3 import part1, part2

EXAMPLE_INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_part1_example():
    """Test part 1 with the example input."""
    result = part1(EXAMPLE_INPUT)[0]
    expected = 1227775554
    assert result == expected, f"Expected {expected}, got {result}"

def test_part2_example():
    """Test part 2 with the example input."""
    result = part2(EXAMPLE_INPUT)
    expected = 4174379265
    assert result == expected, f"Expected {expected}, got {result}"

