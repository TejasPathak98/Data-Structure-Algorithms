class Solution:
    def customSortString(self, order: str, s: str) -> str:
        n = len(s)
        m = len(order)
        pos = []
        t = ""
        l_ = list(range(n))

        for i in range(m):
            indices = [j for j,c in enumerate(s) if s[j] == order[i]]
            if indices != [-1]:
                pos.extend(indices)

        for i in range(len(pos)):
            t = t + s[pos[i]]
        
        l = list(set(l_) - set(pos))

        for i in range(len(l)):
            t = t + s[l[i]]

        return t
        
        
        


        