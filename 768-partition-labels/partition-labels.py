class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        L = len(s)

        last_occ_map = {s[i] : i for i in range(len(s))}

        i = 0
        ans = []

        while i < L:

            j = i

            end = last_occ_map[s[j]]

            while j < end:
                if last_occ_map[s[j]] > end:
                    end = last_occ_map[s[j]]
                j += 1

            ans.append(end - i + 1)

            i = end + 1

        return ans