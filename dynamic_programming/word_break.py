# https://leetcode.com/problems/word-break/description/
# Word Break

def wordBreak(s: str, wordDict) -> bool:
    
    n = len(s)
    
    dp = [False] * (n + 1)
    dp[0] = True
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i] = True
                break
    
    return dp[-1]


s = input()
wordDict = eval(input())

print(wordBreak(s, wordDict))