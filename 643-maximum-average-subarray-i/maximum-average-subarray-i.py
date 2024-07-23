class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        max_avg = -float("inf") 

        i = 0
        j = k
        s = sum(nums[:k])
        avg = s / k 
        max_avg = max(avg,max_avg)
       
        for j in range(k,len(nums)):
            s = s + nums[j] - nums[i]
            j += 1
            i += 1
            avg = s / k 
            max_avg = max(avg,max_avg)

        return max_avg