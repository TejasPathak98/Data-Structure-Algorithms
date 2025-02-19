class Solution:
    def canJump(self, nums: List[int]) -> bool:
        currFar = 0
        currEnd = 0

        for i in range(len(nums)):
            currFar = max(currFar,i + nums[i])

            if currEnd == i:
                currEnd = currFar
                if currEnd >= len(nums) - 1:
                    return True
        
        return False
        