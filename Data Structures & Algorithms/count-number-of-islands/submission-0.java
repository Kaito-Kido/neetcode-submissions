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

        Queue<Pair> queue = new LinkedList<>();
        queue.add(new Pair(i, j));

        while (queue.size() != 0) {

            Pair currentIndex = queue.poll();

            int row = currentIndex.row;
            int column = currentIndex.column;

            if (grid[row][column] == '0') {
                continue;
            }

            grid[row][column] = '0';

            // up
            if (row >= 1 && grid[row - 1][column] == '1') {
                queue.add(new Pair(row - 1, column));
            }

            // left
            if (column >= 1 && grid[row][column - 1] == '1') {
                queue.add(new Pair(row, column - 1));
            }

            // down
            if (row < grid.length - 1 && grid[row + 1][column] == '1') {
                queue.add(new Pair(row + 1, column));
            }

            // right
            if (column < grid[0].length - 1 && grid[row][column + 1] == '1') {
                queue.add(new Pair(row, column + 1));
            }
        }
    }

    public class Pair {
        int row;
        int column;

        public Pair(int row, int column) {
            this.row = row;
            this.column = column;
        }
    }
}
