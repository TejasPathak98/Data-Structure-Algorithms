class Solution:
    def compress(self, chars: List[str]) -> int:
        grouped = groupby(chars)
        j = 0

        for key , gr in grouped:
            l = list(gr)
            le = len(l)

            if le == 1:
                chars[j] = key
                j += 1
            else:
                chars[j] = key
                j += 1
                for c in str(le):
                    chars[j] = c
                    j += 1
            
        return j
        