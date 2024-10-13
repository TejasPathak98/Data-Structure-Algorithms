class Solution:
    def maximumSwap(self, num: int) -> int:
        if 0 <= num <= 9:
            return num
        s = str(num)

        l = []
        for i in range(len(s)):
            l.append(s[i])
        l_sorted = sorted(l,reverse=True)

        i = 0
        while i < len(l):
            if l[i] == l_sorted[i]:
                i += 1
            else:
                x = l_sorted[i]
                pos = -1
                for k in range(len(l) - 1,-1,-1):
                    if l[k] == x:
                        pos = k
                        break
                l[i] , l[pos] = l[pos] , l[i]
                break
        
        return int(''.join(l))
                

        return 0
        
        #7632