class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        idx = 0
        de_deq = deque()
        in_deq = deque()

        for i in range(n):
            while de_deq and nums[de_deq[-1]] < nums[i]:
                de_deq.pop()
            while in_deq and nums[in_deq[-1]] > nums[i]:
                in_deq.pop()
            
            de_deq.append(i)
            in_deq.append(i)

            while nums[de_deq[0]] - nums[in_deq[0]] > 2:
                if idx == de_deq[0] : de_deq.popleft()
                if idx == in_deq[0] : in_deq.popleft()
                idx += 1
            
            ans += i - idx + 1 
        
        return ans
                      


        