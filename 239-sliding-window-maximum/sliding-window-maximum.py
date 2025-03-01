class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # if len(nums) == 1:
        #     return [nums[0]]
        
        # ans = []

        # max_heap = []
        # for i in range(k):
        #     max_heap.append((-1 * nums[i],i))

        # heapq.heapify(max_heap)

        # ans.append(-1 * max_heap[0][0])

        # for i in range(k,len(nums)):
        #     while max_heap and max_heap[0][1] <= i - k:
        #         heapq.heappop(max_heap)
            
        #     heapq.heappush(max_heap, (-1 * nums[i],i))
        #     ans.append(-1* max_heap[0][0])
        
        # return ans

        # #O(NlogN) ; O(N)
        
        if len(nums) == 1:
            return [nums[0]]
        
        ans = []
        dq = deque()

        for i in range(len(nums)):
            if dq and dq[0] < i - k + 1:
                dq.popleft()
            
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()
            
            dq.append(i)

            if i >= k - 1:
                ans.append(nums[dq[0]])
        
        return ans


