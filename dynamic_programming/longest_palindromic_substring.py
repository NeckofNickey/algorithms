# https://leetcode.com/problems/longest-palindromic-substring/description/
# Longest Palindromic Substring

def longestPalindrome(s: str):
    
    n = len(s)
    if n <= 1:
        return s
    
    # dp[i][j] = True, если s[i:j+1] палиндром
    dp = [[False] * n for _ in range(n)]

    # Каждый символ сам по себе палиндром
    for i in range(n):
        dp[i][i] = True

    start, max_len = 0, 1

    # Проверяем пары одинаковых символов
    for i in range(n-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            start, max_len = i, 2

    # Проверяем подстроки длины 3 и больше
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                if length > max_len:
                    start, max_len = i, length
    
    return s[start:start + max_len]




s = input().strip()

print(longestPalindrome(s))