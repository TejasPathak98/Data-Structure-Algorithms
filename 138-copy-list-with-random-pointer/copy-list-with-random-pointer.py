"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.my_dict = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head in self.my_dict:
            return self.my_dict[head]
        
        if head is None:
            return None
        
        node = Node(head.val)
        self.my_dict[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
        