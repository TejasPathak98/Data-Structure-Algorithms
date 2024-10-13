class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        M = 1440
        minute = [False] * M
        for time in timePoints:
            mi = self.helper(time)
            if minute[mi]:
                return 0
            else:
                minute[mi] = True
        
        minutes = [i for i in range(M) if minute[i] == True]
        return min(((minutes[i] - minutes[i - 1]) % M for i in range(len(minutes))))

    def helper(self,time):
        h,m = map(int,time.split(":"))
        return h*60 + m
        