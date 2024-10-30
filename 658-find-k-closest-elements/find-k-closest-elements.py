class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        my_dict = defaultdict(list)

        for num in arr:
            my_dict[abs(num - x)].append(num)
        
        my_dict = dict(sorted(my_dict.items()))

        ans = []

        for _,val in my_dict.items():
            if len(ans) + len(val) < k:
                ans.extend(val)
            else:
                extra = len(ans) + len(val) - k
                val = sorted(val)
                pos = len(val) - extra
                val = val[:pos]
                ans.extend(val)

        return sorted(ans)