class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.my_dict = defaultdict(Node)
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key not in self.my_dict:
            return -1
        else:
            node = self.my_dict[key]
            self.removeNode(node)
            self.addNode(node)
            return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.my_dict:
            node = self.my_dict[key]
            node.value = value
            self.removeNode(node)
            self.addNode(node)
        else:
            if len(self.my_dict) < self.capacity:
                node = Node(key,value)
                self.addNode(node)
                self.my_dict[key] = node
            else:
                self.removeLastNode()
                node = Node(key,value)
                self.addNode(node)
                self.my_dict[key] = node
            
    def addNode(self,node):
        next_temp = self.head.next
        self.head.next = node
        node.next = next_temp
        node.prev = self.head
        next_temp.prev = node

    def removeNode(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def removeLastNode(self):
        node = self.tail.prev
        if node.key not in self.my_dict:
            return
        del self.my_dict[node.key]
        self.removeNode(node)
    
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)