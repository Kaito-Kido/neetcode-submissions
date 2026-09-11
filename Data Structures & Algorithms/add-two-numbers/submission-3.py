# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        remember = False
        while l1 and l2:
            sumval = l1.val + l2.val
            if remember: 
                sumval += 1
            if sumval >= 10:
                remember = True
                sumval -= 10
            else:
                remember = False
            head.next = ListNode(sumval)
            head = head.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val
            if remember:
                val += 1
            
            if val >= 10:
                remember = True
                val -= 10
            else:
                remember = False
            head.next = ListNode(val)
            head = head.next
            l1 = l1.next
        while l2:
            val = l2.val
            if remember:
                val += 1
            if val >= 10:
                val -= 10
                remember = True
            else:
                remember = False
            head.next = ListNode(val)
            head = head.next
            l2 = l2.next
        
        if remember:
            head.next = ListNode(1)
            head = head.next
        
        
        return dummy.next


            
