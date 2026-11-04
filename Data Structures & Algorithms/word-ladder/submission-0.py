from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        def isValid(startword, nextword):
            diff = 0
            for i in range(len(startword)):
                if startword[i] != nextword[i]:
                    diff += 1
                    if diff > 1:
                        return False
            return True
        

        q = deque()
        q.append(beginWord)
        levelcount = 1
        visited = set()
        while q:
            n = len(q)
            for _ in range(n):
                currentword = q.popleft()
                if currentword == endWord:
                    return levelcount
                
                for word in wordList:
                    if word in visited:
                        continue
                    
                    if not isValid(currentword, word):
                        continue
                    visited.add(word)
                    q.append(word)
            levelcount += 1
        return 0


