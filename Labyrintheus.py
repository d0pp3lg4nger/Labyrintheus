# Labyrintheus
# A labyrinth generated using a graph-based algorithm, which autonomously 
# solves itself through the implementation of a search algorithm.
# Author: Arthur Clemente (d0pp3lg4nger)
# Date: 2025-01-17
# Version: 1.0

# Importing libraries
import random
from collections import deque

def generate_labyrinth(rows, columns):
    # Initialize the labyrinth as a grid of walls
    labyrinth = [['#' for _ in range(columns)] for _ in range(rows)]
    
    # Possible directions
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)] # Up, Down, Left, Right
    
    # Verify if the cell is valid
    def is_valid(x, y):
        return 0 < x < (rows-1) and 0 < y < (columns-1) and labyrinth[x][y] == '#'
    
    def dfs(x, y):
        # Mark the cell as visited
        labyrinth[x][y] = ' '
        
        # Shuffle the directions
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy # Next cell
            if is_valid(nx, ny):
                labyrinth[x + dx//2][y + dy//2] = ' ' # Remove the wall between the actual cell and the next cell
                dfs(nx, ny)
    
    # Start the DFS algorithm
    dfs(1, 1)
    
    labyrinth[1][1] = 'S' # Start
    labyrinth[rows-2][columns-2] = 'E' # Exit
    
    return labyrinth

def solve_labyrinth(labyrinth):
    # Find the start and exit positions
    rows, columns = len(labyrinth), len(labyrinth[0])
    start = exit = None
    for i in range(rows):
        for j in range(columns):
            if labyrinth[i][j] == 'S':
                start = (i, j)
            elif labyrinth[i][j] == 'E':
                exit = (i, j)
    
    if not start or not exit:
        return None
    
    # Possible directions
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # Up, Down, Left, Right
    
    # BFS
    queue = deque([start])
    visited = set()  
    parent = {}
    visited.add(start)
    
    while queue:
        x, y = queue.popleft()
        
        if (x, y) == exit:
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = parent[(x, y)]
            path.append(start)
            return path[::-1]
        
        # Explore the neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (0 <= nx < rows and 0 <= ny < columns and
                labyrinth[nx][ny] in (' ', 'E') and
                (nx, ny) not in visited):
                
                queue.append((nx, ny))
                visited.add((nx, ny))
                parent[(nx, ny)] = (x, y) # Save the parent cell
    
    return None

def mark_path(labyrinth, path):
    for x, y in path:
        if labyrinth[x][y] not in ('S', 'E'):
            labyrinth[x][y] = '.' # Mark the path
            

def print_labyrinth(labyrinth):
    for row in labyrinth:
        print(''.join(row))

rows, columns = 21, 51
labyrinth = generate_labyrinth(rows, columns)
print_labyrinth(labyrinth)

path = solve_labyrinth(labyrinth)
if path:
    mark_path(labyrinth, path)
    print('\nSolved:')
    print_labyrinth(labyrinth)
else:
    print('\nNo solution found.')