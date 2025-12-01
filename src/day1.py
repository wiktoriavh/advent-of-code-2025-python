"""
Advent of Code 2025 - Day 1
"""


def part1(input_text: str) -> int:
    """Solve part 1 of the puzzle."""
    lines = input_text.strip().split('\n')

    dial = 50
    counter = 0
    counter2 = 0

    for line in lines:
        direction = line[0]

        if line[1:-2].isdigit():
            rotations = int(line[1:-2])
        else:
            rotations = 0
        steps = int(line[1:][-2:])

        prevDial = dial

        if direction == 'L':
            dial -= steps
        elif direction == 'R':
            dial += steps

        combined = dial
        clicked = False

        if dial > 99:
            dial -= 100
            if prevDial != 0:
                clicked = True
        elif dial < 0:
            dial += 100
            if prevDial != 0:
                clicked = True

        if dial == 0:
            counter += 1
            counter2 += 1
        elif clicked:
            counter2 += 1

        counter2 += rotations

    return counter, counter2


def part2(input_text: str) -> int:
    """Solve part 2 of the puzzle."""
    lines = input_text.strip().split('\n')
    # TODO: Implement solution
    return part1(input_text)[1]


def main():
    """Run the solutions and print results."""
    # Read the full input
    with open('text/1.txt', 'r') as f:
        input_text = f.read()
    
    print("Day 1 Solutions:")
    print(f"Part 1: {part1(input_text)[0]}")
    print(f"Part 2: {part1(input_text)[1]}")


if __name__ == "__main__":
    main()
