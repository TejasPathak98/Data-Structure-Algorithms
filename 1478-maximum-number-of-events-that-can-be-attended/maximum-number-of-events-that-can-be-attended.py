class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort() #we want the earliest events up front

        i = 0 #to track events
        curr_day = events[0][0] #current day starting point
        meetings_ending_time = [] #min heap for tracking event end times
        n = len(events)
        count = 0

        #the approach is a greedy one, where we always select the earliest ending event at any given time

        while i < n or meetings_ending_time:
            
            #events starting this day
            while i < n and curr_day == events[i][0]:
                heappush(meetings_ending_time, events[i][1])
                i += 1

            #removing expired events
            while meetings_ending_time and meetings_ending_time[0] < curr_day:
                heappop(meetings_ending_time)

            #choosing the meeting to attend and attending it
            if meetings_ending_time:
                heappop(meetings_ending_time)
                curr_day += 1
                count += 1

            #jumping forward if no events in heap
            if len(meetings_ending_time) == 0 and i < n and curr_day < events[i][0]:
                curr_day = events[i][0]


        return count
