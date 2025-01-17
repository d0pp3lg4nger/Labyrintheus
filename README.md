# Labyrintheus

Labyrintheus is a project where labyrinths are dynamically generated using graph-based algorithms and are autonomously solved with the help of search algorithms.

## Features
- **Labyrinth Generation**: Utilizes Depth-First Search (DFS) with backtracking to create unique and solvable mazes.
- **Autonomous Solving**: Implements Breadth-First Search (BFS) to efficiently find the shortest path from start to finish.

## How It Works
1. **Generation**:
   - The labyrinth is represented as a grid.
   - DFS is used to carve out paths, ensuring a single solution.

2. **Resolution**:
   - BFS traverses the labyrinth from the starting point to the end, identifying the shortest route.

## Visualization
- **Start Point**: Marked as `S` in the labyrinth.
- **End Point**: Marked as `E` in the labyrinth.
- **Solution Path**: Highlighted with dots (`.`) for clear visualization.

## Example Output
### Generated Labyrinth
```
#####################
#S  #       #       #
### ### ### # ##### #
#   #   #   #   #   #
# ##### ##### ##### #
#       #       #  E#
#####################
```

### Solved Labyrinth
```
#####################
#S..#.......#.......#
###.###.###.#.#####.#
#...#...#...#...#...#
#.#####.#####.#####.#
#.......#.......#..E#
#####################
```

## Technologies Used
- **Python**: Core programming language for the implementation.
- **Graph Algorithms**: DFS for generation and BFS for solving.

## Future Enhancements
- Add random start and end points.
- Implement additional solving algorithms (e.g., A*).
- Provide interactive visualizations.
