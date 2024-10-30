class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        new_time = []
        for time in timePoints:
            l = time.split(":")
            new_time.append(int(l[0]) * 60 + int(l[1]))
        new_time = sorted(new_time)

        ans = float("INF")

        for i in range(1,len(new_time)):
            ans = min(ans,new_time[i] - new_time[i - 1])
        
        ans = min(ans,1440 - new_time[-1] + new_time[0])
        return ans

        