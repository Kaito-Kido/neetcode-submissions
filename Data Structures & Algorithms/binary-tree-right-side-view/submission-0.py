# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Clarify:
# can this tree be empty, and if so, should i return an empty array
# May i confirm that a node is seen from right side means it is the right most at that level
# Are there any constraints on the number of nodes?
# Can this tree be highly skewed
# Does the values matter or is this purely about tree structure 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = deque()
        queue.append(root)
        result = []

        while queue:
            numberofnodes = len(queue)
            result.append(queue[-1].val)

            for i in range(0, numberofnodes):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        
        return result



