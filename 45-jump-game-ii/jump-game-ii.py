class Solution:
    def jump(self, nums: List[int]) -> int:
        currEnd = 0
        currFar = 0

        answer = 0

        for i in range(len(nums) - 1):
            currFar = max(currFar,nums[i] + i)

            if i == currEnd:
                answer += 1
                currEnd = currFar
                
            
        return answer
        