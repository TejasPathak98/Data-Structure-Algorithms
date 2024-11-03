class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        my_set = set(nums)
        longest_streak = 0

        for num in nums:
            if num - 1 not in my_set:
                streak = 1
                while num + 1 in my_set:
                    streak += 1
                    num += 1
                longest_streak = max(longest_streak,streak)

        return longest_streak


        