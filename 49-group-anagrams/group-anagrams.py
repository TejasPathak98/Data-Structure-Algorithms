class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        my_dict = defaultdict(list)

        for st in strs:
            if tuple(sorted(st)) in my_dict:
                my_dict[tuple(sorted(st))].append(st)
            else:
                my_dict[tuple(sorted(st))].append(st)
        
        for key,val in my_dict.items():
            ans.append(val)
        
        return ans
        