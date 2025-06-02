class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        counter = Counter(s)
        min_len = n
        left = 0
        target = n // 4

        for right in range(len(s)):
            
            counter[s[right]] -= 1 #we stretch the window to right(the window here is the replacable sub-string we want to minimize)

            while left < n and all(counter[ch] <= target for ch in 'QWER'):
                min_len = min(min_len,right - left + 1)
                counter[s[left]] += 1
                left += 1

        return min_len


