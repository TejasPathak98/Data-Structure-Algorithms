class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # heapify(nums)
        # while len(nums) > k:
        #     heappop(nums)
        # return nums[0]

        # #O(N) + O((N- k)logN) ; O(N)


        l = nums[:k]
        heapify(l) #O(k)

        for num in nums[k:]:
            if num > l[0]:
                heappushpop(l, num) #O(logK)
        
        return l[0]