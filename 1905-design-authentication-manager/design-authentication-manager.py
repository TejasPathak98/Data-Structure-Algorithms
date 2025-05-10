class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.TTL = timeToLive
        self.cache = {}
    
    def delete_if_expired(self,currentTime):
        sorted_cache = sorted(self.cache.items(),key = lambda x : (x[1]))
        x = bisect.bisect_right(sorted_cache, (chr(127),currentTime))


        for i in range(x):
            if sorted_cache[i][1] <= currentTime:
                token = sorted_cache[i][0]
                del self.cache[token]

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.delete_if_expired(currentTime)
        self.cache[tokenId] = currentTime + self.TTL


    def renew(self, tokenId: str, currentTime: int) -> None:
        self.delete_if_expired(currentTime)
        if tokenId not in self.cache:
            return
        else:
            new_expiry_time = currentTime + self.TTL
            self.cache[tokenId] = new_expiry_time


    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.delete_if_expired(currentTime)
        return len(self.cache)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)