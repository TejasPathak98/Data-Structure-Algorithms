class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        
        gas_until_now = 0
        cost_until_now = 0
        start_idx = 0

        for i in range(len(gas)):

            gas_until_now += gas[i]
            cost_until_now += cost[i]

            if gas_until_now < cost_until_now:
                gas_until_now = 0
                cost_until_now = 0
                start_idx = i + 1

        
        return start_idx



