grid_width = 10
grid_height = 10
import time
from matplotlib.pyplot import grid
import pandas as pd

def create_binary_grid(width, height):
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        grid.append(row)
    return grid

wrld = create_binary_grid(grid_width, grid_height)

def state_filler(grid):
    import random
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            match random.uniform(0,1):
                case p if p >= 0.9:
                    grid[i][j] = 1
                case p if p >= 0.8:
                    grid[i][j] = 0.9
                case p if p >= 0.7:
                    grid[i][j] = 0.8
                case p if p >= 0.6:
                    grid[i][j] = 0.7
                case p if p >= 0.5:
                    grid[i][j] = 0.6
                case p if p >= 0.4:
                    grid[i][j] = 0.5
                case p if p >= 0.3:
                    grid[i][j] = 0.4
                case p if p >= 0.2:
                    grid[i][j] = 0.3
                case p if p >= 0.1:
                    grid[i][j] = 0.2
                case p if p >= 0:
                    grid[i][j] = 0.1
    return grid

tile_states = state_filler(wrld)

def print_grid(grid):
    states = {
        0: "🌲",  # Tree
        0.1: "🌳",  # Young Tree
        0.2: "🟫",  # Palm Tree
        0.3: "🟫",  # Cactus
        0.4: "🟫",  # Four Leaf Clover
        0.5: "🟫",  # Leaf Fluttering in Wind
        0.6: "🍂",  # Fallen Leaf
        0.7: "🟫",  # Maple Leaf
        0.8: "🌾",  # Sheaf of Rice
        0.9: "🌿",  # Herb
        1: "🟫"   # Empty
    }
    for row in grid:
        for cell in row:
            print(states.get(cell), end=' ')
        print()

print_grid(tile_states)