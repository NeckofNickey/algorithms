# https://new.contest.yandex.ru/contests/80784/problem?id=149944%2F2025_08_30%2F0psuPDpNE3
# Выполнение операций со списком

import sys

class ListNode():
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def append_node(linked_list, pos, val):
    if not val or not linked_list:
        return None
    
    current = linked_list

    for i in range(pos):
        current = current.next
    
    if current.next:
        temp_node = current.next
        current.next = ListNode(val=val, next=temp_node)
    else:
        current.next = ListNode(val)

    return linked_list

def get_val(linked_list, pos):

    if not linked_list:
        return None
    
    current = linked_list

    for i in range(pos):
        current = current.next

    return current.val

def del_node(linked_list, pos):
    if not linked_list:
        return None
    
    current = linked_list

    for _ in range(pos - 1):
        current = current.next

    current.next = current.next.next

    return linked_list


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    
    print("None")


data = list(map(int, sys.stdin.read().split()))

n = data[0]

idx = 1

linked_list = ListNode()

for _ in range(n):
    if data[idx] == 1:
        x, y = data[idx+1], data[idx+2]
        linked_list = append_node(linked_list, x, y)
        idx += 3
    elif data[idx] == 2:
        pos = data[idx+1]
        print(get_val(linked_list, pos))
        idx += 2
    elif data[idx] == 3:
        pos = data[idx+1]
        linked_list = del_node(linked_list, pos)
        idx += 2


print_list(linked_list)