class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        my_dict = defaultdict(int)
        prefix_sum = 0
        my_dict[0] = 1

        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in my_dict:
                res += my_dict[prefix_sum - k]
            my_dict[prefix_sum] += 1
        
        return res