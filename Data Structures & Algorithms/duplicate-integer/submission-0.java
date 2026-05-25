class Solution {
    // Time Complexity: O(nlogn)
    // Space Complexity: O(1)
    public boolean hasDuplicate(int[] nums) {
        if (nums.length == 0) return false;
        Arrays.sort(nums);

        int prev = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == prev) return true;

            prev = nums[i];
        }

        return false;
    }
}