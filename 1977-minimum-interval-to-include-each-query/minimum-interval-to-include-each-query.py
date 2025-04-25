class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x : x[0])
        q = [(query,idx) for idx,query in enumerate(queries)]
        q.sort(key = lambda x: x[0])

        i = 0
        result = [-1] * len(queries)
        min_heap = []

        for query,idx in q:
            while i < len(intervals) and query >= intervals[i][0]:
                heappush(min_heap,(intervals[i][1] - intervals[i][0] + 1,intervals[i][1]))
                i += 1
            
            while min_heap and min_heap[0][1] < query:
                heappop(min_heap)
            
            if min_heap:
                result[idx] = min_heap[0][0]
            else:
                result[idx] = -1
        

        return result
