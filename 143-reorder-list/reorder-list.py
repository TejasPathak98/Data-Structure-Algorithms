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
        if not head or not head.next:
            return head

        slow = head
        fast = head
        prev = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        prev.next = None

        def reverse_helper(head):
            prev = None
            Next = None
            curr = head

            while curr:
                Next = curr.next
                curr.next = prev
                prev = curr
                curr = Next

            return prev

        slow = reverse_helper(slow)
        dummy = ListNode(-1)
        dummy.next = head
        curr2 = slow
        curr1 = head
        prev = curr1

        while curr1.next:
            temp1 = curr1.next
            temp2 = curr2.next

            curr1.next = curr2
            curr2.next = temp1
            curr1 = curr1.next.next
            curr2 = temp2
        
        if curr2:
            curr1.next = curr2
        
        return dummy.next





