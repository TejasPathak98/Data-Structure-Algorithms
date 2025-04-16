class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # n = len(nums)

        # if n == 1:
        #     return 1

        # dp = [1] * n

        # for i in range(1,n):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[j] + 1,dp[i])

        # return max(dp)

        # #O(N^2) ; O(N)

        tails = [] # we recording the ends/tails of the increasing subseq as we observe it

        for num in nums:
            pos = bisect.bisect_left(tails, num)

            if pos == len(tails): #if we find that it is greater than all elements, then we just add it
                tails.append(num)
            else:
                tails[pos] = num #else we just replace the the position in tails which is equal to or least greater than num

        return len(tails)

        #O(NlogN) ; O(N)
