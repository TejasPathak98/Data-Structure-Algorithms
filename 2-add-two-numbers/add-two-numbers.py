# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = curr = ListNode(-1)
        the_sum = 0
        carry = 0

        while l1 and l2:
            the_sum = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            curr.next = ListNode(the_sum)
            l1 = l1.next
            l2 = l2.next
            curr = curr.next

        while l1:
            the_sum = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10
            curr.next = ListNode(the_sum)
            l1 = l1.next
            curr = curr.next
        
        while l2:
            the_sum = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            curr.next = ListNode(the_sum)
            l2 = l2.next
            curr = curr.next
        
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next

        #O(N) ; O(N)


        