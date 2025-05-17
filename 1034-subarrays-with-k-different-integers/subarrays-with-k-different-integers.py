class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atMost(nums,k) - self.atMost(nums,k - 1)
    
    def atMost(self,nums,k):
        l = 0
        result = 0
        counter = Counter()

        for r in range(len(nums)):
            if counter[nums[r]] == 0:
                k -= 1
            counter[nums[r]] += 1

            while k < 0:
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    k += 1
                l += 1
            
            result += 1 + (r - l)

        return result