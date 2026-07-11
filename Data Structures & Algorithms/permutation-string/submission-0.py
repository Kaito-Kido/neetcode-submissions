class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        character_count = defaultdict(int)
    
        for s in s1:
            character_count[s] += 1
        
        window_size = len(s1)
        left = 0
        right = 0
        current_count = defaultdict(int)
        
        while right < len(s2):
            current_count[s2[right]] += 1
            while (right - left + 1) > window_size:
                current_count[s2[left]] -= 1
                left += 1
                
            if right - left + 1 == window_size:
                isInclude = True
                for key, value in character_count.items():
                    if value != current_count[key]:
                        isInclude = False
                if isInclude:
                    return True
            
            right += 1
        return False