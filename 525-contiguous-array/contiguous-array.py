class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mx = 0
        count = 0
        my_dict = {0:-1}
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1
            
            if count in my_dict:
                ans = max(ans,i - my_dict[count])
            else:
                my_dict[count] = i
                
        return ans


        