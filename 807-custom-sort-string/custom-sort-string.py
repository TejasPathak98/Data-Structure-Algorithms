class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = []

        sMap = defaultdict(int)

        for c in s:
            sMap[c] += 1
        for c in order:
            ans.append(c * sMap[c])
            del sMap[c]
        
        for c,f in sMap.items():
            ans.append(f*c)
        
        return ''.join(ans)
        