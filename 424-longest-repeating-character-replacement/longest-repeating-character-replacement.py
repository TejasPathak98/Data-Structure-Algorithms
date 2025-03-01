class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Fmap = defaultdict(int)
        start = 0
        max_frequency = 0
        max_len = 0

        for end in range(len(s)):
            Fmap[s[end]] += 1
            max_frequency = max(max_frequency,Fmap[s[end]])

            isValid = (end -start + 1 - max_frequency) <= k

            if not isValid:
                Fmap[s[start]] -= 1
                start += 1
            
            max_len = max(max_len,end - start + 1)

        return max_len
