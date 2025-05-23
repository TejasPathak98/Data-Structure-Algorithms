class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        even_numbers = Counter(nums[::2]).most_common(2) + [(0,0)]
        odd_numbers = Counter(nums[1::2]).most_common(2) + [(0,0)]

        if even_numbers[0][0] != odd_numbers[0][0]:
            no_change = even_numbers[0][1] + odd_numbers[0][1]
        else:
            no_change = max(even_numbers[0][1] + odd_numbers[1][1],odd_numbers[0][1] + even_numbers[1][1])
        
        return len(nums) - no_change