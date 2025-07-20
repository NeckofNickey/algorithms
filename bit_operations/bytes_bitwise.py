# https://informatics.msk.ru/mod/statements/view.php?id=77938&chapterid=129#1
# Вывести значение байта побитно

def get_num(num):
    
    bitwise_num = []
    
    while num > 0:
        bitwise_num.append(num % 2)
        num //= 2
    
    return ''.join(map(str, bitwise_num[::-1])).rjust(8, '0')


num = int(input())
print(get_num(num))

# def get_num(num):
#     # Приводим число к 8-битному представлению, учитывая знак
#     byte = num & 0xFF
#     # Форматируем вывод в 8 бит с ведущими нулями
#     return f"{byte:08b}"

# num = int(input())
# print(get_num(num))