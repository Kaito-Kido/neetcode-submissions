# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Can root input root node be none?
# So if the root node is none? would it be considered balanced? 
# Is values of the tree unique? 
# Do we have maximum number of nodes?
# If the tree has only one node will it be considered balance?

# Approach 1: Use DFS to travel all the tree from the left node of the root, and do the same to the right node to calculate the maximum height of each left branch and right branch, compare it.
# The time complexity of this approach is O(n) with n is the number of nodes.
# Space complexity is the maximum height of the tree, if the tree is hightly skewed (worst case), it's O(n)

# Approach 2: use BFS to travel to each level of the tree, keep track of number of nodes of each level of the branch. return the result if number of nodes of either branches is zero, else return true.
# Time complexity O(n)
# space complexity O(2^m) m is the deepest level of the tree.

# Invariant, haven't figured it out :)) yet

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node):
            if node is None:
                return 0
            
            leftheight = height(node.left)
            if leftheight == -1:
                return -1

            rightheight = height(node.right)
            if rightheight == -1:
                return -1
            
            if abs(leftheight - rightheight) <= 1:
                return max(leftheight, rightheight) + 1
            else:
                return -1
        
        if height(root) >= 0:
            return True
        else:
            return False
        







        