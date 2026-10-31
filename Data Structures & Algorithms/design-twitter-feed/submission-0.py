
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

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.following[userId] | {userId}
        newsfeed = []

        for followee in followees:
            newsfeed.extend(self.tweets[followee])

        newsfeed.sort(key=lambda tweet: tweet[1], reverse=True)

        return [tweetId for tweetId, seq in newsfeed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
