# https://informatics.msk.ru/mod/statements/view.php?id=85724&chapterid=1437#1

# def get_lost_card(n, cards):
    
#     for num in range(1, n + 1):
#         if num not in cards:
#             return num
    
#     return 0

# def get_lost_card(n, cards):
#     total_sum = n * (n + 1) // 2
#     current_sum = 0
#     for num in cards:
#         current_sum += num
#     return total_sum - current_sum

def get_lost_card(n, cards):
    
    total_sum = n * (n + 1) // 2
    cards_sum = sum(cards)
    
    return total_sum - cards_sum

seq = list(map(int, input().strip().split()))
n = seq[0]
cards = seq[1:]

print(get_lost_card(n, cards))