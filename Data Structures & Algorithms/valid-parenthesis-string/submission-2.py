from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        leftstack = deque()
        starstack = deque()
        for i, c in enumerate(s):
            if c == '(':
                leftstack.append(i)
            elif c == '*':
                starstack.append(i)
            else:
                if leftstack:
                    leftstack.pop()
                elif starstack:
                    starstack.pop()
                else:
                    return False
        
        while leftstack:
            if starstack and starstack[-1] > leftstack[-1]:
                starstack.pop()
                leftstack.pop()
            else:
                return False
        
        return True