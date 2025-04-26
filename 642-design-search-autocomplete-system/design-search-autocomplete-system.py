class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.sentence_dict = defaultdict(int)
        for i in range(len(sentences)):
            self.sentence_dict[sentences[i]] = times[i]
        self.search_word = ""

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.sentence_dict[self.search_word] += 1
            self.search_word = ""
            return []
        else:
            self.search_word += c
            max_heap = []

            for sentence,freq in self.sentence_dict.items():
                if sentence.startswith(self.search_word):
                    heappush(max_heap,(-freq,sentence))
            
            if not max_heap:
                return []

            result = []
            counter = 3

            while max_heap and counter > 0:
                freq,sentence = heappop(max_heap)
                result.append(sentence)
                counter -= 1
            
            return result

            




        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)