class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        heap = []
        intervals = sorted(intervals)

        for interval in intervals:
            if heap == [] or heap[0] > interval[0]:
                heapq.heappush(heap, interval[1])
            else:
                heapq.heapreplace(heap, interval[1])

        return len(heap)
        