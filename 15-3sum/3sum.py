class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # if len(nums) < 3:
        #     return []
        # nums = sorted(nums)
        # ans = set()

        # for i,v in enumerate(nums):
        #     if i >= 1 and nums[i - 1] == v:
        #         continue
        #     triplet_dict = {}
        #     for x in nums[i + 1:]:
        #         if x not in triplet_dict:
        #             triplet_dict[(-x-v)] = 1
        #         else:
        #             ans.add((v,x,-x-v))
        
        # return list(ans)

        #O(N^2) ; O(N)

        if len(nums) < 3:
            return []
        nums.sort()
        ans = []

        for i,v in enumerate(nums):
            if i >= 1 and nums[i - 1] == v:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + v
                if total == 0:
                    ans.append([v,nums[left],nums[right]])
                    left += 1
                    right -= 1
                
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return ans




        