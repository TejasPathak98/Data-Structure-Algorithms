class Node:
    def __init__(self,key,value):
        self.key = key 
        self.value = value
        self.next = None 
        self.prev = None 


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.Head = Node(0,0)
        self.Tail = Node(0,0)
        self.capacity = capacity
        self.Head.next = self.Tail 
        self.Tail.prev = self.Head

    def add_node(self,node):
        node.prev = self.Head 
        node.next = self.Head.next 
        self.Head.next.prev = node
        self.Head.next = node
    
    def remove_node(self,node):
        p = node.prev 
        n = node.next
        p.next = n
        n.prev = p  
        
        
    
    def move_node(self,node):
        self.remove_node(node) 
        self.add_node(node) 
    
    def pop_node(self):
        node = self.Tail.prev
        self.remove_node(node) 
        #del self.cache[node.key] 
        return node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1 
        else:
            node = self.cache[key]
            self.move_node(node) 
            return node.value        

    def put(self, key: int, value: int) -> None:
        if not self.cache.get(key):
            newNode = Node(key,value)
            self.cache[key] = newNode
            self.add_node(newNode)
            if len(self.cache) > self.capacity:
                p = self.pop_node()
                del self.cache[p.key] 
        else:
            self.cache[key].value = value 
            self.move_node(self.cache[key])

                 





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)