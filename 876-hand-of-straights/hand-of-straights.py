class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        n = len(hand)
        
        heapify(hand)
        count = 0
        temp = []
        temp_store = []
        ans = []

        while hand:
            x = heapq.heappop(hand)
            if len(temp) >= 1:
                if temp[-1] == x:
                    temp_store.append(x)
                    continue
                elif temp[-1] != x - 1:
                    return False
                elif temp[-1] == x - 1:
                    temp.append(x)
                    count += 1
            else:
                temp.append(x)
                count += 1
            
            if count == groupSize:
                ans.extend(temp[:])
                temp.clear()
                count = 0
                for y in temp_store:
                    heapq.heappush(hand, y)
                temp_store.clear()

        return len(ans) == n

        #1,2,2,3,3,4,6,7,8


