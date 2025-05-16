class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        heap = []

        for interval in intervals:
            if not heap:
                heappush(heap,interval[1])
            else:
                if interval[0] < heap[0]:
                    heappush(heap,interval[1])
                else:
                    heapreplace(heap, interval[1])

        return len(heap)