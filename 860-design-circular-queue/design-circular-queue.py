class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [-1] * k
        self.sz = k
        self.cnt = 0
        self.head_idx = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        
        insert_idx = (self.head_idx + self.cnt) % self.sz
        self.q[insert_idx] = value
        self.cnt += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        
        self.head_idx = (self.head_idx + 1) % self.sz
        self.cnt -= 1
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.q[self.head_idx % self.sz]
        
    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        
        return self.q[(self.head_idx + self.cnt - 1) % self.sz]
        

    def isEmpty(self) -> bool:
        return self.cnt == 0
        

    def isFull(self) -> bool:
        return self.cnt == self.sz


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()