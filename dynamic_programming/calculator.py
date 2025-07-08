# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=2968#1

def get_min_operations(n):
    
    num_operations_list = [0] * (n + 1)
    
    for i in range(2, n + 1):
        variant_list = []
        if i % 3 == 0:
             variant_list.append(num_operations_list[i // 3])
        if i % 2 == 0:
            variant_list.append(num_operations_list[i // 2])
        
        variant_list.append(num_operations_list[i - 1])
        
        num_operations_list[i] = min(variant_list) + 1
    
    last_num = n
    operations_list = []
        
    while last_num > 1:
        if last_num % 3 == 0 and num_operations_list[last_num] == num_operations_list[last_num // 3] + 1:
            last_num //= 3
            operations_list.append(3)
        elif last_num % 2 == 0 and num_operations_list[last_num] == num_operations_list[last_num // 2] + 1:
            last_num //= 2
            operations_list.append(2)
        else:
            last_num -= 1
            operations_list.append(1)
        
    return operations_list[::-1]

n = int(input())
print(''.join(map(str, get_min_operations(n))))