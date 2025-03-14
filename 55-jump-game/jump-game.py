class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)

        i = 0
        currEnd = 0
        currFar = 0

        while i <= currEnd:
            currFar = max(currFar,i + nums[i])

            if currFar >= n - 1:
                return True # Early stopping
            
            if currEnd < currFar:
                currEnd = currFar
            
            i += 1
    
        return False