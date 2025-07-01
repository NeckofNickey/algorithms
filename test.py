line = input('Введите строку: ')

punctuation = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
cleaned_line = ''.join(char if char not in punctuation else ' ' for char in line)

words = cleaned_line.split()

if not words:
    print("Введена пустая строка")
else:
    num_words = len(words)
    total_length = sum(len(word) for word in words)
    avg_length = total_length / num_words
    
    print(f'Количество слов: {num_words}')
    print(f'Средняя длина слова: {avg_length}')