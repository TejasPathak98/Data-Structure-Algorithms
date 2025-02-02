class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:return 0
        answer = 0
        currEnd = 0
        currFar = 0

        for i in range(len(nums) - 1):
            currFar = max(currFar,i + nums[i])

            if i == currEnd:
                answer += 1
                currEnd = currFar
        
        return answer
        