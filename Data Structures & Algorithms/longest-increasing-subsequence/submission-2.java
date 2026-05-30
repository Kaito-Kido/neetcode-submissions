class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] tails = new int[nums.length];
        int size = 0;

        for (int x : nums) {
            // Binary search: tìm vị trí của x trong tails
            int i = 0, j = size;
            while (i != j) {
                int m = (i + j) / 2;
                if (tails[m] < x)
                    i = m + 1;
                else
                    j = m;
            }

            // Thay thế hoặc thêm mới
            tails[i] = x;
            if (i == size)
                size++;
        }
        return size;
    }
}
