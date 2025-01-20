class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        sub = 1

        for i in range(1,n + 1):
            if 2 * sub == i:
                sub = i
            
            dp[i] = dp[i - sub] + 1
        
        return dp
