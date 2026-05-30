class Solution {
    public int climbStairs(int n) {
        if (n == 1) return 1;

        int[] mem = new int[n + 1];
        mem[0] = 1;
        mem[1] = 1;

        return recur(n, mem);
    }

    public int recur(int i, int[] mem) {
        if (mem[i] != 0) return mem[i];

        return mem[i] = recur(i - 1, mem) + recur(i - 2, mem);
    }
}
