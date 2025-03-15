class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        i = 0
        currFar = 0
        currEnd = 0
        jumps = 0

        while i <= currEnd:
            currFar = max(currFar, i + nums[i])

            if i == currEnd:
                currEnd = currFar
                jumps += 1
                if currEnd >= n - 1:
                    return jumps
            
            i += 1

        return -1