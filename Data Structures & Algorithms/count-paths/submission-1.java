class Solution {
    public int uniquePaths(int m, int n) {
        if (m == 1 || n == 1)
            return 1;

        int[] dp = new int[n + 1];
        for (int i = 0; i < n + 1; i++) {
            dp[i] = 1;
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                dp[j] = dp[j - 1] + dp[j];
            }
        }

        return dp[n - 1];
    }
}
