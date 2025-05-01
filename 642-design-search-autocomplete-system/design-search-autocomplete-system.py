class TrieNode:
    def __init__(self):
        self.children = {}
        self.top_sentences = []

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr = self.root
        self.frequency_dict = {}
        self.prefix = ""
        self.Invalid_prefix = False

        for sentence,time in zip(sentences,times):
            self.add_sentence(sentence, time)
            self.frequency_dict[sentence] = time

    def add_sentence(self,sentence,times):
        self.current_node = self.root

        for ch in sentence:
            if ch not in self.current_node.children:
                self.current_node.children[ch] = TrieNode()
            self.current_node = self.current_node.children[ch]

            ts = [(t,s) for t,s in self.current_node.top_sentences if s != sentence]
            ts = ts + [(times,sentence)]
            ts = sorted(ts,key = lambda x : (-x[0],x[1]))
            ts = ts[:3]
            self.current_node.top_sentences = ts

    def input(self, c: str) -> List[str]:

        if c == "#":
            f = self.frequency_dict.get(self.prefix,0)
            f += 1
            self.frequency_dict[self.prefix] = f
            self.add_sentence(self.prefix, f)
            self.curr = self.root
            self.Invalid_prefix = False
            self.prefix = ""
            return []

        self.prefix += c

        if self.Invalid_prefix or c not in self.curr.children:
            self.Invalid_prefix = True
            return []

        self.curr = self.curr.children[c]
        return [sentence for (_,sentence) in self.curr.top_sentences]



        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)