# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # prev1 = None
        # while l1:
        #     next1 = l1.next
        #     l1.next = prev1
        #     prev1 = l1
        #     l1 = next1
        
        # l1 = prev1
        
        # prev2 = None
        # while l2:
        #     next2 = l2.next
        #     l2.next = prev2
        #     prev2 = l2
        #     l2 = next2
        
        # l2 = prev2

        dummy = ListNode()
        head = dummy
        remember = False
        while l1 and l2:
            sumval = l1.val + l2.val
            print(sumval)
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
        
        # dummy = dummy.next
        # prev = None
        # while dummy:
        #     nextresult = dummy.next
        #     dummy.next = prev
        #     prev = dummy
        #     dummy = nextresult
        
        return dummy.next


            
