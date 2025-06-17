# https://informatics.msk.ru/mod/statements/view.php?id=86290&chapterid=112476#1

# def delete_repeats(s):
    
#     list_without_repeats = []
    
#     for letter in s:
#         if letter not in list_without_repeats:
#             list_without_repeats.append(letter)
            
#     return ''.join(list_without_repeats)


# def delete_repeats(s):
    
#     dict_str = {}
    
#     for letter in s:
#         if dict_str.get(letter, None):
#             continue
#         else:
#             dict_str[letter] = 1
            
#     return ''.join(dict_str.keys())

# def delete_repeats(s):
#     return ''.join(dict.fromkeys(s))


def delete_repeats(s):
    
    seen = set()
    unique_letters = []
    
    for letter in s:
        if letter not in seen:
            seen.add(letter)
            unique_letters.append(letter)
            
    return ''.join(unique_letters)


s = input().strip()
print(delete_repeats(s))

