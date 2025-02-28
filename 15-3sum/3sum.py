class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        ans = set()

        for i,v in enumerate(nums):
            if i >= 1 and nums[i - 1] == v:
                continue
            triplet_dict = {}
            for x in nums[i + 1:]:
                if x not in triplet_dict:
                    triplet_dict[(-x-v)] = 1
                else:
                    ans.add((v,x,-x-v))
        
        return list(ans)


        