class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = dict() #key to node
        self.head = Node(-1,-1)
        self.tail = Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            node = self.dic[key]
            self.removeNode(node)
            self.addNodetoHead(node)
            return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            self.removeNode(node)
            self.addNodetoHead(node)
            node.value = value
        else:
            if len(self.dic) >= self.capacity:
                self.removefromTail()
            node = Node(key,value)
            self.dic[key] = node
            self.addNodetoHead(node)

    def removeNode(self,node):
        node.next.prev = node.prev
        node.prev.next = node.next
    
    def addNodetoHead(self,node):
        temp = self.head.next
        self.head.next = node
        node.next = temp
        node.prev = self.head
        temp.prev = node
    
    def removefromTail(self):
        if len(self.dic) == 0:
            return
        tail_node = self.tail.prev
        del self.dic[tail_node.key]
        self.removeNode(tail_node)

    

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)