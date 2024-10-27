class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_arr = []
        temp = 0 
        my_dict = defaultdict(int)
        my_dict[0] = 1
        ans = 0

        for num in nums:
            temp += num
            if temp - k in my_dict:
                ans += my_dict[temp - k]
            my_dict[temp] += 1
            
        return ans
                
            
        