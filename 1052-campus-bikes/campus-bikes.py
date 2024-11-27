class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        hq = []
        for w,[wx,wy] in enumerate(workers):
            for b,[bx,by] in enumerate(bikes):
                dis = abs(wx - bx) + abs(wy - by)
                heapq.heappush(hq,(dis,w,b))
        
        bike_set = set()
        worker_set = set()
        ans = [None] * len(workers)

        while hq:
            _,w,b = heapq.heappop(hq)
            if b not in bike_set and w not in worker_set:
                ans[w] = b
                worker_set.add(w)
                bike_set.add(b)
        
        return ans



        