file = open('data.txt', 'r')
content = file.read()
file.close()
content = content.splitlines()

grid = []
for i in range(0,len(content)):
    grid.append(content[i].split())
grid = [[int(item) for item in inner_list] for inner_list in grid]

def max_prod_any_dir(grid,n):
    max_prod = 0
    for i in range(0,len(grid)):
        for j in range(0,len(grid[0])):
            # horizontal
            if j <= len(grid)-n:
                prod = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
                max_prod = max(max_prod, prod)
            # vertical
            if i <= len(grid)-n:
                prod = grid[i][j] + grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
                max_prod = max(max_prod, prod)
            # diagonal_down_right
            if i <= len(grid)-n and j <= len(grid)-n:
                prod = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
                max_prod = max(max_prod, prod)
            # diagonal_down_left
            if i <= len(grid)-n and j <= len(grid)-n:
                prod = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
                max_prod = max(max_prod, prod)
    return max_prod


def printgrid():
    for row in grid:
        print(row)