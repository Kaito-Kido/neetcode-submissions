class Solution {
    public int[] productExceptSelf(int[] nums) {
        int prefix = 1;
        int suffix = 1;
        int product = 1;
        int[] output = new int[nums.length];

        for (int i = 0; i < nums.length; i++) {
            output[i] = product * prefix;
            product *= nums[i];
        }
        product = 1;
        for (int i = nums.length - 1; i >=0 ; i--) {
            output[i] *= suffix * product;
            product *= nums[i];
        }

        return output;
    }
}
