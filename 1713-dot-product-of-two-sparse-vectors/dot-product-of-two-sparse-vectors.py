class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dic = defaultdict(int)
        for i,num in enumerate(nums):
            if num != 0:
                self.dic[i] = num  

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i,num in enumerate(vec.nums):
            if num != 0:
                if i in self.dic:
                    ans += num * self.dic[i]
        return ans

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)