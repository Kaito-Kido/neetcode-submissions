class Solution {
    // Time complexity: O(n)
    // Space complexity: O(n)
    public int[] twoSum(int[] nums, int target) {
        int capacity = (int) (nums.length / 0.75) + 1;
        Map<Integer, Integer> map = new HashMap<>(capacity);

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            if (map.containsKey(complement)) {
                return new int[]{map.get(complement), i};
            }

            map.put(nums[i], i);
        }

        return new int[]{}; // place holder return
    }
}
