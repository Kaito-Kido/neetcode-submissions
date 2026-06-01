class Solution {
    public int[] productExceptSelf(int[] nums) {
        int zeroCount = 0;
        int product = 1;
        for (int i : nums) {
            if (i == 0) {
                zeroCount++;
            } else {
                product *= i;
            }
        }

        int[] output = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            if (zeroCount == 0) {
                output[i] = product / nums[i];
            } else if (zeroCount == 1) {
                if (nums[i] == 0) {
                    output[i] = product;
                } else {
                    output[i] = 0;
                }
            } else {
                output[i] = 0;
            }
        }

        return output;
    }
}
