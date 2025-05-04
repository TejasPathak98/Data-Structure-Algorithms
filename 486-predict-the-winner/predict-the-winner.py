class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        dp = [[0] * n for _ in range(n)]

        for i in range(n - 2,-1,-1):
            dp[i][i] = nums[i]

            for j in range(i + 1,n):
                left = nums[i] - dp[i + 1][j]
                right = nums[j] - dp[i][j - 1]
                dp[i][j] = max(left,right)


        return dp[0][n - 1] >= 0 