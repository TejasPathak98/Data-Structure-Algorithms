class SummaryRanges:

    def __init__(self):
        self.nums = set()

    def addNum(self, value: int) -> None:
        self.nums.add(value)

    def getIntervals(self) -> List[List[int]]:
        seen = set()
        result = []

        for num in self.nums:
            if num in seen:
                continue
            
            seen.add(num)
            
            left = num
            while left - 1 in self.nums:
                left -= 1
                seen.add(left)
            
            right = num
            while right + 1 in self.nums:
                right += 1
                seen.add(right)

            print(result)
            result.append([left,right])

        return sorted(result)





# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()