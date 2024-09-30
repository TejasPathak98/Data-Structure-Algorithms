class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if not timePoints:
            return 0

        arr = []
        min_diff = float('inf')
        
        for st in timePoints:
            time = st.split(":")
            arr.append(int(time[0]) * 60 + int(time[1]))
        
        arr = sorted(arr)

        for i in range(1,len(arr)):
            min_diff = min(min_diff,(arr[i] - arr[i-1]))
        
        return min(min_diff,arr[0] + 1440 - arr[-1])
        

        