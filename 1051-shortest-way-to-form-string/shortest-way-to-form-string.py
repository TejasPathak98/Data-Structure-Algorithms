class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        i = 0
        minimum = 1

        for ch in target:
            i = source.find(ch,i)
            if i == -1:
                i = source.find(ch)
                if i == -1:
                    return i
                minimum += 1
            
            i += 1

        return minimum
        