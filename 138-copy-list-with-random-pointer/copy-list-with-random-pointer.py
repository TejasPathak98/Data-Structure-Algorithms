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
        self.list_dict = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        if head in self.list_dict:
            return self.list_dict[head]
        
        self.list_dict[head] = Node(head.val)

        self.list_dict[head].next = self.copyRandomList(head.next)

        self.list_dict[head].random = self.copyRandomList(head.random)

        return self.list_dict[head]


        