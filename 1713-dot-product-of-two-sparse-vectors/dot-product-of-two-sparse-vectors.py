class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {i:n for i,n in enumerate(nums) if n}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0

        
        if len(self.nums) < len(vec.nums):
            for key in self.nums.keys():
                if key in vec.nums:
                    result += self.nums.get(key) * vec.nums.get(key)
        else:
            for key in vec.nums.keys():
                if key in self.nums:
                    result += self.nums.get(key) * vec.nums.get(key)

        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)