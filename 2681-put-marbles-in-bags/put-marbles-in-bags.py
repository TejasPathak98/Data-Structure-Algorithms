class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == len(weights):
            return 0

        n = len(weights) - 1

        #the idea is here is that k bags combination will have the weights[0] + weights[n] 
        # we want the diff : (weights[0] + weights[n] + largest k - 1 cuts) - (weights[0] + weights[n] + smallest k - 1 cuts)
        # we have (largest k - 1 cuts) - (smallest k - 1 cuts)
        #the cuts are basically weights[i] + weight[i + 1] done at any i

        costs = [weights[i] + weights[i + 1] for i in range(n)]
        costs.sort()
        res = 0

        for i in range(k - 1):
            res += costs[-1 - i] - costs[i]
        
        return res
        
