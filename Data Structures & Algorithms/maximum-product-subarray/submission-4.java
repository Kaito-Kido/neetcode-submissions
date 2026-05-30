class Solution {
    public int maxProduct(int[] nums) {
        // Time Complexity: O(N)
        // Space Complexity: O(1)

        int[] dp = new int[nums.length];
        int max = nums[0];
        int min = nums[0];
        int result = max;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] < 0) {
                int temp = max;
                max = min;
                min = temp;
            }

            max = Math.max(max * nums[i], nums[i]);
            min = Math.min(min * nums[i], nums[i]);

            result = Math.max(max, result);
        }

        return result;
    }
}
