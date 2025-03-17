class Solution:
    def countBits(self, n: int) -> List[int]:

    #     ans = []

    #     for x in range(n + 1):
    #         ans.append(self.helper(x))
        
    #     return ans

    # def helper(self,x):
    #     res = 0

    #     for _ in range(32):
    #         if (x & 1) == 1:
    #             res += 1
    #         x = x >> 1
        
    #     return res


        ans = [0] * (n + 1)

        for i in range(1,n + 1):
            ans[i] = ans[i >> 1] + (i & 1)

        return ans  
