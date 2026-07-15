# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer1 = head
        pointer2 = head
        counter = 0
        while pointer1 and pointer2:
            if pointer1 == pointer2:
                counter += 1
            if counter == 2:
                return True
            pointer1 = pointer1.next
            if pointer2.next:
                pointer2 = pointer2.next.next
            else:
                pointer2 = pointer2.next
        
        return False