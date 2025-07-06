# https://informatics.msk.ru/mod/statements/view.php?id=654&chapterid=912#1

def get_num_of_seq(n):
    
    zeros_list = [0] * n
    ones_list = [0] * n
    one_one_list = [0] * n
    
    zeros_list[0] = 1
    ones_list[0] = 1
    one_one_list[0] = 0
    
    for i in range(1, n):
        zeros_list[i] = zeros_list[i - 1] + ones_list[i - 1] + one_one_list[i - 1]
        ones_list[i] = zeros_list[i - 1]
        one_one_list[i] = ones_list[i - 1]
        
        
    return zeros_list[n - 1] + ones_list[n - 1] + one_one_list[n - 1]


n = int(input())
print(get_num_of_seq(n))