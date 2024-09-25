class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        my_dict = defaultdict(list)

        for st in strs:
            x = tuple(sorted(st))
            my_dict[x].append(st)
        
        for key,value in my_dict.items():
            ans.append(value)
        
        return ans


        