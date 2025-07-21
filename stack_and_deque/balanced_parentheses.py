# https://stepik.org/lesson/1483973/step/14?unit=1503701
# Сбалансированные скобки

def is_balanced_parentheses(s: str) -> bool:
    
    s = s.replace(' ', '')
    
    if not s:
        return True
    
    stack = []
    
    brackets_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for bracket in s:
        if bracket in brackets_pairs.values():
            stack.append(bracket)
        elif bracket in brackets_pairs:
            if not stack or stack.pop() != brackets_pairs[bracket]:
                return False
        else:
            return False

            
    return not stack
    
    

seq = input()
print(is_balanced_parentheses(seq))