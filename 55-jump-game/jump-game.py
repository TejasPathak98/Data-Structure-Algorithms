class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if len(nums) == 1:
            return True

        currFar = 0
        currEnd = 0

        for i in range(len(nums) - 1):
            currFar = max(i + nums[i],currFar)

            if i == currEnd:
                currEnd = currFar
                if currEnd >= len(nums) - 1:
                    return True
        
        return False




        