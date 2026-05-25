class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> result = new ArrayList<>();
        if (heights == null || heights.length == 0 || heights[0].length == 0) {
            return result;
        }

        int rows = heights.length;
        int cols = heights[0].length;

        // 2 mảng trạng thái độc lập
        boolean[][] canReachPacific = new boolean[rows][cols];
        boolean[][] canReachAtlantic = new boolean[rows][cols];

        // 2 Queue đa nguồn (Multi-source) cho 2 đại dương
        Queue<int[]> pacificQueue = new LinkedList<>();
        Queue<int[]> atlanticQueue = new LinkedList<>();

        // Bước 1: Duyệt biên hàng ngang (Hàng đầu & Hàng cuối)
        for (int c = 0; c < cols; c++) {
            // Biên Thái Bình Dương (Hàng top)
            canReachPacific[0][c] = true;
            pacificQueue.add(new int[]{0, c});

            // Biên Đại Tây Dương (Hàng bottom)
            canReachAtlantic[rows - 1][c] = true;
            atlanticQueue.add(new int[]{rows - 1, c});
        }

        // Bước 2: Duyệt biên hàng dọc (Cột đầu & Cột cuối)
        for (int r = 0; r < rows; r++) {
            // Biên Thái Bình Dương (Cột left)
            if (!canReachPacific[r][0]) { // Tránh add trùng ô góc (0,0)
                canReachPacific[r][0] = true;
                pacificQueue.add(new int[]{r, 0});
            }

            // Biên Đại Tây Dương (Cột right)
            if (!canReachAtlantic[r][cols - 1]) { // Tránh add trùng ô góc (rows-1, cols-1)
                canReachAtlantic[r][cols - 1] = true;
                atlanticQueue.add(new int[]{r, cols - 1});
            }
        }

        // Bước 3: Chỉ gọi BFS đúng 2 lần duy nhất cho 2 đại dương
        bfs(heights, pacificQueue, canReachPacific);
        bfs(heights, atlanticQueue, canReachAtlantic);

        // Bước 4: Tổng hợp kết quả giao thoa
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (canReachPacific[r][c] && canReachAtlantic[r][c]) {
                    result.add(List.of(r, c)); // Tối ưu bộ nhớ, không cần new ArrayList<>
                }
            }
        }

        return result;
    }

    private void bfs(int[][] heights, Queue<int[]> q, boolean[][] canReach) {
        int rows = heights.length;
        int cols = heights[0].length;
        int[][] directions = {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

        while (!q.isEmpty()) {
            int[] curr = q.poll();
            int r = curr[0];
            int c = curr[1];

            for (int[] d : directions) {
                int newRow = r + d[0];
                int newCol = c + d[1];

                // Kiểm tra biên ma trận
                if (newRow < 0 || newRow >= rows || newCol < 0 || newCol >= cols) {
                    continue;
                }

                // Nếu ô tiếp theo thấp hơn HOẶC đã được duyệt qua rồi thì bỏ qua
                if (canReach[newRow][newCol] || heights[newRow][newCol] < heights[r][c]) {
                    continue;
                }

                // Đánh dấu ngay khi push vào Queue để chặn đứng việc phình bộ nhớ
                canReach[newRow][newCol] = true;
                q.add(new int[]{newRow, newCol});
            }
        }
    }
}