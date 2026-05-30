class Solution {
    // Time Complexity: O(N)
    // Space Complexity: O(1)
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);
        int prev2 = 0;
        int prev1 = nums[0];
        int dp1 = 0;
        

        for (int i = 1; i < nums.length - 1; i++) {
            dp1 = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = dp1;
        }

        prev1 = nums[1];
        prev2 = 0;
        int dp2 = 0;

        for (int i = 2; i < nums.length; i++) {
            dp2 = Math.max(prev1, prev2 + nums[i]);
            prev2 = prev1;
            prev1 = dp2;
        }

        return Math.max(dp1, dp2);
    }
}
