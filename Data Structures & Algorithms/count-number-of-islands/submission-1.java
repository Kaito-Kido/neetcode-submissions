class Solution {
    public int numIslands(char[][] grid) {
        int islandCount = 0;

        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {

                if (grid[i][j] == '1') {
                    islandCount++;
                    bfs(grid, i, j);
                }
            }
        }

        return islandCount;
    }

    public void bfs(char[][] grid, int i, int j) {
        Queue<Integer> queue = new LinkedList<>();
        grid[i][j] = 0;
        int cols = grid[0].length;
        int rows = grid.length;
        queue.add(i * cols + j);
        

        int[][] directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        while (!queue.isEmpty()) {
            int currentId = queue.poll();
            int r = currentId / cols;  // Khôi phục chỉ số hàng
            int c = currentId % cols;  // Khôi phục chỉ số cột

            for (int[] dir : directions) {
                int nextRow = r + dir[0];
                int nextCol = c + dir[1];

                // Kiểm tra điều kiện biên và xem có phải là đất chưa thăm hay không
                if (nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols && grid[nextRow][nextCol] == '1') {
                    // ĐÚNG THỜI ĐIỂM: Đánh dấu '0' ngay lập tức để các ô khác không add trùng nó nữa
                    grid[nextRow][nextCol] = '0';
                    queue.add(nextRow * cols + nextCol);
                }
            }
        }
    }
}
