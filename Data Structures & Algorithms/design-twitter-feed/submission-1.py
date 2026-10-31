
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
        users = self.following[userId] | {userId}

        # Each pointer starts at the latest tweet
        pointers = {
            uid: len(self.tweets[uid]) - 1
            for uid in users
        }

        result = []

        while len(result) < 10:
            latest_user = None
            latest_seq = -1

            # Find the most recent tweet among all users
            for uid in users:
                index = pointers[uid]

                if index < 0:
                    continue

                tweetId, seq = self.tweets[uid][index]

                if seq > latest_seq:
                    latest_seq = seq
                    latest_user = uid

            # No tweets remaining
            if latest_user is None:
                break

            index = pointers[latest_user]
            tweetId, _ = self.tweets[latest_user][index]

            result.append(tweetId)

            # Move to this user's previous tweet
            pointers[latest_user] -= 1

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
