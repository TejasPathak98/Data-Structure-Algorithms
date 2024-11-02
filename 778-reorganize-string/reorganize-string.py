class Solution:
    def reorganizeString(self, s: str) -> str:
        c = Counter(s)
        print(c)
        c = sorted(c.items(),key = lambda x : x[1],reverse= True)

        res = []
        for k,val in c:
            res.extend([val * k])
        
        st = ''.join(res)
        
        arr = [None] * len(s)
        i = 0
        j = 0

        while j < len(st):
            if i > len(s) - 1:
                i = 1
            arr[i] = st[j]
            i += 2
            j += 1
        
        print(arr)
        
        for i in range(1,len(arr)):
            if arr[i] == arr[i - 1]:
                return ""
        return ''.join(arr)




        return ""
        