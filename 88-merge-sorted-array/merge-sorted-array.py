class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        j = m - 1
        k = n - 1

        if i == 0:
            if n == 1:
                nums1[0] = nums2[0]
                return
            else:
                return

        while i >= 0 and j >= 0 and k >= 0:
            if nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1
            print(nums1)
            i -= 1
        
        if j >= 0:
            while j >= 0:
                nums1[i] = nums1[j]
                i -= 1
                j -= 1
                print(nums1)
        
        if k >= 0:
            while k >= 0:
                nums1[i] = nums2[k]
                i -= 1
                k -= 1
        
        
        

        
                