class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0

        print(dp)

        for i in range(2,n + 1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]

            number = int(s[i - 2:i])
            if 10 <= number <= 26:
                dp[i] += dp[i - 2]
            
        
        return dp[n]