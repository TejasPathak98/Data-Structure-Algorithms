class Solution:
    def compress(self, chars: List[str]) -> int:
        j = 0

        for key,gr in groupby(chars):
            gr = list(gr)
            if len(gr) == 1:
                chars[j] = key
                j += 1
            else:
                chars[j] = key
                j += 1
                l = str(len(gr))
                for ch in l:
                    chars[j] = ch
                    j += 1
                

        return j