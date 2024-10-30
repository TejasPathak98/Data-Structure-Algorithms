class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        return self.Kclosest(nums,3,target)

    def Kclosest(self,nums,k,target):
        if len(nums) < k:
            return 10**4 + 1001
        
        if len(nums) == k:
            return sum(nums)

        if sum(nums[:k]) >= target:
            return sum(nums[:k])
        
        if sum(nums[-k:]) <= target:
            return sum(nums[-k:])
        
        if k == 1:
            m = float('INF')
            var = -10001
            for x in nums:
                if abs(target - x) < m:
                    m = abs(target - x)
                    var = x
            return var
        
        

        closest = sum(nums[:k])

        for i,x in enumerate(nums):
            bs = self.Kclosest(nums[i + 1:] , k - 1, target - x)
            t = bs + x

            if abs(target - t) < abs(target - closest):
                if target == t:
                    return target
                closest = t
        
        return closest




            

        