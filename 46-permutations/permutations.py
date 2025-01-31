class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]
        
        ans = set()

        def helper(temp):
            if len(temp) == len(nums):
                ans.add(tuple(temp.copy()))
                return
            
            for i in range(len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    helper(temp)
                    temp.pop()
        
        helper([])
        return list(ans)


        