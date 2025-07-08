# https://informatics.msk.ru/mod/statements/view.php?id=81344#1

def get_min_ticket_purchase_time(time_list):
    
    if not time_list:
        return 0
    
    n = len(time_list)
    min_time_list = [0] * n
    
    for i in range(n):
        
        if i == 0:
            min_time_list[i] = time_list[i][0]
        elif i == 1:
            min_time_list[i] = min(
                min_time_list[i-1] + time_list[i][0],
                time_list[i-1][1]
            )
        elif i == 2:
            min_time_list[i] = min(
                min_time_list[i-1] + time_list[i][0],
                min_time_list[i-2] + time_list[i-1][1],
                time_list[i-2][2]
            )
        else:
            min_time_list[i] = min(
                min_time_list[i-1] + time_list[i][0],
                min_time_list[i-2] + time_list[i-1][1],
                min_time_list[i-3] + time_list[i-2][2]
            )
        
    return min_time_list[-1]
            
        


n = int(input())
time_list = [list(map(int, input().split())) for _ in range(n)]

print(get_min_ticket_purchase_time(time_list))
