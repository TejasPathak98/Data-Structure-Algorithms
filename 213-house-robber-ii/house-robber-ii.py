class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)
        
        def helper(arr):
            m = len(arr)
            if m == 1:
                return arr[0]
            if m == 2:
                return arr[1]

            dp = [0] * m

            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])

            for i in range(2,m):
                dp[i] = max(dp[i - 2] + arr[i],dp[i - 1])
            
            return dp[m - 1]

        return max(helper(nums[1:]),helper(nums[:-1]))
        