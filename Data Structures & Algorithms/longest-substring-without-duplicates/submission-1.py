class Solution:
    # Time Complexity: O(2n)
    # Space Complexity: O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        start = 0
        end = 0
        set_of_char = set()
        max_len = 0 
        while end < len(s):
            while s[end] in set_of_char:
                set_of_char.remove(s[start])
                start += 1
            max_len = max(end - start + 1, max_len)
            set_of_char.add(s[end])
            end += 1

        return max_len
        
