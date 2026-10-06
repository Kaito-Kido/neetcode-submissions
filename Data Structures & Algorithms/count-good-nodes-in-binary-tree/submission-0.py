# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# The values of the tree isn't unique?
# What are the constrains on the number of nodes?
# Can the tree be empty?
# Is the root node always good?

# Invariant
# Because the node is good if there is no node has value greater than x. 
# So we can bring the max value on the way, compare it to the current node when traveling using DFS

# Time complexity is O(V) with V is the verticle 
# Space complexity is O(V) in the worst case if the tree is highly skewed
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None: return 0
        goodNodeCount = 0
        maxSoFar = root.val
        def dfs(node, maxSoFar):
            nonlocal goodNodeCount
            if node.val >= maxSoFar:
                goodNodeCount += 1
                maxSoFar = node.val
            
            if node.left:
                dfs(node.left, maxSoFar)
            if node.right:
                dfs(node.right, maxSoFar)
        dfs(root, maxSoFar)
        return goodNodeCount

        