class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":return 0
        if len(s) == 1:return 1
        if len(s) == 2:
            if 10 <= int(s) <= 26:
                if int(s) in (10,20):return 1
                else: return 2
            elif int(s) % 10 == 0:
                return 0
            else:
                return 1
        
        dp = [0] * len(s)
        dp[0] = 1
        if 10 <= int(s[:2]) <= 26:
            if int(s[:2]) in (10,20):
                dp[1] = 1
            else:dp[1] = 2
        else:
            if int(s[:2]) % 10 == 0:return 0
            else: dp[1] = 1
            
        
        for i in range(2,len(s)):
            if s[i] != "0":
                dp[i] += dp[i - 1]
                if 10 <= int(s[i - 1:i + 1]) <= 26:
                    dp[i] += dp[i - 2]
            else:
                if int(s[i - 1:i + 1]) in (10,20):
                    dp[i] += dp[i - 2]
                else:
                    return 0
        
        return dp[len(s) - 1]
                



        