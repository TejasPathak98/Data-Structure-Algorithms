class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        my_dict = defaultdict(int)
        my_dict[0] = 1
        prefix_sum = 0
        ans = 0

        for num in nums:
            prefix_sum += num

            if prefix_sum - goal in my_dict:
                ans += my_dict[prefix_sum - goal]
            
            my_dict[prefix_sum] += 1
        
        return ans

        