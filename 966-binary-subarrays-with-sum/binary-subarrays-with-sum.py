class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            count += prefix[curr_sum - goal]
            prefix[curr_sum] += 1
            
        return count
            