# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1,head)
        
        curr = head
        prev = dummy

        while curr and curr.next:
            npn = curr.next.next
            
            prev.next = curr.next

            curr.next.next = curr
            curr.next = npn

            prev = curr
            curr = npn

        return dummy.next
