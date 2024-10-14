class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        rem = total_sum % p

        if rem == 0:
            return 0
        
        hmap = {0:-1}
        prefix_sum = 0
        min_len = len(nums)

        for i, num in enumerate(nums):
            prefix_sum += num
            currentMod = prefix_sum % p
            targetMod = (currentMod - rem + p) % p
            if targetMod in hmap:
                min_len = min(min_len,i - hmap[targetMod])
            hmap[currentMod] = i

        if min_len < len(nums) :
            return min_len
        else:
            return -1
