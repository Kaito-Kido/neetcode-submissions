class Solution:
    def minWindow(self, s: str, t: str) -> str:
        contains = defaultdict(int)
    
        for c in t:
            contains[c] += 1
        
        left = 0
        right = 0
        counter = 0
        min_left = 0
        minsublen = len(s)
        containsAll = False
        
        while left < len(s) and right < len(s):
            print(left, right)
            print(s[left], s[right])
            print(contains)
            print(counter)
            print()
            c = s[right]
            if c in contains:
                contains[c] -= 1
                if contains[c] == 0:
                    counter += 1
            
            while counter == len(contains) and left < len(s):
                containsAll = True
                if right - left + 1 < minsublen:
                    minsublen = right - left + 1
                    min_left = left
                if s[left] in contains:
                    contains[s[left]] += 1
                    if contains[s[left]] > 0:
                        counter -= 1
                left += 1
                
            right += 1

           
        if not containsAll: return ""
        return s[min_left:min_left + minsublen]
        