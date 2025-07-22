# https://informatics.msk.ru/mod/statements/view.php?id=206&chapterid=50#1
# Игра в пьяницу

def get_game_result(cards1: list, cards2: list) -> tuple:
    
    counter = 0
    
    while cards1 and cards2:
        
        c1 = cards1.pop()
        c2 = cards2.pop()
        
        if c1 == 0 and c2 == 9:
            cards1[0:0] = [c2, c1]
        elif c2 == 0 and c1 == 9:
            cards2[0:0] = [c2, c1]
        elif c1 > c2:
            cards1[0:0] = [c2, c1]
        else:
            cards2[0:0] = [c2, c1]
        
        counter += 1
        
        if counter > 1e6:
            break
                
    if not cards1:
        return ('second', str(counter))
    elif not cards2:
        return ('first', str(counter))
    else:
        return ('botva',)



cards1 = list(map(int, input().split()))
cards2 = list(map(int, input().split()))

game_result = get_game_result(cards1, cards2)

print(' '.join(game_result))