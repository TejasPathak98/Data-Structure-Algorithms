class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q = [(query,idx) for idx,query in enumerate(queries)]
        q.sort()

        i = 0
        result = [-1] * len(queries)
        heap = []

        for query,idx in q:
            while i < len(intervals) and intervals[i][0] <= query:
                heappush(heap, (intervals[i][1] - intervals[i][0] + 1 , intervals[i][1]))
                i += 1

            while heap and heap[0][1] < query:
                heappop(heap)

            if heap:
                result[idx] = heap[0][0]
            else:
                result[idx] = -1


        return result 
