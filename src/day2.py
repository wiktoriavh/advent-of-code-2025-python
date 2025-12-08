"""
Advent of Code 2025 - Day 1
"""

def part1(input_text: str) -> int:
  ranges = input_text.strip().split(",")
  ids = [range.split("-") for range in ranges]
  
  invalidIds = 0

  for range in ids:
    alpha, beta = map(int, range)

    while alpha <= beta:
      id = str(alpha)

      if len(id) % 2 != 0:
        alpha += 1
        continue

      mid = len(id) // 2

      left = id[:mid]
      right = id[mid:]
      if left == right:
        invalidIds += alpha

      alpha += 1

  return invalidIds


def part2(input_text: str) -> int:
  return 0

def main():
    """Run the solutions and print results."""
    # Read the full input
    with open('text/2.txt', 'r') as f:
        input_text = f.read()
    
    print("Day 2 Solutions:")
    print(f"Part 1: {part1(input_text)}")
    print(f"Part 2: {part2(input_text)}")


if __name__ == "__main__":
    main()
