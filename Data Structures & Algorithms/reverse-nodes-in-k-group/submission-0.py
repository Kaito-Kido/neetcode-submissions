# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseGroup(head: Optional[ListNode], tail: Optional[ListNode]):
            prev = tail
            first = head.next
            index = 0
            while index < k:
                nextnode = first.next
                first.next = prev
                prev = first
                first = nextnode
                index += 1
            
            head.next = prev
        
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = None
        countpointer = head
        count = 0
        while countpointer != None and count < k:
            count += 1
            countpointer = countpointer.next

        while count == k:
            right = countpointer
            reverseGroup(left, right)

            for i in range(k):
                left = left.next
            countpointer = left.next
            count = 0
            while countpointer != None and count < k:
                count += 1
                countpointer = countpointer.next
        return dummy.next




