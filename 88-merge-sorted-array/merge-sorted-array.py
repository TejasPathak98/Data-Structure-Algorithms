class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        temp = []

        for i in range(m):
            temp.append(nums1[i])
        
        p1 = 0
        p2 = 0
        j = 0

        while p1 < m and p2 < n:
            if temp[p1] <= nums2[p2]:
                nums1[j] = temp[p1]
                j += 1
                p1 += 1
            else:
                nums1[j] = nums2[p2]
                j += 1
                p2 += 1
        
        while p1 < m:
            nums1[j] = temp[p1]
            j += 1
            p1 += 1
        
        while p2 < n:
            nums1[j] = nums2[p2]
            j += 1
            p2 += 1

