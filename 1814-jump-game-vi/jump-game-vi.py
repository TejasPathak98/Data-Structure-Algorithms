class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        scores = nums[:]
        q = deque([0])

        for i in range(1,len(nums)):
            if q[0] < i - k:
                q.popleft()
            scores[i] += scores[q[0]]

            while q and scores[q[-1]] < scores[i]:
                q.pop()
            
            q.append(i)

        return scores[-1]



        