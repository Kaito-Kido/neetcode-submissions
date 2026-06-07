class Solution {
    public int maxSubArray(int[] nums) {
        int prev = -1000001;
        int max = prev;
        for (int i = 0; i < nums.length; i++) {
            prev = Math.max(prev + nums[i], nums[i]);
            max = Math.max(prev, max);
        }
        return max;
    }
}
