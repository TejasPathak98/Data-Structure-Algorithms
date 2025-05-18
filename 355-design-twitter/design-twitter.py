class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set)
        self.TweetMap = defaultdict(list)
        self.timer = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.TweetMap[userId].append((-self.timer,tweetId))
        self.timer += 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users = self.followerMap[userId] | {userId}

        for user in users:
            if len(self.TweetMap[user]) > 0:
                idx = len(self.TweetMap[user]) - 1
                time , tweetID = self.TweetMap[user][idx]
                heappush(heap, (time,tweetID,user,idx))

        result = []

        while heap and len(result) < 10:
            t,tweet_ID, u , ID = heappop(heap)
            result.append(tweet_ID)

            if ID - 1 >= 0:
                new_time , new_tweetID = self.TweetMap[u][ID - 1]
                heappush(heap, (new_time,new_tweetID,u,ID - 1))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)