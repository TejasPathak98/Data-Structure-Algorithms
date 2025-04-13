class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = [[startTime[i] , endTime[i] , profit[i]] for i in range(n)]
        jobs.sort(key = lambda x : x[0])
        startTime.sort()
        dp = [-1] * len(startTime)
       

        return self.helper(0,jobs,startTime,dp,n)

    def helper(self,i,jobs,startTime,dp,n):
        if i >= n:
            return 0
        if dp[i] != -1:
            return dp[i]

        index_of_next_job = bisect.bisect_left(startTime,jobs[i][1])

        dp1 = jobs[i][2] + self.helper(index_of_next_job,jobs,startTime,dp,n)
        dp2 = self.helper(i + 1,jobs,startTime,dp,n)
        dp[i] = max(dp1,dp2)
        return dp[i]



        




