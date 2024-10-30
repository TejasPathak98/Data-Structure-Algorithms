class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        my_dict = defaultdict(list)

        for s in strs:
            my_dict[tuple(sorted(s))].append(s)
        
        for s,val in my_dict.items():
            ans.append(val)
        
        return ans
        