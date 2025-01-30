class Twitter:
    

    def __init__(self):
        self.following_dict = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timer = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        self.tweets[userId].append((-self.timer,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = []
        the_users = self.following_dict[userId] | {userId}

        for user in the_users:
            for the_tweet in self.tweets[user]:
                heapq.heappush(max_heap, the_tweet)
        
        return [heapq.heappop(max_heap)[1] for i in range(min(10,len(max_heap)))]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following_dict[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)