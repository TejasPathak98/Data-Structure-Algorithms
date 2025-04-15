class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []

        str_dict = defaultdict(list)

        for st in strs:
            str_dict[tuple(sorted(st))].append(st)

        for v in str_dict.values():
            ans.append(v)
        return ans