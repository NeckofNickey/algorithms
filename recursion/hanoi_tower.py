# https://new.contest.yandex.ru/contests/48568/problem?id=215%2F2023_04_06%2FDEEgnJVwi3

def get_hanoi_tower_steps(n, from_peg, to_peg):
    
    if n == 1:
        print('Move disk from ', from_peg, ' to ', to_peg)
        return
    
    unused_peg = 6 - from_peg - to_peg
    
    get_hanoi_tower_steps(n - 1, from_peg, unused_peg)
    
    print('Move disk from ', from_peg, ' to ', to_peg)
    
    get_hanoi_tower_steps(n - 1, unused_peg, to_peg)
    
    
get_hanoi_tower_steps(3, 1, 3)

