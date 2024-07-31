class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node(self,node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node 
    
    def remove_node(self,node):
        p = node.prev 
        n = node.next
        p.next = n
        n.prev = p
    
    def move_node(self,node):
        self.remove_node(node)
        self.add_node(node)
 
    def pop_node(self):
        node = self.tail.prev 
        self.remove_node(node)
        return node        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.move_node(self.cache.get(key))
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.move_node(self.cache.get(key))
        else:
            node = Node(key,value)
            self.add_node(node)
            self.cache[key] = node
            if len(self.cache) > self.capacity:
                temp_node = self.pop_node()
                del self.cache[temp_node.key]
            


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)