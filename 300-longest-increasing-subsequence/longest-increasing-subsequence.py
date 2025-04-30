class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)
        # dp = [1] * n

        # for i in range(1,n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[j] + 1,dp[i])
        
        # return max(dp)

        tails = []

        for num in nums:
            x = bisect.bisect_left(tails, num)

            if x == len(tails):
                tails.append(num)
            else:
                tails[x] = num
        
        return len(tails)



