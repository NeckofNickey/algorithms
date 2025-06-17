# https://new.contest.yandex.ru/contests/48569/problem?id=215%2F2023_04_06%2FRRehKswGis

def get_merging_sorted_sequences(list_1, list_2):
    
    list1 = [x for x in list_1]
    list2 = [x for x in list_2]
    
    sorted_list = []
    
    list1_idx = list2_idx = 0
    len_list1 = len(list1)
    len_list2 = len(list2)
    
    while list1_idx < len_list1 and list2_idx < len_list2:
        if list1[list1_idx] < list2[list2_idx]:
            sorted_list.append(list1[list1_idx])
            list1_idx += 1
        else:
            sorted_list.append(list2[list2_idx])
            list2_idx += 1
            
    # Добавляем оставшиеся элементы         
    sorted_list.extend(list1[list1_idx:])
    sorted_list.extend(list2[list2_idx:])
        
    return sorted_list

def merge_sorted_sequences(sequences):
    
    if not sequences:
        return []
    
    # Инициализируем результат первым списком
    result = sequences[0]
    
    # Последовательно сливаем со всеми остальными списками
    for seq in sequences[1:]:
        result = get_merging_sorted_sequences(result, seq)
        
    return result


n = int(input())
sequences_list = []

for i in range(n):
    seq_n = int(input())
    sequences_list.append(list(map(int, input().split())))
    
print(' '.join(map(str, merge_sorted_sequences(sequences_list))))
    