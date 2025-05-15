# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummmy = ListNode(0,head)
        prev = dummmy

        if left == right or (not head or not head.next):
            return head
        
        for _ in range(left - 1):
            prev = prev.next
        
        curr = prev.next

        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        return dummmy.next

