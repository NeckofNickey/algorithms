# https://informatics.msk.ru/mod/statements/view.php?id=81344&chapterid=515#1
# Словарь

import sys

def get_correct_text(text, dictionary):
    
    # Динамическое программирование
    # dp[i] = (можно ли разбить префикс длины i, предыдущее слово)
    m = len(text)
    dp = [None] * (m + 1)
    dp[0] = (-1, "")

    for i in range(m + 1):
        if dp[i] is None:
            continue

        # Пробуем все возможные слова, начинающиеся с позиции i
        for word in dictionary:
            j = i + len(word)
            if j <= m:
                if text[i:j] == word:
                    dp[j] = (i, word) # Сохраняем откуда пришли и какое слово

    # Восстанавливаем разбиение
    result = []
    pos = m
    while pos > 0:
        prev_pos, word = dp[pos]
        result.append(word)
        pos = prev_pos

    result.reverse()
    
    return " ".join(result)


data = sys.stdin.read().split()
text = data[0]
n = int(data[1])
dictionary = set(map(lambda x: x.strip(), data[2:]))

correct_text = get_correct_text(text, dictionary)

print(correct_text)