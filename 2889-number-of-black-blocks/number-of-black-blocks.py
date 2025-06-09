class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        counts = defaultdict(int)

        for x,y in coordinates:
            for i in range(max(0,x - 1),min(x + 1,m - 1)):
                for j in range(max(0,y - 1),min(y + 1,n - 1)):
                    counts[(i,j)] += 1 #it represents a 2*2 sub-grid (top left corner)

        
        ans = [0] * 5

        for count in counts.values():
            ans[count] += 1

        
        ans[0] = (m - 1) * (n - 1) - sum(ans)

        return ans


        
