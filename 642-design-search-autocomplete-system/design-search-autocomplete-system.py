class TrieNode:
    def __init__(self):
        self.children = {}
        self.top_sentences = []

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.frequencies = {}
        self.prefix = ""
        self.root = TrieNode()
        self.current_node = self.root
        self.invalid_prefix = False

        for sentence,time in zip(sentences,times):
            self.add_sentence(sentence,time)
            self.frequencies[sentence] = time
        

    def add_sentence(self,sentence,time):

        self.curr_node = self.root

        for char in sentence:
            if char not in self.curr_node.children:
                self.curr_node.children[char] = TrieNode()
            self.curr_node = self.curr_node.children[char]

            ts = [(t,s) for t,s in self.curr_node.top_sentences if s != sentence]
            ts = ts + [(time,sentence)]
            ts.sort(key = lambda x : (-x[0],x[1]))
            ts = ts[:3]
            self.curr_node.top_sentences = ts

    def input(self, c: str) -> List[str]:
        if c == "#":
            freq = self.frequencies.get(self.prefix,0)
            freq += 1
            self.frequencies[self.prefix] = freq
            self.add_sentence(self.prefix, freq)
            self.prefix = ""
            self.invalid_prefix = False
            self.current_node = self.root
            return []
        
        self.prefix += c

        if self.invalid_prefix or c not in self.current_node.children:
            self.invalid_prefix = True
            return []

        self.current_node = self.current_node.children[c]
        return [word for (_,word) in self.current_node.top_sentences]







        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)