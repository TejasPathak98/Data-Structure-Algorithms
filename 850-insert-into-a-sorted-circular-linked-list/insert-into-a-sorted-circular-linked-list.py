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
        
        if head.next == head:
            node = Node(insertVal)
            head.next = node
            node.next = head
            return head
        
        t = prev = head
        curr = head.next
        insertIt = False

        while True:
            if prev.val <= insertVal <= curr.val:
                insertIt = True
            elif prev.val > curr.val:
                if (insertVal >= prev.val and insertVal >= curr.val) or (insertVal <= curr.val and insertVal <= prev.val):
                    print("br")
                    insertIt = True
            
            if insertIt == True:
                print("br2")
                node = Node(insertVal)
                prev.next = node
                node.next = curr
                break
            
            prev = curr
            curr = curr.next

            if prev == head:
                break
        
        if not insertIt:
            print("br3") 
            while curr != head:
                prev = prev.next
                curr = curr.next
            node = Node(insertVal)
            prev.next = node
            node.next = curr

        return t

        