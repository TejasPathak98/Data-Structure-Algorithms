class Solution:
    def findValidPair(self, s: str) -> str:
        counter = Counter(s)

        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                if counter[s[i]] == int(s[i]) and counter[s[i+1]] == int(s[i + 1]):
                    return s[i:i + 2]
        
        return ""