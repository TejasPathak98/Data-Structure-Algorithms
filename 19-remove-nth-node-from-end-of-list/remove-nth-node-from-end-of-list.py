# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        if not head.next:
            return None
        
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next
        
        pos = count - n
        if pos == 0:
            return head.next

        curr = head
        counter = 0

        while curr:
            counter += 1
            if counter == pos:
                break
            curr = curr.next

        curr.next = curr.next.next

        return head
        