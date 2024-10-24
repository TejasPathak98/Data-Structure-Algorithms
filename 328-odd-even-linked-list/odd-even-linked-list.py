# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        odd = ListNode(-1)
        even = ListNode(-1)
        odd_ptr = odd
        even_ptr = even
        idx = 1

        while head != None:
            if idx % 2 == 0:
                even_ptr.next = head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            idx += 1
            head = head.next
        
        even_ptr.next = None
        odd_ptr.next = even.next

        return odd.next