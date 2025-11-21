# https://leetcode.com/problems/course-schedule-iv/description/
# Course Schedule IV

def checkIfPrerequisite(numCourses, prerequisites, queries):

    # Создаем матрицу достижимости    
    reachable = [[False] * numCourses for _ in range(numCourses)]

    # Инициализируем прямые связи из prerequisites
    for a, b in prerequisites:
        reachable[a][b] = True

    # Алгоритм Флойда-Уоршелла для транзитивного замыкания
    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                if reachable[i][k] and reachable[k][j]:
                    reachable[i][j] = True


    result = []
    for u, v in queries:
        result.append(reachable[u][v])

    return result


numCourses = int(input())
prerequisites = eval(input())
queries = eval(input())

print(checkIfPrerequisite(numCourses, prerequisites, queries))