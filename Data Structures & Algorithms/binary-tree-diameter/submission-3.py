class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        best = 0
        def height(node):
            nonlocal best
            if node is None:
                return 0
            l = height(node.left)
            r = height(node.right)
            best = max(best, l + r)      # carry-up: trả height, CHỐT best tại đây
            return 1 + max(l, r)
        height(root)
        return best