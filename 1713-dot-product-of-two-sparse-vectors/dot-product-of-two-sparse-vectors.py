class SparseVector:
    def __init__(self, nums: List[int]):
        self.dict = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] != 0:
                self.dict[i] = nums[i]
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for idx,num in self.dict.items():
            if idx in vec.dict:
                ans += self.dict[idx] * vec.dict[idx]
        
        return ans
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)