# https://new.contest.yandex.ru/contests/48569/problem?id=215%2F2023_04_06%2F08fmDTMXQZ

def selection_sort(num_list):

    copy_num_list = [x for x in num_list]

    for i in range(len(copy_num_list)):

        min_index = i

        for j in range(i + 1, len(copy_num_list)):
            if copy_num_list[j] < copy_num_list[min_index]:
                min_index = j
                
        if i != min_index:
            copy_num_list[i], copy_num_list[min_index] = copy_num_list[min_index], copy_num_list[i]

    return copy_num_list
        


n = int(input())
num_list = list(map(int, input().split()))

print(' '.join(map(str, selection_sort(num_list))))