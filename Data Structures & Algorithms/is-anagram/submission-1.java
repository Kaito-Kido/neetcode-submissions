class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] store = new int['z' - 'a' + 1];
    

        for (int i = 0; i < s.length(); i++) {
            store[s.charAt(i) - 'a'] += 1;
            store[t.charAt(i) - 'a'] -= 1;
        }

        for (int i = 0; i < store.length; i++) {
            if (store[i] != 0) return false;
        }

        return true;
    }
}