class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        if len(nums) <= 2:
            return []

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
                total = nums[i] + nums[j] + nums[k]

                if total == 0:
                    ans.append([nums[i],nums[j],nums[k]])
                
                    while j < len(nums) - 1  and nums[j] == nums[j + 1]:
                        j += 1
                    
                    while k > 0 and nums[k] == nums[k - 1]:
                        k -= 1
                    
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
            i += 1
                
        return ans



