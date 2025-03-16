class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals.sort(key = lambda x : x[0])

        # min_heap = []
        # heapify(min_heap)
        # meeting_rooms = 0

        # for i in range(len(intervals)):
        #     if not min_heap:
        #         heappush(min_heap, intervals[i][1])
        #         meeting_rooms = max(meeting_rooms,len(min_heap))
        #     else:
        #         if intervals[i][0] >= min_heap[0]: #No such functionality like min_heap.peek() (only in Java)
        #             heappushpop(min_heap, intervals[i][1])
        #             meeting_rooms = max(meeting_rooms,len(min_heap))
        #         else:
        #             heappush(min_heap, intervals[i][1])
        #             meeting_rooms = max(meeting_rooms,len(min_heap))


        # return meeting_rooms # we could also eliminate the variable and directly return the len(min_heap) but for clarity probably its better to keep it

        # #O(NlogN) ; O(N)

        start = sorted([i[0] for i in intervals]) #The start of a new meeting
        end = sorted([i[1] for i in intervals]) # The end of exisiting meetings

        start_ptr = end_ptr = meeting_rooms = 0

        for start_ptr in range(len(start)):
            if start[start_ptr] >= end[end_ptr]:
                end_ptr += 1
            else:
                meeting_rooms += 1
        
        return meeting_rooms




