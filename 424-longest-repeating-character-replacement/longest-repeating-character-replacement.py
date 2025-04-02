class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        Fmap = [0] * 26
        start = 0
        end = 0
        max_freq = 0
        max_len = 0
        Map = defaultdict(int)

        while end < len(s):
            Map[s[end]] += 1
            max_freq = max(max_freq,Map[s[end]])

            if (end - start + 1) - max_freq > k:
                Map[s[start]] -= 1
                start += 1
            
            max_len = max(max_len,end - start + 1)
            end += 1
        
        return max_len