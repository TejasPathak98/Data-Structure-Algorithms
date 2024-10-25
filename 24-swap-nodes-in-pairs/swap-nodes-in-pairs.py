# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1,head)

        prev = dummy
        curr = head

        while curr and curr.next:
            npn = curr.next.next
            second_node = curr.next

            second_node.next = curr
            curr.next = npn
            prev.next = second_node

            prev = curr
            curr = npn
        
        return dummy.next
        