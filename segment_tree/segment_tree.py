# Реализация дерева отрезков


def build_segment_sum_tree(arr, v, st_left, st_right):
    if st_left == st_right:
        segment_sum_tree[v] = arr[st_left]
    else:
        st_mid = (st_left + st_right) // 2
        build_segment_sum_tree(arr, v * 2, st_left, st_mid)
        build_segment_sum_tree(arr, v * 2 + 1, st_mid + 1, st_right)
        segment_sum_tree[v] = segment_sum_tree[v*2] + segment_sum_tree[v*2 + 1]


def build_segment_min_tree(arr, v, st_left, st_right):
    if st_left == st_right:
        segment_min_tree[v] = arr[st_left]
    else:
        st_mid = (st_left + st_right) // 2
        build_segment_min_tree(arr, v * 2, st_left, st_mid)
        build_segment_min_tree(arr, v * 2 + 1, st_mid + 1, st_right)
        segment_min_tree[v] = min(segment_min_tree[v*2], segment_min_tree[v*2 + 1])


def get_segment_sum(v, st_left, st_right, l, r):
    if l > r:
        return 0
    if l == st_left and r == st_right:
        return segment_sum_tree[v]
    st_mid = (st_left + st_right) // 2
    left_sum = get_segment_sum(v * 2, st_left, st_mid, l, min(r, st_mid))
    right_sum = get_segment_sum(v * 2 + 1, st_mid + 1, st_right, max(l, st_mid + 1), r)
    return left_sum + right_sum


def get_segment_min(v, st_left, st_right, l, r):
    if l > r:
        return float('inf')
    if l == st_left and r == st_right:
        return segment_min_tree[v]
    st_mid = (st_left + st_right) // 2
    left_min = get_segment_min(v * 2, st_left, st_mid, l, min(r, st_mid))
    right_min = get_segment_min(v * 2 + 1, st_mid + 1, st_right, max(l, st_mid + 1), r)
    return min(left_min, right_min)


def update_segment_sum_tree(v, st_left, st_right, pos, new_val):
    if st_left == st_right:
        segment_sum_tree[v] = new_val
    else:
        st_mid = (st_left + st_right) // 2
        if pos <= st_mid:
            update_segment_sum_tree(v * 2, st_left, st_mid, pos, new_val)
        else:
            update_segment_sum_tree(v * 2 + 1, st_mid + 1, st_right, pos, new_val)
        segment_sum_tree[v] = segment_sum_tree[v * 2] + segment_sum_tree[v * 2 + 1]


def update_segment_min_tree(v, st_left, st_right, pos, new_val):
    if st_left == st_right:
        segment_min_tree[v] = new_val
    else:
        st_mid = (st_left + st_right) // 2
        if pos <= st_mid:
            update_segment_min_tree(v * 2, st_left, st_mid, pos, new_val)
        else:
            update_segment_min_tree(v * 2 + 1, st_mid + 1, st_right, pos, new_val)
        segment_min_tree[v] = min(segment_min_tree[v * 2], segment_min_tree[v * 2 + 1])
           

arr = [1, 1, 2, 3, 1, 1, 4, 2]
n = len(arr)
segment_sum_tree = [0] * (n * 4)
segment_min_tree = [float('inf')] * (n * 4)
# Строим дерево суммы
build_segment_sum_tree(arr, 1, 0, n - 1)
print(segment_sum_tree)
print(get_segment_sum(1, 0, n - 1, 0, 5))
# Обновляем дерево суммы
update_segment_sum_tree(1, 0, n - 1, 0, 3)
print(segment_sum_tree)
# Получение суммы
print(get_segment_sum(1, 0, n - 1, 0, 5))
# Строим дерево минимумов
build_segment_min_tree(arr, 1, 0, n - 1)
print(segment_min_tree)
print(get_segment_min(1, 0, n - 1, 0, 5))
# Обновляем дерево минимумов
update_segment_min_tree(1, 0, n - 1, 1, 0)
print(segment_min_tree)
# Получаем минимум
print(get_segment_min(1, 0, n - 1, 0, 5))
