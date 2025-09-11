# https://leetcode.com/problems/longest-repeating-character-replacement/description/
# 424. Longest Repeating Character Replacement

def characterReplacement(s: str, k: int) -> int:
    
    n = len(s)
    
    freq_dict = dict()
    
    left = max_freq = max_len = 0
    
    for right in range(n):
        
        freq_dict[s[right]] = freq_dict.get(s[right], 0) + 1
        max_freq = max(max_freq, freq_dict[s[right]])
        
        if (right - left + 1) - max_freq > k:
            freq_dict[s[left]] -= 1
            left += 1
        
        max_len = max(max_len, right - left + 1)
         
            
            
    return max_len



s = input()
k = int(input())
print(characterReplacement(s, k))