class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        curr_sum = 0
        curr_len = 0
        hashmap = {0:-1}
        target = sum(nums) - x
        if target == 0:
            return n

        for i in range(len(nums)):
            curr_sum += nums[i]
            j = hashmap.get(curr_sum - target,i)
            curr_len = max(curr_len,i - j)
            hashmap[curr_sum] = i
        
        return n - curr_len if curr_len > 0 else -1
