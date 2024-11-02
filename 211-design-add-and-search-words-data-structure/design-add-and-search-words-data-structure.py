class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEnd = True
        
    def search(self, word: str) -> bool:
        return self.helper(0,word,self.root)
    
    def helper(self,index,word,node):
        if index == len(word):
            return node.isEnd
        
        c = word[index]

        if c == ".":
            for child in node.children.values():
                if self.helper(index + 1, word, child):
                    return True
            return False
        else:
            if c in node.children:
                return self.helper(index + 1, word, node.children[c])
            else:
                return False


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)