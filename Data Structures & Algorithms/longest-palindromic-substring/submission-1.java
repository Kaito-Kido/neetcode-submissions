class Solution {
    public String longestPalindrome(String s) {
        if (s.length() == 1) return s;
        if (s.length() == 2 && s.charAt(0) == s.charAt(1)) return s;
        boolean[][] dp = new boolean[s.length()][s.length()];
        int maxLength = 1;
        int start = 0;

        // base case
        for (int i = 0; i < s.length(); i++) {
            dp[i][i] = true;
        }

        for (int i = 0; i < s.length() - 1; i++) {
            if (s.charAt(i) == s.charAt(i + 1)) {
                dp[i][i+1] = true;
                maxLength = 2;
                start = i;
            } else {
                dp[i][i+1] = false;
            }
        }

        for (int length = 3; length <= s.length(); length++) {

            for (int i = 0; i < s.length() - length + 1; i++) {
                dp[i][i + length - 1] = s.charAt(i) == s.charAt(i + length - 1) && dp[i + 1][i + length - 2] == true;
                if (dp[i][i + length - 1] == true && length > maxLength) {
                    maxLength = length;
                    start = i;
                }
            }
        }


        return s.substring(start, start + maxLength);
    }
}
