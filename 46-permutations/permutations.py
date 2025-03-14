class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def helper(temp,temp_set):
            if len(temp) == n:
                ans.append(temp[:])
                return
            
            for j in range(n):
                if nums[j] not in temp_set:
                    temp.append(nums[j])
                    temp_set.add(nums[j])
                    helper(temp,temp_set)
                    temp.pop()
                    temp_set.remove(nums[j])

        
        helper([],set())
        return ans



