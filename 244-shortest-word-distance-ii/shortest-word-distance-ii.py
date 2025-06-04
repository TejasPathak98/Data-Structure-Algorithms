class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.indices_map = defaultdict(list)
        for idx,word in enumerate(wordsDict):
            self.indices_map[word].append(idx)
        
    def shortest(self, word1: str, word2: str) -> int:
        index_list1  = self.indices_map[word1]
        index_list2 = self.indices_map[word2]

        i = j = 0
        mid_distance = float('inf')

        while i < len(index_list1) and j < len(index_list2):
            mid_distance = min(mid_distance,abs(index_list1[i] - index_list2[j]))

            if index_list1[i] > index_list2[j]:
                j += 1
            else:
                i += 1

        return mid_distance





        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)

#coding , makes, makes, practice, perfect