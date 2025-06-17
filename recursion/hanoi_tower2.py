# https://new.contest.yandex.ru/contests/48568/problem?id=215%2F2023_04_06%2FNQ3L2sn9W8

import math

def get_hanoi_three_pegs_steps(n, source, aux, target, moves):
    
    if n == 1:
        moves.append(f'Переместить диск {n} c {source} на {target}')
        return
    
    get_hanoi_three_pegs_steps(n - 1, source, target, aux, moves)
    
    moves.append(f'Переместить диск {n} c {source} на {target}')
    
    get_hanoi_three_pegs_steps(n - 1, aux, source, target, moves)


def get_hanoi_four_pegs_steps(n, source, aux1, aux2, target, moves):
    
    if n == 0:
        return
    if n == 1:
        moves.append(f'Переместить диск 1 с {source} на {target}')
        return
    
    # Оптимальное k для 4 стержней (Frame-Stewart algorithm)
    k = n - round(math.sqrt(2 * n + 1)) + 1
    
    # Шаг 1: Переместить k верхних дисков с source на aux1, используя все 4 стержня
    get_hanoi_four_pegs_steps(k, source, aux2, target, aux1, moves)
    
    # Шаг 2: Переместить оставшиеся n-k дисков с source на target, используя 3 стержня (aux1 занят)
    get_hanoi_three_pegs_steps(n - k, source, aux2, target, moves)
    
    # Шаг 3: Переместить k дисков с aux1 на target, используя все 4 стержня
    get_hanoi_four_pegs_steps(k, aux1, source, aux2, target, moves)


def solve_hanoi_four_pegs(n):
    moves = []
    get_hanoi_four_pegs_steps(n, 1, 2, 3, 4, moves)
    print(f'Решение для {n} дисков:')
    for i, move in enumerate(moves, start=1):
        print(f'Шаг {i}: {move}')
    print(f'Общее количество перемещений: {len(moves)}')
    

n = int(input())
solve_hanoi_four_pegs(n)