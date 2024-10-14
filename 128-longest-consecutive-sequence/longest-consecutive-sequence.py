class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        n = len(nums)
        longest_streak = 0

        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                current_streak = 1
                current = num

                while current + 1 in nums:
                    current_streak += 1
                    current += 1
                longest_streak = max(longest_streak,current_streak)
        
        return longest_streak
                


        