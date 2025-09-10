# https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Evaluate Reverse Polish Notation


def evalRPN(tokens) -> int:
        
    stack = []

    for token in tokens:

        if token not in '+-*/':
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))

    return stack.pop()


tokens = eval(input())
print(evalRPN(tokens))