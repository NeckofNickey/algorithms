# https://stepik.org/lesson/1483973/step/15?thread=solutions&unit=1503701
# Проверяется, является ли строка "почти палиндромом"

def is_almost_palindrome(s: str) -> bool:
    
    def is_palindrome(s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
            
        return True
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            # Проверяем возможность удаления левого или правого символа
            return is_palindrome(s, left + 1, right) or is_palindrome(s, left, right - 1)
        left += 1
        right -=1
        
    return True


line = input().replace('"', '')
print(is_almost_palindrome(line))