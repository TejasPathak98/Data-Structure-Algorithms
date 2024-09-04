class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums) 

        for num,cnt in count.items():
            if cnt == 1:
                return num    
        return -1
        