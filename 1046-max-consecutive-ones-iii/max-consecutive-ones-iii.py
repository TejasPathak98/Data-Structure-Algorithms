class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_ans = 0

        i = 0
        j = 0
        ans = 0

        while j < n:
            if nums[j] == 1:
                max_ans = max(j - i + 1,max_ans)
                j += 1
            else:
                if k > 0:
                    k -= 1
                    max_ans = max(j - i + 1,max_ans)
                    j += 1
                else:
                    if nums[i] == 0:
                        k += 1
                        i += 1
                    else:
                        i += 1
                    
        
        return max_ans



            


        