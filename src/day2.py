"""
Advent of Code 2025 - Day 1
"""

def part1(input_text: str) -> int:
  ranges = input_text.strip().split(",")
  ids = [range.split("-") for range in ranges]
  
  invalidIds = 0
  invalidIds2 = 0

  for range in ids:
    alpha, beta = map(int, range)

    while alpha <= beta:
      id = str(alpha)

      repeats = repeating(id, 2)
      if repeats:
        invalidIds2 += alpha

      if len(id) % 2 != 0:
        alpha += 1
        continue

      mid = len(id) // 2

      left = id[:mid]
      right = id[mid:]
      if left == right:
        invalidIds += alpha

      alpha += 1

  return invalidIds, invalidIds2

def repeating(id: str, divide: int) -> int:
 
  if divide > len(id):
    return False
  
  num = int(id)
  length = len(id)
  
  if length % divide != 0:
    return repeating(id, divide + 1)

  size = length // divide
  parts = [id[i * size : (i + 1) * size] for i in range(divide)]
  part1 = parts[0]

  repeats = False

  for part in parts:
   if part1 == part:
     repeats = True
   else:
     repeats = False
     break

  if repeats:
    return True
  else:
    return repeating(id, divide + 1)

def part2(input_text: str) -> int:
  return part1(input_text)[1]

def main():
    """Run the solutions and print results."""
    # Read the full input
    with open('text/2.txt', 'r') as f:
        input_text = f.read()
    
    print("Day 2 Solutions:")
    print(f"Part 1: {part1(input_text)[0]}")
    print(f"Part 2: {part1(input_text)[1]}")


if __name__ == "__main__":
    main()
