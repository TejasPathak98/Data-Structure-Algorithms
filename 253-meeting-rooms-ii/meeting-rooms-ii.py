class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x : x[0])

        min_heap = []
        heapify(min_heap)
        meeting_rooms = 0

        for i in range(len(intervals)):
            if not min_heap:
                heappush(min_heap, intervals[i][1])
                meeting_rooms = max(meeting_rooms,len(min_heap))
            else:
                if intervals[i][0] >= min_heap[0]: #No such functionality like min_heap.peek() (only in Java)
                    heappushpop(min_heap, intervals[i][1])
                    meeting_rooms = max(meeting_rooms,len(min_heap))
                else:
                    heappush(min_heap, intervals[i][1])
                    meeting_rooms = max(meeting_rooms,len(min_heap))


        return meeting_rooms