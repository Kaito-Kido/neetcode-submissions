class Solution {
    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int row = heights.length;
        int col = heights[0].length;
        boolean[][] canReachPacific = new boolean[row][col];
        boolean[][] canReachAtlantic = new boolean[row][col];
        
        for (int c = 0; c < col; c++) {
            canReachPacific[0][c] = true;
            canReachAtlantic[row - 1][c] = true;
        }

        for (int r = 0; r < row; r++) {
            canReachPacific[r][0] = true;
            canReachAtlantic[r][col - 1] = true;
        }

        for (int c = 0; c < col; c++) {
            bfs(heights, 0, c, canReachPacific);
            bfs(heights, row - 1, c, canReachAtlantic);
        }

        for (int r = 0; r < row; r++) {
            bfs(heights, r, 0, canReachPacific);
            bfs(heights, r, col - 1, canReachAtlantic);
        }
        
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (canReachPacific[i][j] && canReachAtlantic[i][j]) {
                    result.add(new ArrayList<>(List.of(i, j)));
                }
            }
        }

        return result;
    }

    public void bfs(int[][] heights, int row, int col, boolean[][] canReach) {
        int cols = canReach[0].length;
        int rows = canReach.length;
        Queue<Integer> q = new LinkedList<>();
        q.add(row * cols + col);
        int[][] direction = new int[][] {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};
        while (!q.isEmpty()) {
            int currentId = q.poll();
            int r = currentId / cols;
            int c = currentId % cols;

            for (int[] d : direction) {
                int newRow = r + d[0];
                int newCol = c + d[1];

                if (newRow >=0 && newRow < rows && newCol >= 0 && newCol < cols 
                && canReach[newRow][newCol] == false 
                && heights[newRow][newCol] >= heights[r][c]
                ) {
                    canReach[newRow][newCol] = true;
                    q.add(newRow * cols + newCol);
                }
            }
        }
    }
}