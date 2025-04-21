from collections import OrderedDict

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.freq = 1

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #key -> Node
        self.freq_map = defaultdict(OrderedDict) # freq -> (key -> Node) 
        self.min_freq = 0

    def _update_freq_bucket(self,node):
        freq = node.freq
        key = node.key

        del self.freq_map[freq][key]
        node.freq += 1

        self.freq_map[freq + 1][key] = node

        if not self.freq_map[freq]:
            del self.freq_map[freq]

            if self.min_freq == freq:
                #self.min_freq = min(list(self.freq_map.keys()),default=1)
                self.min_freq = freq + 1

        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self._update_freq_bucket(node)
            return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._update_freq_bucket(node)
        else:
            if self.capacity == len(self.cache):
                self.evict()
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.freq_map[1][key] = new_node
            self.min_freq = 1


    def evict(self):
        if self.freq_map[self.min_freq]:
            key, node = self.freq_map[self.min_freq].popitem(last=False)
            del self.cache[key]

        if not self.freq_map[self.min_freq]:
            del self.freq_map[self.min_freq]
        





        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)