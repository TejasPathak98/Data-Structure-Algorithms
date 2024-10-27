class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        
        i = 0
        ans = []
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]

                if summ == 0:
                    ans.append([nums[i],nums[j],nums[k]])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                elif summ < 0:
                    j += 1
                else:
                    k -= 1
            
            i += 1
        
        return ans
        

        