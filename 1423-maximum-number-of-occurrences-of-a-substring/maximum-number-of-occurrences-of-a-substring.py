class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substring_dict = defaultdict(int)

        for i in range(len(s) - minSize + 1):
            if len(set(s[i:i + minSize])) <= maxLetters:
                substring_dict[s[i:i+minSize]] += 1

        if substring_dict:
            return max(substring_dict.values())
        else:
            return 0
        
        