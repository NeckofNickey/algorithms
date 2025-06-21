# https://stepik.org/lesson/1430144/step/16?unit=1448506

def get_all_num_palindrome_from_seq(n):
    
    if n <= 0:
        print('Число должно быть положительным')
    else:
        for num in range(1, n + 1):
            if num % 10 == 0:
                continue
            else:
                reverse_num = 0
                orig_num = num
                
                while orig_num > 0:
                    reverse_num = reverse_num * 10 + (orig_num % 10)
                    orig_num //= 10
                
                if reverse_num == num:
                    print(num)
    


n = int(input())
get_all_num_palindrome_from_seq(n)
