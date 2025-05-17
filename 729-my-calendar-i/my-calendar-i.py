class MyCalendar:

    def __init__(self):
        self.events = []
        
    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.append([startTime,endTime])
            return True
        else:
            idx = bisect.bisect_left(self.events,[startTime,endTime])

            if idx > 0 and self.events[idx - 1][1] > startTime:
                return False
            
            if idx < len(self.events) and self.events[idx][0] < endTime:
                return False
            
            self.events.insert(idx,[startTime,endTime])
            return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)