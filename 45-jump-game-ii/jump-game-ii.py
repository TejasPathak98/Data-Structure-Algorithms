class Solution:
    def jump(self, nums: List[int]) -> int:
        currFar = 0
        currEnd = 0
        jumps = 0

        if len(nums) == 1:
            return 0

        for i in range(len(nums)):
            currFar = max(currFar,i + nums[i])

            if i == currEnd:
                currEnd = currFar
                jumps += 1

                if currEnd >= len(nums)  - 1:
                    return jumps


        return -1
