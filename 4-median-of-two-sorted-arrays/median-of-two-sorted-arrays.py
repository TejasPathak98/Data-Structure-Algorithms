class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)

        if n > m:
            nums1 , nums2 = nums2 ,nums1

        n = len(nums1)
        m = len(nums2)
        
        l = 0
        r = len(nums1)

        while l <= r:
            partitionX = (l + r) // 2
            partitionY = (n + m) // 2 - partitionX

            maxLeftX = nums1[partitionX - 1] if partitionX >= 1 else float('-inf')
            minRightX = nums1[partitionX] if partitionX < n else float('inf')
            maxLeftY = nums2[partitionY - 1] if partitionY >= 1 else float('-inf')
            minRightY = nums2[partitionY] if partitionY < m else float('inf')

            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                if (n + m) % 2 == 1:
                    return min(minRightX,minRightY)
                else:
                    return  (max(maxLeftX,maxLeftY) + min(minRightX,minRightY)) / 2.0
            
            elif maxLeftX > minRightY:
                r = partitionX - 1
            else:
                l = partitionX + 1

        
        return -1
        