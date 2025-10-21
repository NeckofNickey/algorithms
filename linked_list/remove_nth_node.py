# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
# 19. Remove Nth Node From End of List

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
n = int(input())
head = build_linked_list(arr)

print_list(head)

def removeNthFromEnd(head, n):
        
        dummy = ListNode(0)
        dummy.next = head

        left, right = dummy, head

        for _ in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next

        return dummy.next

new_head = removeNthFromEnd(head, n)

print_list(new_head)