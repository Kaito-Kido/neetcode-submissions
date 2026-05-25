class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        
        int[] store = new int['z' - 'a' + 1];
        for (int i = 0; i < store.length; i++) {
            store[i] = 0;
        }

        char[] sChar = s.toCharArray();
        for (int i = 0; i < s.length(); i++) {
            store[sChar[i] - 'a'] += 1;
        }

        char[] tChar = t.toCharArray();
        for (int i = 0; i < t.length(); i++) {
            store[tChar[i] - 'a'] -= 1;
        }

        for (int i = 0; i < store.length; i++) {
            if (store[i] != 0) return false;
        }

        return true;
    }
}
