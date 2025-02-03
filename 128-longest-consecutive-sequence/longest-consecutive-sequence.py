class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0
        my_set = set(nums)

        for num in list(set(nums)):
            if num - 1 not in my_set:
                curr_streak = 1
                curr_element = num

                while curr_element + 1 in my_set:
                    curr_streak += 1
                    curr_element += 1

                max_streak = max(max_streak,curr_streak)
                
        
        return max_streak
        