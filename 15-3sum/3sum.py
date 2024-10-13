class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []

        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
        
        i = 0
        while i < len(nums) - 2:
            if i > 0 and nums[i - 1] == nums[i]:
                i += 1
                continue
            else:
                j = i + 1
                k = len(nums) - 1
                

                while j < k:
                    total = nums[i] + nums[j] + nums[k]

                    if total == 0:
                        ans.append([nums[i],nums[j],nums[k]])

                        while j < k and nums[j] == nums[j + 1]:
                            j += 1
                        
                        while j < k and nums[k] == nums[k - 1]:
                            k -= 1
                    
                        j += 1
                        k -= 1
                    elif total < 0:
                        j += 1
                    else:
                        k -= 1
            i += 1

        return ans
                



