class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class MaxStack:

    def __init__(self):
        self.node_map = {} # key -> (collection of nodes in DLL)
        self.max_heap = []
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, x: int) -> None:
        node = Node(x)

        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        self.tail.prev = node
        node.prev = prev

        self.node_map.setdefault(x,[]).append(node)
        heappush(self.max_heap, -x)

    def pop(self) -> int:
        node = self.tail.prev
        val = node.val

        self.node_map[val].pop()
        if not self.node_map[val]:
            del self.node_map[val]

        prev,nxt = node.prev,node.next
        prev.next = nxt
        nxt.prev= prev
        
        return val

    def top(self) -> int:
        return self.tail.prev.val
        
    def peekMax(self) -> int:
        while self.max_heap and -self.max_heap[0] not in self.node_map:
            heappop(self.max_heap)
        return -self.max_heap[0]
        
    def popMax(self) -> int:
        while self.max_heap and -self.max_heap[0] not in self.node_map:
            heappop(self.max_heap)

        val = -self.max_heap[0]

        node = self.node_map[val].pop()
        if not self.node_map[val]:
            del self.node_map[val]

        prev,nxt = node.prev,node.next
        prev.next = nxt
        nxt.prev= prev

        return val

        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()