"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Constraint: 0 <= n <= 100
        # Result: 0 <= len(result) <= 200
        # Initial approach
        # Interate through linkedlist and deep copy first n node, only follow next pointer,
        # Save each node using a hash map with key is the index of that node and value is the node
        # Integrate though linedlist again and point the random pointer to the following node saved in the hashmap

        node_by_index = {}

        pointer = head
        dummy = Node(0)
        result = dummy
    
        while pointer:
            newnode = Node(pointer.val)
            result.next = newnode
            result = result.next
            # print(pointer.val, pointer.random)
            # print(result.val, result.random)
            node_by_index[pointer] = result
            pointer = pointer.next

        pointer = head
        result = dummy.next
        while pointer:
            if pointer.random:
                result.random = node_by_index[pointer.random]
            pointer = pointer.next
            result = result.next

        return dummy.next



