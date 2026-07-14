# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        prevnode = None
        prevprevnode = None
        currentnode = head

        while currentnode is not None:
            if prevnode is not None:
                prevnode.next = prevprevnode
            prevprevnode = prevnode
            prevnode = currentnode
            currentnode = currentnode.next
        
        prevnode.next = prevprevnode
        return prevnode