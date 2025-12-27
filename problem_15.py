# Starting in the top left corner of a 2 x 2 grid, and only being able to move
# to the right and down, there are exactly routes to the bottom right corner.
# 
# How many such routes are there through a 20 x 20 grid?

def generate_grid(n,m):
    for i in range(0,n):
        row = []
        for j in range(0,m):
            row.append([i,j])
        grid.append(row)
    return grid