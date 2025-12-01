"""
Advent of Code 2025 - Day 1
"""


def part1(input_text: str) -> int:
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split('\n')
    print(lines)
    # TODO: Implement solution
    dial = 50
    counter = 0

    for line in lines:
        direction = line[0]
        steps = int(line[1:][-2:])

        if direction == 'L':
            dial -= steps
        elif direction == 'R':
            dial += steps

        if dial > 99:
            dial -= 100
        elif dial < 0:
            dial += 100

        if dial == 0:
            counter += 1

    return counter


def part2(input_text: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = input_text.strip().split('\n')
    # TODO: Implement solution
    return 0


def main():
    """Run the solutions and print results."""
    # Read the full input
    with open('text/1.txt', 'r') as f:
        input_text = f.read()
    
    print("Day 1 Solutions:")
    print(f"Part 1: {part1(input_text)}")
    print(f"Part 2: {part2(input_text)}")


if __name__ == "__main__":
    main()
