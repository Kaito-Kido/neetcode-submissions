class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        edgeregion = "E"
        queue = deque()
        for r in range(m):
            for c in range(n):
                if (r == 0 or c == 0 or r == m - 1 or c == n - 1) and board[r][c] == "O":
                    queue.append((r, c))
                    board[r][c] = edgeregion
                        
        
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            r, c = queue.popleft()
            
            for dr, dc in direction:
                newRow = r + dr
                newCol = c + dc
                if newRow >= m or newCol >= n or newRow < 0 or newCol < 0 or board[newRow][newCol] != "O":
                    continue
                
                board[newRow][newCol] = edgeregion
                queue.append((newRow, newCol))
                
        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"
        
        return