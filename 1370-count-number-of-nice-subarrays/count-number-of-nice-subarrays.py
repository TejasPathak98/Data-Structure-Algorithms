class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count = 0
        odd_count = 0
        prefix = defaultdict(int)
        prefix[0] = 1

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            count += prefix[odd_count - k]
            prefix[odd_count] += 1

        
        return count
