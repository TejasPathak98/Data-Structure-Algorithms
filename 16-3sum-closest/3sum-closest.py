class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        return self.Kclosest(nums,target,3)

    def Kclosest(self,nums,target,k):
        N = len(nums)

        if N < k:
            return 10 ** 4 + (1001)
        
        if N == k:
            return sum(nums)
        
        if N > k:
            if sum(nums[:k]) >= target:
                return sum(nums[:k])
            if sum(nums[-k:]) <= target:
                return sum(nums[-k:])

        if k == 1:
            var =  [(x,abs(target - x)) for x in nums]
            return min(var,key = lambda x : x[1])[0]

        
        closest = sum(nums[:k])
        
        for i, x in enumerate(nums):
            if i > 0 and nums[i - 1] == x:
                continue
            
            bs = self.Kclosest(nums[i + 1:], target - x, k - 1)
            t = bs + x

            if abs(t - target) < abs(target - closest):
                if t == target:
                    return target
                closest = t
        
        return closest
        