class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        scores = nums[:]
        queue = deque([0])

        for i in range(1,len(nums)):
            
            while queue and queue[0] < i - k:
                queue.popleft()
            
            scores[i] += scores[queue[0]]

            while queue and scores[queue[-1]] < scores[i]:
                queue.pop()
            
            queue.append(i)
        
        return scores[-1]




            