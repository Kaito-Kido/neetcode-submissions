from collections import defaultdict 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = defaultdict(int)
        hand.sort()
        for h in hand:
            freq[h] += 1
        
        for h in hand:
            if freq[h] == 0:
                continue
            
            for i in range(h, h + groupSize):
                if freq[i] == 0:
                    return False
                
                freq[i] -= 1
        
        return True

        