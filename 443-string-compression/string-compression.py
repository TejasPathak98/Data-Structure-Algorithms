class Solution:
    def compress(self, chars: List[str]) -> int:
        grouped = groupby(chars)
        s = ""
        j = 0
        for key, group in grouped:
            length = len(list(group))
            if length == 1:
                chars[j] = key
                j += 1
            else:
                chars[j] = key
                j += 1
                for c in str(length):
                    chars[j] = c
                    j += 1
                
        return j