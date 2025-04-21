class TimeMap:

    def __init__(self):
        self.my_dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.my_dict[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.my_dict:
            return ""
        else:
            values = self.my_dict[key]
            idx = bisect.bisect_right(values,(timestamp,chr(137)))
            if idx - 1 >= 0:
                _ , val = values[idx - 1]

                return val
            return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)