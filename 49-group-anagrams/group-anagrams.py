class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = []

        # str_dict = defaultdict(list)

        # for st in strs:
        #     str_dict[tuple(sorted(st))].append(st)

        # for v in str_dict.values():
        #     ans.append(v)
        # return ans

        str_dict = defaultdict(list)

        for st in strs:

            ch_count = [0] * 26

            for ch in st:
                ch_count[ord(ch) - ord('a')] += 1

            str_dict[tuple(ch_count)].append(st)


        return list(str_dict.values())