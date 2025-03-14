class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # ans = []
        # n = len(nums)

        # def helper(temp,i):
        #     if i > len(nums):
        #         return
            
        #     if i == len(nums):
        #         ans.append(temp[:])
        #         return

        #     temp.append(nums[i])

        #     helper(temp,i + 1)

        #     temp.pop()

        #     helper(temp,i + 1)

        
        # helper([],0)
        # return ans

        ans = []
        n = len(nums)
        nums.sort()

        def helper(temp,i):
            # if i > len(nums):
            #     return
            
            # if i == len(nums):
            #     ans.append(temp[:])
            #     return

            #we do not need explicit conditions because the loop handles it, the function naturally returns after the loop is over

            ans.append(temp[:])

            for j in range(i,len(nums)):
                if j > i and nums[j] == nums[j - 1]:
                    continue
                temp.append(nums[j])
                helper(temp,j + 1)
                temp.pop()  #.....again here we do not need another call like helper(temp,j + 1) because the loop handles it implicitly

        
        helper([],0)
        return ans

