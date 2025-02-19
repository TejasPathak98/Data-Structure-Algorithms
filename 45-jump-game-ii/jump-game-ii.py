class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:return 0

        currFar = 0
        currEnd = 0
        no_of_jumps = 0

        for i in range(len(nums)):
            currFar = max(currFar,i + nums[i])

            if currEnd == i:
                no_of_jumps += 1
                currEnd = currFar
                if currFar >= len(nums) - 1:
                    break
                
        
        return no_of_jumps