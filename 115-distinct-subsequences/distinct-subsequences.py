class Solution:
    def recursive_helper(self,s,t,s_index,t_index,dp):
            if t_index == len(t):
                return 1
            if s_index == len(s):
                return 0
            
            if dp[s_index][t_index] != -1:
                return dp[s_index][t_index]
            
            take = 0
            not_take = 0 

            if s[s_index] == t[t_index]:
                take = self.recursive_helper(s,t,s_index + 1,t_index + 1,dp)
           
            not_take = self.recursive_helper(s,t,s_index + 1,t_index,dp)
            
            dp[s_index][t_index] = take + not_take
            return dp[s_index][t_index]

    def numDistinct(self, s: str, t: str) -> int:
        dp = [[-1] * len(t) for _ in range(len(s))]
        return self.recursive_helper(s, t, 0, 0,dp)
            
