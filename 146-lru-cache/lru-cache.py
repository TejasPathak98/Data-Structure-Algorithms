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
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.RemoveNode(node)
            self.addNode(node)
            return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.RemoveNode(node)
            self.addNode(node)
        else:
            if len(self.cache) == self.capacity:
                self.RemovefromLast()
            node = Node(key,value)
            self.cache[key] = node
            self.addNode(node)

    def addNode(self,new_node):
        temp_node = self.head.next
        self.head.next = new_node
        new_node.next = temp_node
        new_node.prev = self.head
        temp_node.prev = new_node
    
    def RemoveNode(self,node):
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
    
    def RemovefromLast(self):
        node = self.tail.prev
        if node.key not in self.cache:
            return
        del self.cache[node.key]
        self.RemoveNode(node)



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)