# what are the constrains on k and the length of input nums?
# can the added value be null?
# do constructor nums neccessary to be larger than k?

# My approach here
# First come to my thought, i will use a max heap to store kth largest element
# add each add() operation, add the element to the heap and return the last element in the heap by heap[-1].
# Time complexity: build and operate on heap nlogn on init and O(logn) on adding new value to heap. Get the last element in heap is O(1) if using array to implement heap, i don't think we have another data structure to implement heap
# Space complexity: O(k) number of nums

# second approach sort every time we add new value, complexity nlogn on init and nlogn on every add
# space complexity O(n)



import heapq
from typing import List

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []

        for num in nums:
            self._insert(num)

    def _insert(self, val: int) -> None:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

    def add(self, val: int) -> int:
        self._insert(val)
        return self.heap[0]
