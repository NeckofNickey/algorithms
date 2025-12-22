'''
Сколько существует восьмеричных шестизначных чисел, 
в которых все цифры различны, никакие две чётные или две нечётные цифры не стоят рядом и 
десятичная запись которых делится на 5?
'''

from itertools import permutations

digits = "01234567"
n = 6
even = set("0246")
odd = set("1357")

def is_valid(num, n):
    # не начинается с 0
    if num[0] == '0':
        return False
    # десятичная запись делится на 5
    if int(num, base=8) % 5 != 0:
        return False
    # чередование чет, нечет
    for i in range(5):
        curr_is_even = int(num[i]) % 2 == 0
        next_is_even = int(num[i+1]) % 2 == 0
        if (curr_is_even and next_is_even) or not (curr_is_even or next_is_even):
            return False

    return True

counter = 0
for num in permutations(digits, 6):
    num = ''.join(num)
    if is_valid(num, n):
        counter += 1

print(counter)
