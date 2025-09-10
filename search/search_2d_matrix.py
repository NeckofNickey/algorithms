# https://leetcode.com/problems/search-a-2d-matrix/description/
# Search a 2D Matrix


def searchMatrix(matrix, target: int) -> bool:
    
    if not matrix: return False
    
    m, n = len(matrix), len(matrix[0])
    
    top, bottom = 0, m - 1
    
    while top <= bottom:
        mid_row = (top + bottom) // 2
        if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
            left, right = 0, n - 1
            while left <= right:
                mid_col = (left + right) // 2
                if matrix[mid_row][mid_col] == target:
                    return True
                elif matrix[mid_row][mid_col] < target:
                    left = mid_col + 1
                else:
                    right = mid_col - 1
            return False
        elif matrix[mid_row][0] > target:
            bottom = mid_row - 1
        else:
            top = mid_row + 1
 
    return False
            

matrix = eval(input())
target = int(input())
print(searchMatrix(matrix, target))