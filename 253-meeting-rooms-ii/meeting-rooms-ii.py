class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = 1
        heap = []
        heappush(heap,intervals[0][1])

        for i in range(1,len(intervals)):
            if intervals[i][0] < heap[0]:
                heappush(heap, intervals[i][1])
            else:
                heapreplace(heap,intervals[i][1])

            rooms = max(rooms,len(heap))
        
        return rooms





