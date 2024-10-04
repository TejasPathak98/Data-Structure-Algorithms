class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.Kclosest(nums,3,target)
    
    def Kclosest(self,nums,k,target):
        N = len(nums)

        if N<k:
            return (10**4)+1001

        if N == k:
            return sum(nums[:k])
        
        if sum(nums[:k]) >= target:
            return sum(nums[:k])
        
        if sum(nums[-k:]) <= target:
            return sum(nums[-k:])
        
        if k == 1:
            var = [(x,abs(x - target)) for x in nums]
            return min(var , key = lambda x : x[1])[0]
        
        closest = sum(nums[:k])
        for i , x in enumerate(nums):
            if i > 0 and nums[i - 1] == x:
                continue
            
            bs = self.Kclosest(nums[i + 1:], k - 1, target - x)
            curr = bs + x

            if abs(curr - target) < abs(target - closest):
                if curr == target:
                    return target
                else:
                    closest = curr
        
        return closest


        