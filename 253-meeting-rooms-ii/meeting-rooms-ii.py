class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # intervals.sort()
        # rooms = 1
        # heap = []
        # heappush(heap,intervals[0][1])

        # for i in range(1,len(intervals)):
        #     if intervals[i][0] < heap[0]:
        #         heappush(heap, intervals[i][1])
        #     else:
        #         heapreplace(heap,intervals[i][1])

        #     rooms = max(rooms,len(heap))
        
        # return rooms


        starts = sorted([intervals[i][0]] for i in range(len(intervals)))
        ends = sorted([intervals[i][1]] for i in range(len(intervals)))
        startptr = 0
        endptr = 0
        used = 0
        max_rooms =0 

        while startptr < len(intervals):
            if starts[startptr] < ends[endptr]: #is the next earliest meeting starting before the earliest end meeting time
                used += 1
                startptr += 1 
            else:
                endptr += 1
                used -= 1
            
            max_rooms = max(max_rooms,used)

        return max_rooms





