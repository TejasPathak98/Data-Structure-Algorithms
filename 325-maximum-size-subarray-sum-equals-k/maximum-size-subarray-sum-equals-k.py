class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        my_dict = defaultdict(int)
        my_dict[0] = -1
        prefix_sum = 0
        max_ans = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum - k in my_dict:
                max_ans = max(max_ans,i - my_dict[prefix_sum - k])
            if prefix_sum not in my_dict:
                my_dict[prefix_sum] = i
        
        return max_ans

            
        