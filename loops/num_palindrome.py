def get_num_palindrome(n):
    
    is_negative = n < 0
    n = abs(n)  
    
    if n == 0:
        return 0
    else:
        num_palindrome = 0
        orig_n = n
        while orig_n > 0:
            num_palindrome = num_palindrome * 10 + (orig_n % 10)
            orig_n //= 10
        
    return -num_palindrome if is_negative else num_palindrome

n = int(input())
print(get_num_palindrome(n))