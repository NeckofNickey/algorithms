'''
Даша составляет 7-буквенные слова из букв БАНДЕРОЛЬ. 
Мягкий знак используется в каждом слове не больше одного раза. 
Остальные буквы могут быть использованы сколько угодно раз или не использоваться совсем.

Сколько слов может составить Даша, если известно, 
что буква Е не может стоять рядом с согласными?
'''

from itertools import product
 
alphabet = 'БАНДЕРОЛЬ'
consonants = set('БНДРЛ')

def is_valid(word):
    # Условие 1: мягкий знак не больше одного раза
    if word.count('Ь') > 1:
        return False
    # Условие 2: Е не соседствует с согласными
    n = len(word)
    for i in range(n):
        if word[i] == 'Е':
            # Проверяем левого соседа
            if i > 0 and word[i - 1] in consonants:
                return False
            # Проверяем правого соседа
            if i < n - 1 and word[i + 1] in consonants:
                return False
    
    return True

count = 0
for comb in product(alphabet, repeat=7):
    if is_valid(comb):
        count += 1

print(count)
