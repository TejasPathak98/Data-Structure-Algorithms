class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        nums = set(nums)

        for num in nums:
            if num - 1 not in nums:
                curr_streak = 1
                var = num + 1
                while var in nums:
                    curr_streak += 1
                    var += 1
                
                longest_streak = max(longest_streak,curr_streak)
    
        return longest_streak

                 
        