class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        
        def merge(n1,n2):
            res = []
            while (n1 or n2):
                if n1 > n2:
                    res.append(n1[0])
                    n1 = n1[1:]
                else:
                    res.append(n2[0])
                    n2 = n2[1:]
            return res

        def findmax(nums,length):
            maxpop = len(nums) - length
            l = []

            i = 0
            while i < len(nums):
                while maxpop > 0 and len(l) > 0 and nums[i] > l[-1]:
                    l.pop()
                    maxpop -= 1
                l.append(nums[i])
                i += 1
            
            return l[:length]

        n1 = len(nums1)
        n2 = len(nums2)
        res = []
        for i in range(k + 1):
            j = k - i
            if i > n1 or j > n2:
                continue
            
            f1 = findmax(nums1,i)
            f2 = findmax(nums2,j)

            res = max(res,merge(f1,f2))

        return res


