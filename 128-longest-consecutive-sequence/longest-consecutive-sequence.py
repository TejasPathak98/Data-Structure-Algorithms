class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        longest_streak = 0

        my_set = set(nums)

        for num in my_set:
            if num - 1 not in my_set:
                current_number = num 
                current_streak = 1

                while current_number + 1 in my_set:
                    current_number += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak,current_streak)
        
        return longest_streak



        