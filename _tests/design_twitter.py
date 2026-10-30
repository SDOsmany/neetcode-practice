
def check(mod, eq):
    t = mod.Twitter()
    t.postTweet(1,10); t.postTweet(2,20)
    eq(t.getNewsFeed(1), [10])
    t.follow(1,2)
    eq(t.getNewsFeed(1), [20,10])
    t.unfollow(1,2)
    eq(t.getNewsFeed(1), [10])
    t.unfollow(1,5)
    eq(t.getNewsFeed(9), [])
    for i in range(100, 115):
        t.postTweet(1,i)
    eq(t.getNewsFeed(1), list(range(114, 104, -1)))
