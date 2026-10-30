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

class Twitter:
    def __init__(self):
        pass

    def postTweet(self, userId: int, tweetId: int) -> None:
        pass

    def getNewsFeed(self, userId: int) -> list[int]:
        pass

    def follow(self, followerId: int, followeeId: int) -> None:
        pass

    def unfollow(self, followerId: int, followeeId: int) -> None:
        pass


if __name__ == "__main__":
    import pathlib, sys
    sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
    from _harness import run
    run(__file__)
