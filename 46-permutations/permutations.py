class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # n = len(nums)

        # def helper(temp,temp_set):
        #     if len(temp) == n:
        #         ans.append(temp[:])
        #         return
            
        #     for j in range(n):
        #         if nums[j] not in temp_set:
        #             temp.append(nums[j])
        #             temp_set.add(nums[j])
        #             helper(temp,temp_set)
        #             temp.pop()
        #             temp_set.remove(nums[j])

        
        # helper([],set())
        # return ans


        #O(N!) ; O(N) + O(N)


        ans = []
        n = len(nums)

        def helper(i):
            if i == n:
                ans.append(nums[:])
                return
            
            for j in range(i,n):
                nums[i] , nums[j] = nums[j] , nums[i]
                helper(i + 1)
                nums[i] , nums[j] = nums[j] , nums[i]

        
        helper(0)
        return ans
