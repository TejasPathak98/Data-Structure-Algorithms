class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        return self.helper(0,word,self.root)
    
    def helper(self,index,word,node):
        if index == len(word):
            return node.isEnd
        
        if word[index] == ".":
            for child in node.children.values():
                if self.helper(index + 1,word,child):
                    return True
            return False
        else:
            if word[index] not in node.children:
                return False
            else:
                return self.helper(index + 1,word,node.children[word[index]])
    


        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)