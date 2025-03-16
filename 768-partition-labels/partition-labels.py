class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        L = len(s)
        s_dict = {s[i] : i for i in range(L)}

        ans = []
        i = 0

        while i < L:
            j = i
            end = s_dict[s[j]]

            while j < end:
                if s_dict[s[j]] > end:
                    end = s_dict[s[j]]
                j += 1
            
            ans.append(end - i + 1)
            i = end + 1
        

        return ans