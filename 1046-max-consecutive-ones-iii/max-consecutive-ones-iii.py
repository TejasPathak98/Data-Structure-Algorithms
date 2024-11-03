class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        j = 0
        max_ans = 0

        while j < len(nums):
            if nums[j] == 1:
                max_ans = max(max_ans,j - i + 1)
                j += 1
            else:
                if k > 0:
                    max_ans = max(max_ans,j - i + 1)
                    j += 1
                    k -= 1
                else:
                    if nums[i] == 0:
                        k += 1
                    i += 1

        return max_ans


        