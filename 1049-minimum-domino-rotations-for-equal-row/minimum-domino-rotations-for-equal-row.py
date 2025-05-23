class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(target):
            bottom_swaps = 0
            top_swaps = 0

            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return float('inf')
                elif tops[i] != target:
                    top_swaps += 1
                elif bottoms[i] != target:
                    bottom_swaps += 1
            
            return min(top_swaps,bottom_swaps)

        
        candidate1 = tops[0]
        candidate2 = bottoms[0]

        res = min(check(candidate1),check(candidate2))

        return -1 if res == float('inf') else res

                