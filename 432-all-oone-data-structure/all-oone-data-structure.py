class Node:
    def __init__(self,freq):
        self.freq = freq
        self.keys = set()
        self.next = None
        self.prev = None

class AllOne:

    def __init__(self):
        self.map = {}
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _create_node(self,prev_node,freq):

        new_node = Node(freq)
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

        return new_node

    def _remove_node_if_required(self,node):

        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.map:
            current_node = self.map[key]

            current_freq = current_node.freq
            new_freq = current_freq + 1

            current_node.keys.remove(key)

            if current_node.next == self.tail or current_node.next.freq != new_freq:
                next_node = self._create_node(current_node,new_freq)
                next_node.keys.add(key)
                self.map[key] = next_node
            else:
                current_node.next.keys.add(key)
                self.map[key] = current_node.next
            
            self. _remove_node_if_required(current_node)

        else:
            if self.head.next.freq != 1 or self.head.next == self.tail:
                new_node = self._create_node(self.head, 1)
                new_node.keys.add(key)
                self.map[key] = new_node
            else:
                self.head.next.keys.add(key)
                self.map[key] = self.head.next
            

    def dec(self, key: str) -> None:
        if key not in self.map:
            return
        
        current_node = self.map[key]
        current_freq = current_node.freq
        new_freq = current_freq - 1
        current_node.keys.remove(key)

        if new_freq == 0:
            self.map.pop(key)
            self._remove_node_if_required(current_node)
            return
        else:
            if current_node.prev == self.head or current_node.prev.freq != new_freq:
                new_node = self._create_node(current_node.prev,new_freq)
                new_node.keys.add(key)
                self.map[key] = new_node
            else:
                current_node.prev.keys.add(key)
                self.map[key] = current_node.prev


            self. _remove_node_if_required(current_node)

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))
        
    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        else:
            return next(iter(self.head.next.keys))
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()