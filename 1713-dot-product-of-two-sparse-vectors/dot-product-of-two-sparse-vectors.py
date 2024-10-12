class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dic = defaultdict(int)
        for i,num in enumerate(self.nums):
            if num != 0:
                self.dic[i] = num
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0

        if len(self.dic) < len(vec.dic):
            for x,val in self.dic.items():
                if x in vec.dic:
                    ans += val*vec.dic[x]
        else:
            for x,val in vec.dic.items():
                if x in self.dic:
                    ans += val*self.dic[x]
        
        return ans

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)