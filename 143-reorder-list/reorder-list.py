# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return
        
        curr = head
        slow = fast = curr

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        l1 = head
        l2 = prev

        while l2.next:
            t1= l1.next
            t2 = l2.next

            l1.next = l2
            l2.next = t1

            l1 = t1
            l2 = t2
        
        
        
