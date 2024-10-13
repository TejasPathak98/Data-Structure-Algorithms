class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.prev = self.tail
        self.tail.next = self.head
        self.dic = defaultdict(Node)
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            node = self.dic[key]
            self.removeNode(node)
            self.addNode(node)
            return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.value = value
            self.removeNode(node)
            self.addNode(node)
        else:
            if len(self.dic) >= self.capacity:
                self.removeLastNode()
            node = Node(key,value)
            self.addNode(node)
            self.dic[key] = node  

    def removeNode(self,node):
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node

    def addNode(self,node):
        temp = self.head.prev
        self.head.prev = node
        node.next = self.head
        node.prev = temp
        temp.next = node
    
    def removeLastNode(self):
        if len(self.dic) == 0:
            return
        temp = self.tail.next
        del self.dic[temp.key]
        self.removeNode(temp)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)