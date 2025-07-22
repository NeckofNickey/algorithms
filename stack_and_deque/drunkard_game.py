# https://informatics.msk.ru/mod/statements/view.php?id=206&chapterid=50#1
# Игра в пьяницу

def get_game_result(cards1: list, cards2: list) -> tuple:
    
    counter = 0
    
    while cards1 and cards2:
        
        if counter >= 10**6:
            return ('botva', '')
        
        c1 = cards1.pop(0)
        c2 = cards2.pop(0)
        
        if (c1 == 0 and c2 == 9) or (c1 > c2 and not (c2 == 0 and c1 == 9)):
            cards1.extend([c1, c2])
        elif (c2 == 0 and c1 == 9) or (c2 > c1 and not (c1 == 0 and c2 == 9)):
            cards2.extend([c2, c1])
        
        counter += 1
        
                
    if not cards1:
        return ('second', str(counter))
    elif not cards2:
        return ('first', str(counter))
    else:
        return ('botva',)



cards1 = list(map(int, input().split()))
cards2 = list(map(int, input().split()))

# Получаем результат
winner, moves = get_game_result(cards1, cards2)

# Выводим результат
print(winner if winner == 'botva' else f"{winner} {moves}")