class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        my_dict = defaultdict(list)

        for st in strs:
            my_dict[tuple(sorted(st))].append(st)

        for key,val in my_dict.items():
            ans.append(val)
        
        return ans
        