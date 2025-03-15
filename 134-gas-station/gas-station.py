class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # if sum(cost) > sum(gas):
        #     return -1
        
        # for i in range(len(gas)):
        #     if cost[i] - gas[i] > 0:
        #         continue
        #     else:
        #         return i
        
        # return -1

        if sum(cost) > sum(gas):
            return -1
        
        g = 0
        idx = 0

        for i in range(len(gas)):
            g += gas[i] - cost[i]
            if g < 0:
                idx = i + 1
                g = 0
        
        return idx