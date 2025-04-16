class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        meeting_heap = []
        heapify(meeting_heap)

        for interval in intervals:
            if not meeting_heap:
                heapq.heappush(meeting_heap,interval[1])
            else:
                if meeting_heap[0] > interval[0]:
                    heapq.heappush(meeting_heap, interval[1])
                else:
                    heapq.heapreplace(meeting_heap,interval[1])
        
        return len(meeting_heap)

