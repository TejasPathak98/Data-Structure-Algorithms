class Solution:
    def hammingWeight(self, n: int) -> int:
        # ans = 0
        # for _ in range(32):
        #     if (n >> 1) & 1 == 1:
        #         ans += 1
        #     n = n >> 1
        
        # return ans


        ans = 0
        for _ in range(32):
            if (n & 1) == 1: #Check the LSB and then shift
                ans += 1
            n = n >> 1
        
        return ans

        #Earlier I was not checking the LSB at all