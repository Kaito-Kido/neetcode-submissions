class Solution {
    public int numDecodings(String s) {
        if (s.length() == 1) return s.equals("0") ? 0 : 1;
        Set<String> alphabet = new HashSet<>();
        for (int i = 0; i <= 26; i++) {
            alphabet.add(String.valueOf(i));
        }

        int[] dp = new int[s.length() + 1];
        dp[0] = s.charAt(0) == '0' ? 0 : 1;
        dp[1] = s.charAt(0) != '0' && s.charAt(1) != '0'  ? 1 : 0;

        for (int i = 2; i <= s.length(); i++) {
            if (i < s.length() - 1 && s.charAt(i) == '0') {
                dp[i] = 0;
                continue;
            };
            if (alphabet.contains(s.substring(i - 2, i))) {
                dp[i] += dp[i-2];
            }

            if (alphabet.contains(s.substring(i - 1, i)) ) {
                dp[i] += dp[i-1];
            }
        }

        return dp[s.length()];
    }
}
