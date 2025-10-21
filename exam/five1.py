''' На вход алгоритма подается натуральное число N. 
Алгоритм строит по нему новое число следующим образом:

1. Строится двоичная запись числа N
2. К этой записи дописывается справа бит чётности: 0, если в 
двоичном коде числа N было чётное число единиц, и 1, если нечётное.
3. Полученное число переводится в десятичную систему счисления.
Какое число получится, если на вход было подано число 19? '''

def decimal_to_binary(num):

    if num == 0:
        return "0"
    
    result = ""
    num = abs(num)
    
    while num > 0:
        result = str(num % 2) + result
        num //= 2

    return result if num >= 0 else "-" + result


def reverse_str(s):
    chars = list(s)
    left, right = 0, len(s) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return ''.join(chars)


def binary_to_decimal(binary_str):
    result = 0
    power = 0

    reverse_binary_str = reverse_str(binary_str)

    for digit in reverse_binary_str:
        if digit == "1":
            result += 2 ** power
        power += 1
    
    return result


def parity_bit(num):

    count = 0

    while num:
        count += num & 1
        num >>= 1

    return count % 2 == 0


n = 19
# n_bin = decimal_to_binary(n)
n_bin = bin(n)[2:]

if parity_bit(n):
    n_bin += "0"
else:
    n_bin += "1"

# print(binary_to_decimal(n_bin))
print(int(n_bin, 2))


