class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals = sorted(intervals, key = lambda x : x[0])
        query = ((q,i) for i,q in enumerate(queries))
        query = sorted(query , key = lambda x : x[0])

        min_heap = []
        i = 0
        result = [-1] * len(query)

        for q,idx in query:
            while i < len(intervals) and q >= intervals[i][0]:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1 , intervals[i][1]))
                i += 1
            
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)
            
            result[idx] = min_heap[0][0] if min_heap else -1

        return result



        