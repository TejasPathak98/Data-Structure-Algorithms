class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1 ,nums2 = nums2 , nums1
        
        l = 0
        r = len(nums1)

        while l <= r:
            partitionX = (l + r) // 2
            partitionY = (len(nums1) + len(nums2) + 1) // 2 - partitionX

            maxLeftX = float("-inf") if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float("inf") if partitionX == len(nums1) else nums1[partitionX]

            maxLeftY = float("-inf") if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float("inf") if partitionY == len(nums2) else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(maxLeftX,maxLeftY) + min(minRightX,minRightY)) / 2.0
                    #return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2.0  # ✅ Fixed parentheses
                else:
                    return float(max(maxLeftX,maxLeftY))
            elif maxLeftX > minRightY:
                r = partitionX - 1
            else:
                l = partitionX + 1
        

        return -1