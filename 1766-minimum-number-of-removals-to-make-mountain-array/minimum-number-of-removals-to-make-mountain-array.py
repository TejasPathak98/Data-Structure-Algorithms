class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        lis = [1]*n
        lid = [1]*n 

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])

        for i in range(n - 1,-1,-1):
            for j in range(i + 1,n):
                if nums[i] > nums[j]:
                    lid[i] = max(lid[i],1 + lid[j])
        
        ans = 1000 
        for a,b in zip(lis,lid):
            if a == 1 or b == 1:
                continue
            else:
                ans = min(ans,n - a - b + 1)
        
        return ans
