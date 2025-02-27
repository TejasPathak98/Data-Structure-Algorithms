class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        string_dict = defaultdict(list)

        for string in strs:
            string_dict[tuple(sorted(string))].append(string)
        
        for key,listofstrings in string_dict.items():
            ans.append(listofstrings)
        
        return ans



        