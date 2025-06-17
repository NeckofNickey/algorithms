# https://informatics.msk.ru/mod/statements/view.php?id=85724&chapterid=512#1

def get_longest_thaw(n, temp_list):
    
    longest_thaw = 0
    current_thaw = 0
    
    for temp in temp_list:
        if temp > 0:
            current_thaw += 1
            if current_thaw > longest_thaw:
                longest_thaw = current_thaw
        else:
            current_thaw = 0
            
    return longest_thaw
        

n = int(input())
temp_list = list(map(int, input().strip().split()))
print(get_longest_thaw(n, temp_list))