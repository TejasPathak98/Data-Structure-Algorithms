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


        #Step 1 : Interleaving nodes

        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node # Interleaving step
            curr = new_node.next

        #Step 2: Copying the random pointers:

        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        #Step3 : Extracting our list from the modified list

        curr = head
        dummy_node = Node(-1)
        dummy_copy = dummy_node

        while curr:
            dummy_copy.next = curr.next
            curr.next = curr.next.next #Restoring Original List Step
            curr = curr.next
            dummy_copy = dummy_copy.next

        return dummy_node.next