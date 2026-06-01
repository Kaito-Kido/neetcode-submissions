class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> result = new ArrayList<>();
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i-1]) continue;
            int start = i + 1;
            int end = nums.length - 1;
            while (start < end) {
                int sum = nums[i] + nums[start] + nums[end];
                if (sum == 0) {
                    int currentStart = nums[start];
                    int currentEnd = nums[end];
                    result.add(new ArrayList<>(List.of(nums[i], currentStart, currentEnd)));
                    while (start < end && nums[start] == currentStart) {
                        start++;
                    }

                    while (start < end && nums[end] == currentEnd) {
                        end--;
                    }
                } else if (sum < 0) {
                    int currentStart = nums[start];
                    while (start < end && nums[start] == currentStart) {
                        start++;
                    }
                } else if (sum > 0) {
                    int currentEnd = nums[end];
                    while (start < end && nums[end] == currentEnd) {
                        end--;
                    }
                }
            }
        }

        return result;
    }
}
