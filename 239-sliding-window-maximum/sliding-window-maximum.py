class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        #Decreasing Monotoic Queue (for comparisons at the top)
        #(For Window expiry and taking Max we use front of Deque)


        Deque = deque()
        ans = []
        ans.append(max(nums[:k]))
        for i in range(k):
            while Deque and nums[i] > nums[Deque[-1]]:
                Deque.pop()
            Deque.append(i)

        i = k

        while i < len(nums):
            while Deque and nums[i] > nums[Deque[-1]]:
                Deque.pop()
            Deque.append(i)

            while Deque[0] <= i - k:
                Deque.popleft()
            
            ans.append(nums[Deque[0]])
            i += 1
        
        return ans




