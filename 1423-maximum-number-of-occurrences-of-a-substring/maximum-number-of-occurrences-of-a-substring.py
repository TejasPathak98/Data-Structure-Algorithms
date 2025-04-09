class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        substring_dict = defaultdict(int)

        for i in range(len(s) - minSize + 1):
            t = s[i:i + minSize]

            if len(set(t)) <= maxLetters:
                substring_dict[t] += 1

        
        return max(substring_dict.values()) if substring_dict else 0