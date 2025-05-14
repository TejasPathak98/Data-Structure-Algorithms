class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.TTL = timeToLive
        self.cache = {}
        self.heap = []
    
    def delete_if_expired(self,currentTime):
        while self.heap and self.heap[0][0] <= currentTime:
            expiry_time,token = heappop(self.heap)

            if self.cache[token] == expiry_time:
                del self.cache[token]
        
    def generate(self, tokenId: str, currentTime: int) -> None:
        self.delete_if_expired(currentTime)
        self.cache[tokenId] = currentTime + self.TTL
        heappush(self.heap, (currentTime + self.TTL,tokenId))


    def renew(self, tokenId: str, currentTime: int) -> None:
        self.delete_if_expired(currentTime)
        if tokenId not in self.cache:
            return
        else:
            new_expiry_time = currentTime + self.TTL
            self.cache[tokenId] = new_expiry_time
            heappush(self.heap, (new_expiry_time,tokenId))


    def countUnexpiredTokens(self, currentTime: int) -> int:
        self.delete_if_expired(currentTime)
        return len(self.cache)
        


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)