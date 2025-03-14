class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)


        currEnd = 0
        currFar = 0
        i = 0

        while i <= currEnd:
            currFar = i + nums[i]

            if currEnd >= n - 1:
                return True

            if currFar > currEnd:
                currEnd = currFar
                if currEnd >= n - 1:
                    return True
            i += 1


        return False
