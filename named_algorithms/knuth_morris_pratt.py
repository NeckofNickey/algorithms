# https://stepik.org/lesson/1489019/step/4?unit=1508913
# Алгоритм Кнута-Морриса-Пратта (KMP). Предназначен для эффективного поиска подстроки (шаблона) в строке.
# Основная идея состоит в том, что при обнаружении несовпадения он не пересматривает символы, которые уже были проверены, 
# а использует информацию о префиксах и суффиксах для правильного смещения шаблона. 
# Эта информация хранится в массиве LPS (Longest Prefix Suffix)
# https://www.youtube.com/watch?v=S2I0covkyMc

def compute_lps(pattern):
    """Вычисляет массив LPS (Longest Prefix Suffix) для шаблона."""
    n = len(pattern)
    lps = [0] * n
    i, j = 1, 0  # i - текущий символ, j - длина текущего префикса

    while i < n:
        if pattern[i] == pattern[j]:
            lps[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                lps[i] = 0
                i += 1
            else:
                j = lps[j - 1]
    return lps

def kmp_search(text, pattern):
    """Ищет все вхождения шаблона в тексте с помощью KMP. Возвращает индексы совпадений."""
    
    if not pattern or not text:
        return []

    m, n = len(text), len(pattern)
    lps = compute_lps(pattern)
    matches = []
    i = j = 0  # i - индекс в тексте, j - индекс в шаблоне

    while i < m:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == n:
                matches.append(i - j)
                j = lps[j - 1]
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
    return matches

# Пример использования
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(kmp_search(text, pattern))  # Вернёт [10]