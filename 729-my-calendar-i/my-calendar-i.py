class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.events:
            self.events.append([startTime,endTime])
            return True
        else:
            for event in self.events:
                if startTime < event[1] and endTime > event[0]: # important condition covering partial and full overlaps
                    return False
            self.events.append([startTime,endTime])
            return True
                    


        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)