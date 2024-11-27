class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        ans = 0

        while len(sticks) > 1:
            f1 = heapq.heappop(sticks)
            f2 = heapq.heappop(sticks)
            ans += f1 + f2
            heapq.heappush(sticks,f1 + f2)
        
        return ans


        