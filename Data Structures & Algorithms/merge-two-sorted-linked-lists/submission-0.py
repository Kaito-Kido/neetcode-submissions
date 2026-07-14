# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        mergedList = ListNode()
        cur = mergedList
        while list1 and list2:
            if list1.val <= list2.val:
                cur.val = list1.val
                list1 = list1.next
            else:
                cur.val = list2.val
                list2 = list2.next
            cur.next = ListNode()
            cur = cur.next
        
        if list1:
            cur.val = list1.val
            cur.next = list1.next
        if list2:
            cur.val = list2.val
            cur.next = list2.next

        
        return mergedList