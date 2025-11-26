# https://leetcode.com/problems/min-cost-to-connect-all-points/description/
# 1584. Min Cost to Connect All Points

import heapq

def min_cost_connect_points_prime(points):

    ''' Алгоритм Прима '''
    
    n = len(points)
    if n == 1:
        return 0
    
    def get_manhattan_dist(x, y):
        return abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
    

    visited = [False] * n
    heap = [(0, 0)] # (cost, node)
    total_cost = 0
    edges_used = 0

    while edges_used < n:
        cost, node = heapq.heappop(heap)

        if visited[node]:
            continue

        visited[node] = True
        total_cost += cost
        edges_used += 1

        for neighbour in range(n):
            if not visited[neighbour]:
                heapq.heappush(heap, (get_manhattan_dist(node, neighbour), neighbour))

    return total_cost


def min_cost_connect_points_kruskal(points):

    ''' Алгоритм Краскала '''

    n = len(points)
    if n == 1:
        return 0
    
    def get_manhattan_dist(x, y):
        return abs(points[x][0] - points[y][0]) + abs(points[x][1] - points[y][1])
    
    # Строим полносвязный граф
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            edges.append((get_manhattan_dist(i, j), i, j))

    
    # Реализация алгоритма Краскала
    sorted_edges = sorted(edges, key=lambda x: x[0])
    vertex_groups = {}
    ostov_edges = []

    # Функция для поиска группы вершины
    def find_group(vertex):
        if vertex not in vertex_groups:
            vertex_groups[vertex] = {vertex}  # Создаем новую группу
        return vertex_groups[vertex]
    
    # Функция для объединения групп
    def union_groups(group1, group2):
        # Объединяем группы
        new_group = group1.union(group2)
        # Обновляем ссылки для всех вершин в объединенной группе
        for vertex in new_group:
            vertex_groups[vertex] = new_group
        return new_group

    # Основной цикл алгоритма Краскала
    for cost, u, v in sorted_edges:
        group_u = find_group(u)
        group_v = find_group(v)
        
        # Если вершины в разных группах - добавляем ребро
        if group_u != group_v:
            ostov_edges.append((cost, u, v))
            union_groups(group_u, group_v)
        
        # Если построили MST (n-1 ребро), выходим
        if len(ostov_edges) == n - 1:
            break

    total_cost = sum([x[0] for x in ostov_edges])
    return total_cost



points = eval(input())

print(min_cost_connect_points_prime(points))
print(min_cost_connect_points_kruskal(points))