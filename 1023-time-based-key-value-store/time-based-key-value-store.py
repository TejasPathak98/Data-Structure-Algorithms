class TimeMap:

    def __init__(self):
        self.time_dict = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_dict[key].append([timestamp,value])
        
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_dict or timestamp < self.time_dict[key][0][0]:
            return ""
        else:
            list_of_timestamps_and_values = self.time_dict[key]
            l = 0
            r = len(list_of_timestamps_and_values) - 1

            while l <= r:
                mid = (l + r) // 2
                
                if list_of_timestamps_and_values[mid][0] == timestamp:
                    return list_of_timestamps_and_values[mid][1]
                
                elif list_of_timestamps_and_values[mid][0] > timestamp:
                    r = mid - 1
                else:
                    l = mid + 1
            

            return list_of_timestamps_and_values[r][1]


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)