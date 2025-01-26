# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None

        count = 0
        curr = head
        var = head

        while curr:
            count += 1
            curr = curr.next
        
        if count == n:
            return head.next

        pos = count - n - 1

        while var and pos:
            var = var.next
            pos -= 1
        
        var.next = var.next.next
        return head
        




        