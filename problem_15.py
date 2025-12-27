# Starting in the top left corner of a 2 x 2 grid, and only being able to move
# to the right and down, there are exactly routes to the bottom right corner.
# 
# How many such routes are there through a 20 x 20 grid?

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
    for i in range(0,n+1):
        grid[i][0] = 1
    for j in range(0,m+1):
        grid[0][j] = 1
    for i in range(1,n+1):
        for j in range(1,m+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid

print(max(max(generate_path_tree(20,20))))
