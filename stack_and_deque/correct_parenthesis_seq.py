# https://informatics.msk.ru/mod/statements/view.php?id=206&chapterid=51#1
# Правильная скобочная последовательность

def get_correct_parenthesis_seq(line: str) -> str:
    
    if not line:
        return 'yes'
    
    stack = []
    
    bracket_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for bracket in line:
        if bracket in bracket_pairs.values():
            stack.append(bracket)
        elif bracket in bracket_pairs:
            if not stack or stack.pop() != bracket_pairs[bracket]:
                return 'no'
        else:
            return 'no'
    
    return 'no' if stack else 'yes'
            
    


line = input()
print(get_correct_parenthesis_seq(line))