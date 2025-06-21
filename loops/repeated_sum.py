# https://stepik.org/lesson/1430145/step/11?unit=1448507

def get_repeated_sum(n):
    
    while True:
        total_sum = 0 
        
        while n > 0:
            total_sum += n % 10
            n //= 10
            
        if total_sum < 10:
            return total_sum
        
        n = total_sum
    


n = int(input())
print(get_repeated_sum(n))