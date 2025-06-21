# https://stepik.org/lesson/1430145/step/10?unit=1448507

def is_prime_number(n):
    
    if n <= 1:
        print('Не простое')
    else:
        is_prime = True
        i = 2
        
        while i**2 <= n:
            
            if n % i == 0:
                is_prime = False
                break
            
            i += 1
        
        print('Простое' if is_prime else 'Не простое')


n = int(input())
print(is_prime_number(n))