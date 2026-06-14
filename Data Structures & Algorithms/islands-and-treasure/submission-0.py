class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        INF = 2147483647
        n = len(grid)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    queue.append((r, c))
        level = 0
        direction = [[-1, 0],[1, 0],[0, 1],[0, -1]]
        while queue:
            level += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in direction:
                    newRow = row + dr
                    newCol = col + dc

                    if newRow < 0 or newCol < 0 or newRow >= n or newCol >= len(grid[0]) or grid[newRow][newCol] == -1 or grid[newRow][newCol] != INF:
                        continue
                    grid[newRow][newCol] = level
                    queue.append((newRow, newCol))
                
        return