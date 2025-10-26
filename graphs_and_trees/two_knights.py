# https://informatics.msk.ru/mod/statements/view.php?id=255&chapterid=163#1
# Два коня

from collections import deque

def chess_to_coord(pos):
    """Преобразует шахматную нотацию в координаты (0..7)"""
    col = ord(pos[0]) - ord('a')
    row = int(pos[1]) - 1
    return row, col


def get_knight_moves(r, c):
    """Возвращает все возможные ходы коня из позиции (r, c)"""
    moves = []
    for dr, dc in [(-2,-1),(-2,1),(-1,-2),(-1,2),
                   (1,-2),(1,2),(2,-1),(2,1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 8 and 0 <= nc < 8:
            moves.append((nr, nc))
    return moves


def min_meeting_moves(red_pos, green_pos):
    # Преобразуем координаты
    red_start = chess_to_coord(red_pos)
    green_start = chess_to_coord(green_pos)

    # Если уже на одной клетке
    if red_start == green_start:
        return 0
    
    # BFS: (pos_red, pos_green, moves)
    queue = deque([(red_start, green_start, 0)])
    visited = set([red_start, green_start])

    while queue:
        pos_red, pos_green, moves = queue.popleft()

        # Все возможные ходы для красного коня
        for next_red in get_knight_moves(*pos_red):
            # Все возможные ходы для зеленого коня
            for next_green in get_knight_moves(*pos_green):
                # Проверяем встречу
                if next_red == next_green:
                    return moves + 1
                
                # Проверяем, не были ли в этом состоянии
                state = (next_red, next_green)
                if state not in visited:
                    visited.add(state)
                    queue.append((next_red, next_green, moves + 1))

    return -1

red_pos, green_pos = tuple(input().split())
print(min_meeting_moves(red_pos, green_pos))