class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        min_ans = float('inf')
        arr = []

        for time in timePoints:
            t = time.split(":")
            arr.append(int(t[0])*60 + int(t[1]))
        
        arr = sorted(arr)

        for i in range(1,len(arr)):
            min_ans = min(min_ans,(arr[i] - arr[i - 1]))
        
        return min(min_ans,arr[0] + 1440 - arr[-1])

        #O(nlogn) ; O(n)


