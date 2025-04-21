class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = [(startTime[i],endTime[i],profit[i]) for i in range(n)]
        jobs.sort()
        startTime.sort()
        dp = [-1] * n

        return self.helper(0,jobs,dp,startTime,n)
    
    def helper(self,i,jobs,dp,startTime,n):
        #dp[i] = max(dp1,dp2) 
        #where dp1 = profit[i] + helper(at the next start time) and dp2 = helper(for the next job in Sequence)

        if i >= n:
            return 0
        if dp[i] != -1:
            return dp[i]
        

        next_job_start_time = jobs[i][1]
        idx = bisect.bisect_left(startTime, next_job_start_time)

        dp1 = jobs[i][2] + self.helper(idx,jobs,dp,startTime,n)
        dp2 = self.helper(i + 1,jobs,dp,startTime,n)

        dp[i] = max(dp1,dp2)
        return dp[i]

        



