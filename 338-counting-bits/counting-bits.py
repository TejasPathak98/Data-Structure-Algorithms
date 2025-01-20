class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for x in range(n + 1):
            res = 0
            for i in range(32):
                if (x >> i) & 1:
                    res += 1
            ans.append(res)
        
        return ans

