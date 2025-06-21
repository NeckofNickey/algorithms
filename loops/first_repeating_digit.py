# https://stepik.org/lesson/1430145/step/12?unit=1448507

def get_first_repeating_digit(n):
    
    if n < 10:
        return 'Нет повторяющихся цифр'
    
    # Считаем количество цифр в числе
    num_length = 0
    temp_n = n
    while temp_n > 0:
       num_length += 1
       temp_n //= 10
    
    # Проверяем цифры слева направо   
    for i in range(num_length - 1):
        # Извлекаем текущую цифру (слева)
        current_digit = (n // (10 ** (num_length - 1 - i))) % 10
        # Проверяем оставшиеся цифры справа от неё
        for j in range(i + 1, num_length):
            next_digit = (n // (10 ** (num_length - 1 - j))) % 10
            if current_digit == next_digit:
                return current_digit

    return 'Нет повторяющихся цифр'
            

n = int(input())
print(get_first_repeating_digit(n))