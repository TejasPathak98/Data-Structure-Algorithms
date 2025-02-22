class Solution:
    def partitionString(self, s: str) -> int:
        no_of_partitions = float("inf")
        paritions = []

        i = 0
        temp_charset = set()

        while i < len(s):
            if s[i] not in temp_charset:
                temp_charset.add(s[i])
                i += 1
            else:
                paritions.append(temp_charset.copy())
                temp_charset.clear()
        
        return len(paritions) + 1



        