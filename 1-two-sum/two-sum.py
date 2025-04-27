class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for idx,num in enumerate(nums):
            if target - num in my_dict:
                return [idx,my_dict[target - num]]
            my_dict[num] = idx
        return [-1,-1]