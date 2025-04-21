class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2 , nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:
            partitionX = (left + right) //2
            partitionY = (m + n + 1) // 2 - partitionX

            leftMaxX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            rightMinX = float('inf') if partitionX == m else nums1[partitionX]
            leftMaxY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            rightMinY = float('inf') if partitionY == n else nums2[partitionY]

            if leftMaxX <= rightMinY and leftMaxY <= rightMinX:
                if (m + n) % 2 == 1:
                    return max(leftMaxX,leftMaxY)
                else:
                    return (max(leftMaxX,leftMaxY) + min(rightMinX,rightMinY))/2.0
            
            elif leftMaxX > rightMinY:
                right = partitionX - 1
            else:
                left = partitionX + 1
        

        return -1.0
