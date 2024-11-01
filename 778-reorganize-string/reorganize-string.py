class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        c = sorted(c.items(),key = lambda x : x[1],reverse = True)

        res = []
        for k,val in c:
            res.extend([k] * val)
        
        res = deque(res)
        arr = [None] * len(s)
        i = 0

        while res:
            if i > len(s) - 1:
                i = 1
            arr[i] = res[0]
            res.popleft()
            i += 2
        
        for i in range(1,len(arr)):
            if arr[i] == arr[i - 1]:
                return ""
        return "".join(arr)


        