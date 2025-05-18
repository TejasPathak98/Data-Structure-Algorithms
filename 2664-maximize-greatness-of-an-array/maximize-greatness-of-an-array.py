class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        original = sorted(nums)
        perm = sorted(nums)
        count = 0
        i = 0

        for j in range(len(nums)):
            if perm[j] > original[i]:
                count += 1
                i += 1

        
        return count