# https://informatics.mccme.ru/mod/statements/view.php?chapterid=111253#1
# histogram


def get_largest_rectangle_area(n, heights):
    
    stack = []  # стек хранит индексы в возрастающем порядке высот
    max_area = 0
    
    for i in range(n):
        # Пока текущий элемент меньше последнего в стеке
        while stack and heights[i] < heights[stack[-1]]:
            height = heights[stack.pop()]
            # Ширина = текущий индекс - новый верх стека - 1
            # Если стек пуст, значит это минимальный элемент
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    # Обработка оставшихся элементов в стеке
    while stack:
        height = heights[stack.pop()]
        width = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, height * width)
    
    return max_area


data = list(map(int, input().split()))
n = data[0]
heights = data[1:]
print(get_largest_rectangle_area(n, heights))