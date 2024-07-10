"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        
        def dfs(prev,curr):
            if not curr:
                return prev
            
            curr.prev = prev 
            prev.next = curr
            

            temp_next = curr.next

            tail = dfs(curr,curr.child)

            curr.child = None  

            return dfs(tail,temp_next)

        
        dummy = Node(0, None, head, None) 

        dfs(dummy,head)

        dummy.next.prev = None 
        return dummy.next