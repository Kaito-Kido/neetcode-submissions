class Solution {
    public boolean exist(char[][] board, String word) {
        int m = board.length;
        int n = board[0].length;
        boolean[][] visited = new boolean[m][n];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (backtracking(board, i, j, word, 0, visited)) return true;
            }
        }
        return false;
    }

    private boolean backtracking(char[][] board, int i, int j, String word, int index, boolean[][] visited) {
        // Kiểm tra điều kiện dừng
        if (index == word.length()) return true;
        
        // Kiểm tra biên, đã thăm và ký tự có khớp không
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length || 
            visited[i][j] || board[i][j] != word.charAt(index)) {
            return false;
        }

        // Đánh dấu đã thăm
        visited[i][j] = true;

        // Các hướng: Lên, Xuống, Trái, Phải
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        for (int[] d : directions) {
            if (backtracking(board, i + d[0], j + d[1], word, index + 1, visited)) {
                return true;
            }
        }

        // BACKTRACK: Bỏ đánh dấu để các hướng khác có thể dùng
        visited[i][j] = false;
        return false;
    }
}