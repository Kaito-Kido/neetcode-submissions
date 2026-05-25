class Solution {
    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            Integer minus = map.get(target - nums[i]);
            if (minus != null) {
                return new int[]{minus, i};
            }

            map.put(nums[i], i);
        }

        return new int[]{}; // place holder return
    }
}
