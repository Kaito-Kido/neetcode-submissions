class Solution {
    // Time Complexity: O(N)
    // Space Complexity: O(1)
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        if (nums.length == 2) return Math.max(nums[0], nums[1]);
        int rob1Prev2 = 0;
        int rob2Prev2 = 0;
        int rob1Prev1 = nums[0];
        int rob2Prev1 = nums[1];
        int rob1 = 0;
        int rob2 = 0;
        

        for (int i = 1; i < nums.length - 1; i++) {
            rob1 = Math.max(rob1Prev1, rob1Prev2 + nums[i]);
            rob1Prev2 = rob1Prev1;
            rob1Prev1 = rob1;

            rob2 = Math.max(rob2Prev1, rob2Prev2 + nums[i + 1]);
            rob2Prev2 = rob2Prev1;
            rob2Prev1 = rob2;
        }

        return Math.max(rob1, rob2);
    }
}
