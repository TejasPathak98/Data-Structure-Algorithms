class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class MaxStack:

    def addNode(self,prev_node,node):
        temp = prev_node.next
        node.prev = prev_node
        prev_node.next = node
        node.next = temp
        temp.prev = node
    
    def removeNode(self,node):
        nxt,prev = node.next,node.prev
        nxt.prev = prev
        prev.next = nxt

    def __init__(self):
        self.cache = {}
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_heap = []

    def push(self, x: int) -> None:
        node = Node(x)
        self.addNode(self.tail.prev,node)
        self.cache.setdefault(x,[]).append(node)
        heappush(self.max_heap, -x)

    def pop(self) -> int:
        x = self.tail.prev.value
        self.cache[x].pop()
        if not self.cache[x]:
            del self.cache[x]
        self.removeNode(self.tail.prev)
        return x
        
    def top(self) -> int:
        return self.tail.prev.value
        
    def peekMax(self) -> int:

        while self.max_heap and -self.max_heap[0] not in self.cache:
            heappop(self.max_heap)
        
        return -self.max_heap[0]
        

    def popMax(self) -> int:

        while self.max_heap and -self.max_heap[0] not in self.cache:
            heappop(self.max_heap)

        x = -self.max_heap[0]
        

        node = self.cache[x].pop()
        if not self.cache[x]:
            del self.cache[x]

        self.removeNode(node)

        return x
            


        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()