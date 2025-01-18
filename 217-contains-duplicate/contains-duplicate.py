class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c = Counter(nums)

        for num, freq in c.items():
            if freq >= 2:
                return True
        
        return False