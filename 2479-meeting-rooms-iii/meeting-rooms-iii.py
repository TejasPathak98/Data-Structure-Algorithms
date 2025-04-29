class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n)) #(min_heap)
        heapify(available)
        busy = [] #(free time, room_dix) (min_heap)  
        bookings = [0] * n


        for start,end in meetings:
            
            #Start freeing rooms as you as come near a meeting
            while busy and busy[0][0] <= start:
                free_time,room_idx = heappop(busy)
                heappush(available, room_idx)
            
            
            if available:
                room_idx = heappop(available)
                actual_start_time = start
            else:
                free_time , room_idx = heappop(busy) #this is when nothing is available and you wait
                actual_start_time = free_time
            

            duration = end - start
            heappush(busy, (actual_start_time + duration,room_idx))
            bookings[room_idx] += 1

        
        return bookings.index(max(bookings))

        


            