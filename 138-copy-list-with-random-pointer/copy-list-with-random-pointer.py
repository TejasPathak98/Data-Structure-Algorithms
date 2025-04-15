"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        #Interleaving nodes

        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next
        

        #Copying the random pointer

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        
        #Extracting our desired list out

        curr = head
        dummy_node = Node(-1)
        dummy_copy = dummy_node

        while curr:
            dummy_copy.next  = curr.next
            curr.next = curr.next.next
            curr = curr.next
            dummy_copy = dummy_copy.next
        
        return dummy_node.next