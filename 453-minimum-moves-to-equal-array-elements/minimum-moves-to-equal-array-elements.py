class Solution:
    def minMoves(self, nums: List[int]) -> int:
        #Incrementing n - 1 elements is effectively the same as decreasing that element by 1 in relation to others
        #So for element greater than the smallest, applying the Incrementing n - 1 elements, so that smallest element reaches its level, we should decrement it
        
        nums = sorted(nums)
        ans = 0

        for i in range(len(nums) - 1, -1,-1):
            ans = ans + nums[i] - nums[0]
        return ans