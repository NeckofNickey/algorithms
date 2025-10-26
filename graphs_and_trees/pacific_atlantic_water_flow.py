# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# 417. Pacific Atlantic Water Flow

from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    
    if not heights or not heights[0]:
        return []

    rows, cols = len(heights), len(heights[0])
    pacific = [[False] * cols for _ in range(rows)]
    atlantic = [[False] * cols for _ in range(rows)]

    def dfs(r, c, visited, prev_hight):

        if (r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or heights[r][c] < prev_hight):
            return
        
        visited[r][c] = True
        # Рекурсивно посещаем соседей
        dfs(r + 1, c, visited, heights[r][c])
        dfs(r - 1, c, visited, heights[r][c])
        dfs(r, c + 1, visited, heights[r][c])
        dfs(r, c - 1, visited, heights[r][c])

    # Запускаем от границ Тихого океана (верх и лево)
    for c in range(cols):
        dfs(0, c, pacific, heights[0][c]) # Верхняя граница
    for r in range(rows):
        dfs(r, 0, pacific, heights[r][0]) # Левая граница

    # Запускаем от границ Атлантического океана (низ и право)
    for c in range(cols):
        dfs(rows - 1, c, atlantic, heights[rows - 1][c]) # Нижняя граница
    for r in range(rows):
        dfs(r, cols - 1, atlantic, heights[r][cols - 1]) # Правая граница

    # Находим пересечение
    result = []
    for r in range(rows):
        for c in range(cols):
            if pacific[r][c] and atlantic[r][c]:
                result.append([r, c])
    
    return result


heights = eval(input())
print(pacificAtlantic(heights))