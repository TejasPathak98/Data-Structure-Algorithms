class Solution:
    def maximumSwap(self, num: int) -> int:
        s = list(str(num))
        s_sorted = sorted(s,reverse = True)

        n = len(s)
        i = 0

        pos = -1

        while i < n:
            if s[i] == s_sorted[i]:
                i += 1
                continue
            else:
                pos = i
                for j in range(n - 1,-1,-1):
                    if s[j] == s_sorted[i]:
                        new_pos = j
                        break
                s[i] , s[new_pos] = s[new_pos] , s[i]
                break

        if pos == -1:
            return num
        
        ans = ""

        for x in s:
            ans += x
        return int(ans)