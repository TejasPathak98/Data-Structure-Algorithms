class Solution:
    def customSortString(self, order: str, s: str) -> str:
        n = len(s)
        m = len(order)
        pos = []
        t = ""

        for i in range(m):
            indices = [j for j,c in enumerate(s) if s[j] == order[i]]
            if indices != [-1]:
                pos.extend(indices)
        
        print(pos)

        for i in range(len(pos)):
            t = t + s[pos[i]]
        
        for i in range(n):
            if i not in pos:
                t = t + s[i]
        
        return t
        
        
        


        