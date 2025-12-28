# Starting in the top left corner of a 2 x 2 grid, and only being able to move
# to the right and down, there are exactly routes to the bottom right corner.
# 
# How many such routes are there through a 20 x 20 grid?

# Brute force solution. The number of paths to reach any lattice point is the
# sum of the number of paths to reach the cell left and the cell above. There
# is only one path to reach any cell on the top and left borders.

def generate_grid(n,m):
    grid = []
    for i in range(0,n+1):
        row = []
        for j in range(0,m+1):
            row.append(0)
        grid.append(row)
    return grid

def generate_path_tree(n,m):
    grid = generate_grid(n,m)
    # populate the top row with 1s
    for i in range(0,n+1):
        grid[i][0] = 1
    # populate the left column with 1s
    for j in range(0,m+1):
        grid[0][j] = 1
    # fill in the rest of the grid
    for i in range(1,n+1):
        for j in range(1,m+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid

print(max(max(generate_path_tree(20,20))))

# There is a simple combinatoric solution: this is a simple 'n choose k' problem.
# There are 40 steps (20 right and 20 down) for all solutions and 20 of those must
# be down (or 20 must be right). So this would be 40 choose 20 or 40! / (20! * 20!)

import math

# Calculate the number of combinations
print(math.comb(40, 20))