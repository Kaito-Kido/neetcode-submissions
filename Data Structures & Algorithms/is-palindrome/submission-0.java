class Solution {
    public boolean isPalindrome(String s) {
        int start = 0;
        int end = s.length() - 1;

        while (start <= end) {
            while (start < s.length() && !isValidChar(s.charAt(start))) {
                start++;
            }

            while (end >= 0 && !isValidChar(s.charAt(end))) {
                end--;
            }

            if (start <= end) {
                if (Character.toLowerCase(s.charAt(start)) != Character.toLowerCase(s.charAt(end))) return false;
                start++;
                end--;
            }
        }

        return true;
    }

    public boolean isValidChar(char c) {
        if (c <= 'z' && c >= 'a') return true;
        if (c <= 'Z' && c >= 'A') return true;
        if (c <= '9' && c >= '0') return true;
        return false;
    } 
}
