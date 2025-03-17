class Solution:
    def reverseBits(self, n: int) -> int:
        ans = []

        for _ in range(32):
            ans.append(n & 1)
            n = n >> 1
        

        print(ans)

        result = 0

        for i in range(32):
            result += ans[i] * (2 ** (32 - i - 1))
        
        return result
