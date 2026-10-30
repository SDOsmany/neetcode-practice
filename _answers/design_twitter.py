"""
Design Twitter (Medium)

Design a simple class Twitter.

- postTweet(userId, tweetId) records a new tweet.
- getNewsFeed(userId) returns the IDs of the 10 most recent tweets from that user and the people they follow, newest first.
- follow(followerId, followeeId) starts following someone.
- unfollow(followerId, followeeId) stops following someone.

Example 1:
t = Twitter()
t.postTweet(1, 10)
t.postTweet(2, 20)
t.getNewsFeed(1)  ->  [10]
t.follow(1, 2)
t.getNewsFeed(1)  ->  [20, 10]
t.unfollow(1, 2)
t.getNewsFeed(1)  ->  [10]
Explanation: The feed only includes people currently followed.

Constraints:
- Users don't follow themselves
- Tweet IDs are unique
"""

import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets.setdefault(userId, []).append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.following.get(userId, set()) | {userId}
        all_tweets = [t for u in users for t in self.tweets.get(u, [])[-10:]]
        return [tid for _, tid in heapq.nlargest(10, all_tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following.get(followerId, set()).discard(followeeId)


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
