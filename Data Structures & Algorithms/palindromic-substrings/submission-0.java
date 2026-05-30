class Solution {
    public int countSubstrings(String s) {
        
        boolean[][] dp = new boolean[s.length()][s.length()];
        int count = 0;

        // base case
        for (int i = 0; i < s.length(); i++) {
            dp[i][i] = true;
            count++;
        }

        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i+1] = true;
                count++;
            } else {
                dp[i][i+1] = false;
            }
        }

        for (int length = 3; length <= s.length(); length++) {
            for (int i = 0; i < s.length() - length + 1; i++) {
                dp[i][i + length - 1] = s.charAt(i) == s.charAt(i + length - 1) && dp[i + 1][i + length - 2] == true;
                if (dp[i][i + length - 1] == true) {
                    count++;
                }
            }
        }


        return count;
    }
}
