# Advent of Code 2025 - Python

This repository contains my solutions for [Advent of Code 2025](https://adventofcode.com/2025).

## Project Structure

```
.
├── src/          # Solution code for each day
├── test/         # Tests using example inputs from AoC
├── text/         # Full puzzle inputs from AoC
└── requirements.txt
```

## Setup

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**On Linux/Mac:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running Solutions

### Run a Specific Day

To run the solution for a specific day and see the output:

```bash
python -m src.day1
```

Replace `1` with the day you want to run (e.g., `2`, `3`, etc.).

### Run from the src directory

Alternatively, you can run from within the src directory:

```bash
cd src
python day1.py
```

## Testing

### Run Tests for a Specific Day with watching the scr

```bash
ptw -- test/test_1.py -v
```

### Run All Tests

```bash
pytest -v
```

### Run Tests with Coverage

```bash
pytest --cov=src --cov-report=term-missing
```

## Workflow for Each Day

1. **Create new day files:**
   - Copy `src/day1.py` to `src/dayX.py` (where X is the day number)
   - Copy `test/test_1.py` to `test/test_X.py`
   - Create `text/X.txt` for your puzzle input

2. **Get the puzzle input:**
   - Go to https://adventofcode.com/2025/day/X
   - Copy the example input into your test file
   - Copy your full input into `text/X.txt`

3. **Implement the solution:**
   - Start with Part 1 in `src/dayX.py`
   - Run tests: `pytest test/test_X.py -v`
   - Run the solution: `python -m src.X`

4. **Submit and continue:**
   - Submit Part 1 answer
   - Implement Part 2
   - Test and run again

## Deactivating the Virtual Environment

When you're done working:

```bash
deactivate
```

Happy Coding! 🎄⭐

