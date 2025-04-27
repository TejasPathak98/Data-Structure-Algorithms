class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        my_dict = defaultdict(list)

        def process(s):
            arr = [0] * 26
            for ch in s:
                arr[ord(ch) - 97] += 1
            return arr
        
        for s in strs:
            my_dict[tuple(process(s))].append(s)
        
        return list(my_dict.values())


