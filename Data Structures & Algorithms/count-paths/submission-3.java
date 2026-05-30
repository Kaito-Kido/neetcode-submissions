class Solution {
    public int uniquePaths(int m, int n) {
        long result = 1;
        int N = m + n - 2;
        int K = Math.min(m - 1, n - 1); // Chọn K nhỏ hơn để tính nhanh hơn

        for (int i = 1; i <= K; i++) {
            result = result * (N - K + i) / i;
        }
        return (int) result;
    }
}
