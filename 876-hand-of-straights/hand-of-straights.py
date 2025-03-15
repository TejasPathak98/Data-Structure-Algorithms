class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) % groupSize != 0:
        #     return False
        
        # n = len(hand)
        
        # heapify(hand)
        # count = 0
        # temp = []
        # temp_store = []
        # ans = []

        # while hand:
        #     x = heapq.heappop(hand)
        #     if len(temp) >= 1:
        #         if temp[-1] == x:
        #             temp_store.append(x)
        #             continue
        #         elif temp[-1] != x - 1:
        #             return False
        #         elif temp[-1] == x - 1:
        #             temp.append(x)
        #             count += 1
        #     else:
        #         temp.append(x)
        #         count += 1
            
        #     if count == groupSize:
        #         ans.extend(temp[:])
        #         temp.clear()
        #         count = 0
        #         for y in temp_store:
        #             heapq.heappush(hand, y)
        #         temp_store.clear()

        # return len(ans) == n

        # #O(NlogN) ; O(N)


        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        keys = sorted(count)

        for key in keys:
            while count[key] > 0:
                for i in range(groupSize):
                    if count[i + key] <= 0:
                        return False
                    count[i + key] -= 1
            
        return True