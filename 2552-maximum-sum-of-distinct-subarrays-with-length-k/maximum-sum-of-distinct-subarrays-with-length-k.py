class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        l,r,total,mx = 0,0,0,0 
        visit = set()

        while r < len(nums):
            while nums[r] in visit:
                visit.remove(nums[l])
                total -= nums[l]
                l += 1 
            visit.add(nums[r])
            total += nums[r]
            if r - l + 1 == k:
                mx = max(mx,total)
                visit.remove(nums[l])
                total = total - nums[l]
                l += 1
            r += 1
        
        return mx



        