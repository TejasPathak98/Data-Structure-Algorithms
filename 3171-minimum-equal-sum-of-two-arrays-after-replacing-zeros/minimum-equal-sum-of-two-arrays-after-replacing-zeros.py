class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        c1 = nums1.count(0)
        c2 = nums2.count(0)

        print(sum1,c1)
        print(sum2,c2)

        if c1 == 0:
            if sum1 < sum2 + c2:
                return -1
        if c2 == 0:
            if sum2 < sum1 + c1:
                return -1

        if sum1 == sum2:
            return sum1 + max(c1,c2)
        else:
            return max(sum1 + c1,sum2 + c2)







