class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)

        for x,freq in count.items():
            if freq > 1:
                return True  
        
        return False

        