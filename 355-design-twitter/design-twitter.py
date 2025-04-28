class Twitter:

    def __init__(self):
        self.followerMap = defaultdict(set)
        self.TweetsMap = defaultdict(list)
        self.timer = 1
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.TweetsMap[userId].append((-self.timer,tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        users = self.followerMap[userId] | {userId}

        for u in users:
            if self.TweetsMap[u]:
                idx = len(self.TweetsMap[u]) - 1

                time , tweetID  = self.TweetsMap[u][idx]
                heappush(max_heap,(time,tweetID,u,idx))

        result = []

        while max_heap and len(result) < 10:
            time,tweetID,UID,idx = heappop(max_heap)
            result.append(tweetID)

            if idx - 1 >=0:
                new_time , new_tweetID  = self.TweetsMap[UID][idx - 1]
                heappush(max_heap,(new_time,new_tweetID,UID,idx - 1))
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followerMap[followerId].add(followeeId)

        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followerMap[followerId]:
            self.followerMap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)