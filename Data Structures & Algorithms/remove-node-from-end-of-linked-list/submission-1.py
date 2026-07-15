# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyHead = ListNode()
        dummyHead.next = head
        tail = dummyHead

        for i in range(n):
            tail = tail.next

        pointer = dummyHead
        while tail.next:
            pointer = pointer.next
            tail = tail.next

        pointer.next = pointer.next.next
        return dummyHead.next