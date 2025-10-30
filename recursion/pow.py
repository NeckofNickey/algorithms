# https://leetcode.com/problems/powx-n/description/
# 50. Pow(x, n)

def myPow(x: float, n: int) -> float:

        is_negative = n < 0

        n = abs(n)

        def pow(x, n):
            
            if n == 0:
                return 1

            half = pow(x, n // 2)  # ОДИН рекурсивный вызов
            if n % 2 == 0:
                return half * half
            else:
                return x * half * half
        
        new_x = pow(x, n)

        return 1 / new_x if is_negative else new_x


x = int(input())
n = int(input())

print(myPow(x, n))