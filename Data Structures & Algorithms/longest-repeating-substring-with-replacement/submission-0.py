class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        left = 0
        right = 0
        maxsubstring = 0
        
        def findMax():
            current_max = 0
            for v in d.values():
                if v > current_max:
                    current_max = v
            return current_max
        
        while right < len(s):
            d[s[right]] += 1
            while (right - left + 1) - findMax() > k:
                d[s[left]] -= 1
                left += 1
            
            maxsubstring = max(maxsubstring, right - left + 1)
            right += 1
        return maxsubstring