# AI-Project

Two standalone Python scripts implementing genetic algorithms (GA) for classic optimization problems, written as coursework/practice exercises. There is no shared framework, CLI, or entry point tying them together — each file runs independently and prints its result to the console.

- **`1.py`** — Uses a genetic algorithm to search for traffic-light green/red timing values on a small 5-node road network (nodes A–E), trying to minimize simulated total wait time across intersections.
- **`2.py`** — Uses a genetic algorithm (order crossover + swap mutation) to approximate a solution to the Traveling Salesman Problem for 6 fixed cities with hardcoded coordinates.

## Tech Stack

- Python 3
- NumPy (used only in `1.py`, for `np.argsort` during elitism selection)
- Standard library: `random`, `math`

No external frameworks, no tests, no requirements file, and no input/output files — both scripts use hardcoded data and print results directly to stdout.

## Structure

```
1.py    - GA for traffic light timing optimization
2.py    - GA for Traveling Salesman Problem
```

This is a practice/learning project, not a packaged or deployed application.
