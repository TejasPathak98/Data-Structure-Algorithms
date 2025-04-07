class UnionFind:
    def __init__(self,n):
        self.parents = list(range(n))
    
    def find(self,x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self,x,y):
        self.parents[self.find(x)] = self.find(y)

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        uf = UnionFind(n) 

        index_values = []

        for idx,val in enumerate(nums):
            index_values.append((val,idx))
        
        index_values = sorted(index_values)

        for i in range(n - 1):
            val1,idx1 = index_values[i]
            val2,idx2 = index_values[i + 1]
            if abs(val1 - val2) <= limit:
                uf.union(idx1, idx2)

        #Getting a map for connected_components(idx)

        connected_components = defaultdict(list)
        for idx,val in enumerate(nums):
            root = uf.find(idx) # getting parent
            connected_components[root].append(idx)

        
        res = nums[:]
        for indices in connected_components.values():
            values = [nums[i] for i in indices]
            idx_range = indices
            idx_range.sort()
            values.sort()

            for idx,v in zip(idx_range,values):
                res[idx] = v
        
        return res


        

        