from typing import List

class Solution:
    def dfs(self, row, col, grid):
        if (
            row < 0 or row >= len(grid)
            or col < 0 or col >= len(grid[0])
            or grid[row][col] == 0
        ):
            return 0

        grid[row][col] = 0

        return 1 + (
            self.dfs(row + 1, col, grid)
            + self.dfs(row - 1, col, grid)
            + self.dfs(row, col + 1, grid)
            + self.dfs(row, col - 1, grid)
        )

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        max_area = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    max_area = max(max_area, self.dfs(row, col, grid))

        return max_area