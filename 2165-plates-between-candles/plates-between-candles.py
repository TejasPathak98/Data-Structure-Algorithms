class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        psum = [0] * (len(s) + 1)
        prev = [0] * (len(s) + 1)
        next = [float("inf")] * (len(s) + 1)

        res = []

        for i,ch in enumerate(s):
            psum[i + 1] = psum[i] + (ch == '|')
            prev[i + 1] = i if ch == '|' else prev[i]
        for i,ch in reversed(list(enumerate(s))):
            next[i] = i if ch == '|' else next[i + 1]
        for q in queries:
            l,r = next[q[0]] , prev[q[1] + 1]
            if l < r:
                res.append((r - l) - (psum[r] - psum[l]))
            else:res.append(0)
        
        return res

        