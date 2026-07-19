# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        result = ListNode()
        current = result

        for i in range(len(lists)):
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        
        while heap:
            _, index, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, index, node.next))
        
        return result.next

            

        

