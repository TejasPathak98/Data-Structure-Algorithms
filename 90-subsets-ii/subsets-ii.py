class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        
        ans = []
        my_dict = defaultdict(int)
        
        def helper(i,temp):
            if i == len(nums):
                if tuple(sorted(temp)) in my_dict:
                    return
                else:
                    my_dict[tuple(sorted(temp))] += 1
                    ans.append(temp.copy())
                    return
            
            temp.append(nums[i])
            helper(i + 1,temp)
            temp.pop()
            helper(i + 1,temp)
        
        helper(0,[])
        return ans
            

