class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currEnd = 0
        currFar = 0

        for i in range(len(nums)):
            if currEnd == i:
                currEnd = max(currFar,i + nums[i])
                if currEnd >= len(nums) - 1:return True
            currFar = max(currFar,i + nums[i])

        return False
        

