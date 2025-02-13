class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        L = len(s)
        last = {s[i] : i for i in range(L)}

        ans = []
        i = 0

        while i < L:
            j = i + 1
            end = last[s[i]]
            while j < end:
                if last[s[j]] > end:
                    end = last[s[j]]
                j += 1
            
            ans.append(end - i + 1)
            i = end + 1
        
        return ans

        