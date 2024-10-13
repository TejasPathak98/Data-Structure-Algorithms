"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node
        
        t = prev = head
        curr = head.next
        insertIt = False

        while True:
            if prev.val <= insertVal <= curr.val:
                insertIt = True
            elif prev.val > curr.val:
                if (insertVal >= prev.val and insertVal >= curr.val) or (insertVal <= curr.val and insertVal <= prev.val):
                    insertIt = True
            
            if insertIt == True:
                node = Node(insertVal)
                prev.next = node
                node.next = curr
                break
            
            prev = curr
            curr = curr.next

            if prev == head:
                break
        
        if not insertIt:
            while curr != head:
                prev = prev.next
                curr = curr.next
            node = Node(insertVal)
            prev.next = node
            node.next = curr

        return t

        