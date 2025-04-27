class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLen = 0
        maxfreq = 0
        l = 0
        r = 0
        Fmap = [0] * 26
        FreqMap = defaultdict(int)

        while r < len(s):

            FreqMap[s[r]] += 1

            maxfreq = max(maxfreq,FreqMap[s[r]])

            if (r - l + 1)  - maxfreq > k:
                FreqMap[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen,r - l + 1)
            r += 1
        
        return maxLen



