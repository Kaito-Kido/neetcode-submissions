class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []

        def isPalindrome(s):
            start = 0
            end = len(s) - 1

            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def backtrack(start):
            if start == len(s):
                result.append(path.copy())
                return
            
            for i in range(start, len(s)):
                substring = s[start:i+1]
                if not isPalindrome(substring):
                    continue
                path.append(substring)
                backtrack(i + 1)
                path.pop()
                
        backtrack(0)
        return result

            
