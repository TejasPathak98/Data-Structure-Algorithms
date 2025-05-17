class Solution:
    def firstUniqChar(self, s: str) -> int:
        first = {}
        last = {}

        for i in range(len(s)):
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i

        print(first)
        print(last)
        
        for ch,first_idx in first.items():
            if last[ch] == first_idx:
                return first_idx

        return -1
