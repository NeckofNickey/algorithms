# https://leetcode.com/problems/reverse-linked-list/description/
# 206. Reverse Linked List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(arr):
    if not arr:
        return None
    

    head = ListNode(arr[0])
    current = head

    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return head


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    
    print("None")


arr = eval(input())
head = build_linked_list(arr)


def reverseList(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev


reverseList(head)