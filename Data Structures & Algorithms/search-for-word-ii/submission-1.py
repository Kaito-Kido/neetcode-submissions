# Clarification
# What are the constraints on the number of words?
# What are the contraints on the width and height of the grid?
# Does the word and the board contain uppercase letter or lowercase only?

# Brute Force approach
# From a cell on the board, we can use BFS to go 4 direction and if it matches the currentword
# Do the same for each word
# We can early return if the formed word on the path doesn't match the current word and jump to the next cell.

# Time complexity for this: BFS would cost m*n for each cell, so it't would be (m*n)^2 * O(N * k) with m, n is the width and height of the board, and N is the number of word. in worst case
# Space complexity is O(m*n) when using queue to travel.

# optimize approach:
# I think we can build a trie from the words array.
# also use BFS to travel at each cell, if the current cell match a node on the trie, continue to find the next cell in four direction
# if we can go to the end of the trie, return the word
# if it doesn't match anymore, return soon
# Time complexity is (m*n)^2 + O(N * k) với N là number ò word and k là độ dài trung bình mỗi word
# space complexity is (m + n) (đươngf chéo khi travel bằng bfs) + D với d là số từ distinct 

class Solution:
    class TrieNode:
        def __init__(self):
            self.children = {}
            self.word = None

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.TrieNode() 
        for word in words:
            currentNode = root
            for w in word:
                if w not in currentNode.children:
                    currentNode.children[w] = self.TrieNode()

                currentNode = currentNode.children[w]
            currentNode.word = word
        

        def dfs(row, col, root, visited, result, board):
            rowlength = len(board)
            collength = len(board[0])
            if row >= rowlength or row < 0 or col >= collength or col < 0:
                return
            if (row, col) in visited:
                return

            c = board[row][col]
            if c not in root.children:
                return
            childrenNode = root.children[c]
            if childrenNode.word is not None:
                result.append(childrenNode.word)
                childrenNode.word = None
            visited.add((row, col))
            dfs(row + 1, col, childrenNode,  visited, result, board)
            dfs(row, col + 1, childrenNode, visited, result, board)
            dfs(row - 1, col, childrenNode, visited, result, board)
            dfs(row, col - 1, childrenNode, visited, result, board)
            visited.remove((row, col))
        
        result = []
        for row in range(len(board)):
            for col in range(len(board[0])):
                dfs(row, col, root, set(), result, board)
        return result


        

                

                

                    
        
        








