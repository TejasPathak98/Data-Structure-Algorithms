# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            count += 1
            if count == k:
                break
            curr = curr.next

        
        if count < k:
            return head
        
        other_node = curr.next
        curr.next = None

        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        

        new_head = prev

        while new_head.next:
            new_head = new_head.next
        
        new_head.next = self.reverseKGroup(other_node, k)

        return prev
