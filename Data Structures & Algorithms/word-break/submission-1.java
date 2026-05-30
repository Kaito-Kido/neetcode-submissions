class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        boolean[] dp = new boolean[s.length() + 1];

        dp[0] = true;
        for (int i = 1; i <= s.length(); i++) {
            for (String word : wordDict) {
                if (i - word.length() >= 0) {
                    if (dp[i - word.length()]) {
                        String subString = s.substring(i - word.length(), i);
                        dp[i] = subString.equals(word);
                        // System.out.println(i - word.length());
                        // System.out.println(s.substring(i - word.length(), i));
                        if (dp[i])
                            break;
                    }
                }
            }
        }

        return dp[s.length()];
    }
}
