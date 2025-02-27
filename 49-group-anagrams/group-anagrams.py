class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # ans = []
        # string_dict = defaultdict(list)

        # for string in strs:
        #     string_dict[tuple(sorted(string))].append(string)
        
        # for key,listofstrings in string_dict.items():
        #     ans.append(listofstrings)
        
        # return ans

        #O(N * llogl) ; O(Nk)

        ans = []
        string_dict = defaultdict(list)

        for string in strs:
            char_count = [0] * 26

            for ch in string:
                char_count[ord(ch) - ord('a')] += 1
            string_dict[tuple(char_count)].append(string)

        return list(string_dict.values())





        