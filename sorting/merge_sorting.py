# https://new.contest.yandex.ru/contests/48569/problem?id=215%2F2023_04_06%2Fxwt1i1wLpb


def merge_sorting(unsorted_list):

    n = len(unsorted_list) 

    if n == 1:
        return unsorted_list

    first_half = unsorted_list[:n//2]
    second_half = unsorted_list[n//2:]
    
    sorted_first_half = merge_sorting(first_half)
    sorted_second_half = merge_sorting(second_half)
    
    sorted_list = get_merging_sorted_sequences(sorted_first_half, sorted_second_half)
    
    return sorted_list


def get_merging_sorted_sequences(list_1, list_2):
    
    sorted_list = []
    
    list_1_idx = 0
    list_2_idx = 0
    
    n_list_1 = len(list_1)
    n_list_2 = len(list_2)
    
    while list_1_idx < n_list_1 and list_2_idx < n_list_2:
        if list_1[list_1_idx] < list_2[list_2_idx]:
            sorted_list.append(list_1[list_1_idx])
            list_1_idx += 1
        else:
            sorted_list.append(list_2[list_2_idx])
            list_2_idx += 1
    
    # Добавляем оставшиеся элементы 
    sorted_list.extend(list_1[list_1_idx:])
    sorted_list.extend(list_2[list_2_idx:])
    
    return sorted_list


n = int(input())
unsorted_list = list(map(int, input().split()))

print(' '.join(map(str, merge_sorting(unsorted_list))))
