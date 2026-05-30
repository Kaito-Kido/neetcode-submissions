class Solution {
    // Time COmplexity: O(N)
    // Space Complextiy: O(1)
    public int climbStairs(int n) {
        if (n == 1) return 1;
        int dp1 = 1;
        int dp2 = 1;
        int current = 0;

        for (int i = 2; i <= n; i++) {
            current = dp1 + dp2;
            dp2 = dp1;
            dp1 = current;
        }

        return current;
    }
}
