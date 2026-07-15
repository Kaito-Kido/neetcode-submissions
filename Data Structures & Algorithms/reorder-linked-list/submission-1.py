# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pointer = head
        numnode = 0
        while pointer:
            numnode += 1
            pointer = pointer.next
        
        if numnode <= 2:
            return
        
        secondhalf = numnode // 2 + 1
        counter = 0
        headsecond = None
        pointer = head
        while pointer:
            if counter == secondhalf - 1:
                headsecond = pointer.next
                pointer.next = None
                break
            counter += 1
            pointer = pointer.next
        
        prev = None
        while headsecond:
            temp = headsecond.next
            headsecond.next = prev
            prev = headsecond
            headsecond = temp
        
        head2 = prev

        pointer = head
        while pointer.next and head2:
            temp2 = head2
            head2 = head2.next

            temp2.next = pointer.next
            pointer.next = temp2
            pointer = temp2.next
    
