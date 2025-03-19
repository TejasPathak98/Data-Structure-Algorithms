class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        num_set = set()
        num_list = []

        for num in nums:
            if num not in num_set:
                num_set.add(num)
                num_list.append(num)
        
        
        
        nums.clear()
        for x in num_list:
            nums.append(x)

        return