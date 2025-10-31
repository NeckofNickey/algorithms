# https://leetcode.com/problems/search-a-2d-matrix/description/
# 74. Search a 2D Matrix

def searchMatrix(matrix, target) -> bool:
        
    if not matrix:
        return False
    
    m, n = len(matrix), len(matrix[0])

    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        i = mid // n
        j = mid % n
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return False



# matrix = eval(input())
# target = int(input())
matrix = eval("[[1,3,5,7],[10,11,16,20],[23,30,34,60]]")
target = 3

print(searchMatrix(matrix, target))