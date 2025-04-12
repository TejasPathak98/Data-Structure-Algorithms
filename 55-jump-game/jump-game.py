class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        currFar = 0
        currEnd = 0

        # if nums[0] == 0:
        #     return False
        
        for i in range(len(nums)):
            currFar = max(currFar,i + nums[i])

            if i == currEnd:
                currEnd = currFar

                if currEnd >= len(nums) - 1:
                    return True

        
        return False
