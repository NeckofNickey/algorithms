# https://leetcode.com/problems/middle-of-the-linked-list/description/
# 876. Middle of the Linked List


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

print_list(head)


def middleNode(head):

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val

print(middleNode(head))
