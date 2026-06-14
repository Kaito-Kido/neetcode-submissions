class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r, c))

        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minute = -1
        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for dr, dc in direction:
                    newRow = dr + row
                    newCol = dc + col
                    if (
                        newRow < 0
                        or newCol < 0
                        or newRow >= len(grid)
                        or newCol >= len(grid[0])
                        or grid[newRow][newCol] != 1
                    ):
                        continue
                    grid[newRow][newCol] = 2
                    queue.append((newRow, newCol))
            minute += 1

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        return minute if minute != -1 else 0
