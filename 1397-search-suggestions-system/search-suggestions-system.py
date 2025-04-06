class Trie:
    def __init__(self):
        self.children = {}
        self.isEnd = True
        self.word = ""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #Build the Trie
        self.root = Trie()

        for product in products:
            node = self.root
            for ch in product:
                if ch not in node.children:
                    node.children[ch] = Trie()
                node = node.children[ch]
            node.isEnd = True
            node.word = product

        result = []

        for i in range(len(searchWord)):
            prefix = searchWord[:i + 1]

            node = self.root
            word_list = set()
            flag = False

            for ch in prefix:
                if ch not in node.children:
                    flag = True
                    break
                node = node.children[ch]
            
            if flag:
                result.append([])
                continue


            # if node.isEnd == True:
            #     #print("Exact Prefix Match is present")
            #     word_list.add(prefix)
            
            
            def count_words(node,prefix,word_list):
                if len(node.word) != 0 and node.isEnd:
                    word_list.add(node.word)
                
                for ch,child in node.children.items():
                    count_words(child,prefix + ch,word_list)
                    
            count_words(node,prefix,word_list)

            word_list = list(word_list)
            word_list = sorted(word_list)
            word_list = word_list[:3]

            result.append(word_list)

        
        return result



        