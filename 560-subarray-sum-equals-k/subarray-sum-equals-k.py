class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            if nums[0] == k:
                return 1
            else:
                return 0
        
        prefix = defaultdict(int)
        prefix[0] = 1
        count = 0

        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum - k in prefix:
                count += prefix[curr_sum - k]
            
            prefix[curr_sum] += 1

        
        print(prefix)

        
        return count
