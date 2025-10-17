# https://leetcode.com/problems/number-of-islands/description/
# Number of Islands


def dfs(i, j, grid, visited):
    
    if (i < 0 or i >= len(grid) or
        j < 0 or j >= len(grid[0]) or
        grid[i][j] == "0" or visited[i][j]):
        return

    visited[i][j] = True
    

    # Все 4 направления
    dfs(i + 1, j, grid, visited)
    dfs(i - 1, j, grid, visited)
    dfs(i, j + 1, grid, visited)
    dfs(i, j - 1, grid, visited)


def get_number_of_islands(grid):

    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])

    visited = [[False] * cols for _ in range(rows)]

    number_of_islands = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1" and not visited[i][j]:
                dfs(i, j, grid, visited)
                number_of_islands += 1

    return number_of_islands


grid = eval(input())
print(get_number_of_islands(grid))