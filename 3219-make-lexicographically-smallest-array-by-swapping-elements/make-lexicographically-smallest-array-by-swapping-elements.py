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
        values_indices = [(val,idx) for idx,val in enumerate(nums)]

        values_indices.sort(key = lambda x : x[0])

        for i in range(n - 1):
            val1,idx1 = values_indices[i]
            val2,idx2 = values_indices[i + 1]

            if abs(val1 - val2) <= limit:
                uf.union(idx1, idx2)


        connected_components = defaultdict(list)
        
        for idx,val in enumerate(nums):
            root = uf.find(idx)
            connected_components[root].append(idx)

        
        res = nums[:]

        for indices in connected_components.values():
            values = [nums[i] for i in indices]
            idx_range = indices
            idx_range.sort()
            values.sort()

            for i,v in zip(idx_range,values):
                res[i] = v


        
        return res

