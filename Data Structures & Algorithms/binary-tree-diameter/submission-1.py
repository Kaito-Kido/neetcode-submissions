class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        nodeDiameter = {}

        def levelTree(node: Optional[TreeNode], nodeDiameter: dict) -> int:
            if node is None:
                return 0

            leftLevel = levelTree(node.left, nodeDiameter)
            rightLevel = levelTree(node.right, nodeDiameter)

            nodeDiameter[node.val] = leftLevel + rightLevel

            return 1 + max(leftLevel, rightLevel)

        if root is None:
            return 0

        rootLevel = levelTree(root.left, nodeDiameter) + \
                    levelTree(root.right, nodeDiameter)

        nodeDiameter[root.val] = rootLevel
        print(nodeDiameter)
        mx = 0
        for v in nodeDiameter.values():
            mx = max(mx, v)

        return mx