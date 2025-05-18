# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return None
        
        if not head.next:
            return head
        
        curr = head
        count = 0

        while curr:
            count += 1
            if count == k:
                break
            curr = curr.next

        if count < k:
            return head

        temp = curr.next
        curr.next = None

        curr = head
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        curr = prev

        while curr.next:
            curr = curr.next
        
        curr.next = self.reverseKGroup(temp, k)

        return prev
        

