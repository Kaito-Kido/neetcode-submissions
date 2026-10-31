
from collections import defaultdict
from typing import List

class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweetsequence = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((tweetId, self.tweetsequence))
        self.tweetsequence += 1

    # Complexity O(10F) vs (F + 10logF)
    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.following[userId] | {userId}
        heap = []
        pointers = {}
        for userId in users:
            pointers[userId] = len(self.tweets[userId]) - 1
        
        for userId in users:
            pointer = pointers[userId]
            if pointer < 0:
                continue
            tweetId, sequence = self.tweets[userId][pointer]
            heap.append((-sequence, tweetId, userId))
            pointers[userId] -= 1
        
        heapq.heapify(heap)
        result = []
        for _ in range(10):
            if not heap:
                break
            _, tweetId, userId = heapq.heappop(heap)
            result.append(tweetId)

            pointer = pointers[userId]
            if pointer >= 0:
                tweetId, sequence = self.tweets[userId][pointer]
                heapq.heappush(heap, (-sequence, tweetId, userId))
                pointers[userId] -= 1
        
        return result



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
