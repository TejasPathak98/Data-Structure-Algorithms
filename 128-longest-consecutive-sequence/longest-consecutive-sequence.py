class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 or n == 1:
            return n

        ls = set(nums)
        max_ans = 0

        for num in ls:
            if num - 1 not in ls:
                current_num = num
                current_streak = 1

                while current_num + 1 in ls:
                    current_num += 1
                    current_streak += 1
                
                max_ans = max(max_ans,current_streak)

        return max_ans

        

        