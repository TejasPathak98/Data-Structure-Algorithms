class Solution:
    import heapq
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        cache = defaultdict(list)
        ans = []

        for s,v in items:
            heapq.heappush(cache[s], -v)
        
        for k,val in cache.items():
            curr = 0
            for _ in range(5):
                curr += -heapq.heappop(cache[k])
            
            ans.append([k,curr // 5])
        
        return sorted(ans,key = lambda x : x[0])




        