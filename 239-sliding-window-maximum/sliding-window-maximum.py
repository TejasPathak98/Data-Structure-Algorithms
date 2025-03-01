class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        
        ans = []

        max_heap = []
        for i in range(k):
            max_heap.append((-1 * nums[i],i))

        heapq.heapify(max_heap)

        ans.append(-1 * max_heap[0][0])

        for i in range(k,len(nums)):
            while max_heap and max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            
            heapq.heappush(max_heap, (-1 * nums[i],i))
            ans.append(-1* max_heap[0][0])
        
        return ans


