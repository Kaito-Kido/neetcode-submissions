"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeMap = {}

        def dfs(node):
            if node is None:
                return None

            if node.val in nodeMap:
                return nodeMap[node.val]

            cloneNode = Node(node.val)
            nodeMap[node.val] = cloneNode

            for neighbor in node.neighbors:
                cloneNode.neighbors.append(
                    dfs(neighbor)
                )

            return cloneNode

        return dfs(node)