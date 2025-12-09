"""
Advent of Code 2025 - Day 3
"""

def part1(input_text: str) -> int:


  return 0, 0


def part2(input_text: str) -> int:
  return part1(input_text)[1]

def main():
    """Run the solutions and print results."""
    # Read the full input
    with open('text/3.txt', 'r') as f:
        input_text = f.read()
    
    print("Day 2 Solutions:")
    print(f"Part 1: {part1(input_text)[0]}")
    print(f"Part 2: {part1(input_text)[1]}")


if __name__ == "__main__":
    main()
