class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        count = Counter(hand)
        keys = sorted(count) #when we sort count(a counter) we just get the keys
        #count_ = sorted(count.items(),key = lambda x : (x[1],x[0]))

        for key in keys:
            while count[key] > 0:
                for i in range(groupSize):
                    if count[i + key] <= 0:
                        return False
                    count[i + key] -= 1

        return True
