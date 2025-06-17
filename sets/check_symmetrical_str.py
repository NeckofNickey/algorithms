# https://miro.com/app/board/uXjVItCwSIo=/

def check_symmetrical_str(s):
    
    if not s:
        return 'NO'
    
    set_str_len = len(set(s))
    
    left_set = set()
    
    index = None
    
    for i in range(0, len(s)):
        left_set.add(s[i])
        if len(left_set) == set_str_len:
            index = i
            break
        
    right_set = set(s[index + 1:])
    
    if len(right_set) == set_str_len:
        return 'YES'
    else:
        return 'NO'

s = input().strip()

print(check_symmetrical_str(s))
