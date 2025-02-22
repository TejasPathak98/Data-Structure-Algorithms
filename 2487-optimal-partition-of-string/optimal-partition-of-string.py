class Solution:
    def partitionString(self, s: str) -> int:
        no_of_partitions = 0

        i = 0
        temp_charset = set()

        while i < len(s):
            if s[i] not in temp_charset:
                temp_charset.add(s[i])
                i += 1
            else:
                no_of_partitions += 1
                temp_charset.clear()
        
        return no_of_partitions + 1



        