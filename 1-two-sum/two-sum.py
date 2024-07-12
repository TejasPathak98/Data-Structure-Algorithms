class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        ans = []
        for i in range(len(nums)):
            if target - nums[i] in dic:
                ans.append(i) 
                ans.append(dic.get(target - nums[i]))
                return ans
            dic[nums[i]] = i 
        
        return []

        