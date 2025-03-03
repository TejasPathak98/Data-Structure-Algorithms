class Solution:
    def __init__(self):
        self.minHeap = []
        self.maxHeap = []

    def helper(self,number,minHeap,maxHeap):
        if not maxHeap:
            heapq.heappush(maxHeap,-number)
        elif not minHeap:
            heapq.heappush(minHeap, number)
        else:
            if len(maxHeap) <= len(minHeap):
                heapq.heappush(maxHeap,-number)
            elif len(maxHeap) >= len(minHeap) + 1:
                heapq.heappush(minHeap, number)

        if maxHeap and minHeap and -maxHeap[0] > minHeap[0]:
            x = -heapq.heappop(maxHeap)
            heapq.heappush(minHeap, x)

        while len(maxHeap) < len(minHeap):
            x = heapq.heappop(minHeap)
            heapq.heappush(maxHeap, -x)
            
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums1)):
            self.helper(nums1[i],self.minHeap,self.maxHeap)
        
        for i in range(len(nums2)):
            self.helper(nums2[i],self.minHeap,self.maxHeap)

        if len(self.maxHeap) == len(self.minHeap) + 1:
            return float(-self.maxHeap[0])
        else:
            print(self.minHeap[0])
            return float((-self.maxHeap[0] + self.minHeap[0]) / 2)

        

    




        