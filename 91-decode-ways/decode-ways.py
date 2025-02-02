class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 1:
            if s[0] != "0":
                return 1
            else:
                return 0
        
        if s[0] == "0":
            return 0
                
        dp = [0] * len(s)
        dp[0] = 1
        if int(s[:2]) == 10 or int(s[:2]) == 20:dp[1] = 1
        elif 11 <= int(s[:2]) <= 26:dp[1] = 2
        elif s[1] == "0":return 0
        else: dp[1] = 1


        for i in range(2,len(s)):
            if s[i] != "0":
                dp[i] = dp[i - 1]
                if 11 <= int(s[i - 1:i + 1]) <= 26:
                    dp[i] += dp[i - 2]
            else:
                if s[i - 1] == "1" or s[i - 1] == "2":
                    dp[i] = dp[i - 2]
                else:
                    return 0

        
        return dp[len(s) - 1]

        
        # 11,23
        # 1,1,23


        # 1,12,3
        # 11,2,3
        # 1,1,2,3