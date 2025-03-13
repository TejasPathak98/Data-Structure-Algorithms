class Twitter:

    def __init__(self):
        self.FollowerMap = defaultdict(set)
        self.TweetsMap = defaultdict(list)
        self.timer = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.TweetsMap[userId].append((-self.timer,tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        for f in self.FollowerMap[userId]:
            if len(self.TweetsMap[f]) > 0:
                for t,tweet in self.TweetsMap[f]:
                    tweets.append((t,tweet))
        
        for t,tweet in self.TweetsMap[userId]:
                tweets.append((t,tweet))

        heapify(tweets)
        result = []
        count = 0
        while tweets:
            t, tweet_id = heappop(tweets)
            result.append(tweet_id)
            count += 1
            if count == 10:
                break
        
        return result

                
        
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.FollowerMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.FollowerMap[followerId]:
            self.FollowerMap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)