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
        
        dummy = l3 = ListNode(-1)
        Sum = 0
        carry = 0

        while l1 and l2:
            Sum = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10

            l3.next = ListNode(Sum)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        
        while l1:
            Sum = (l1.val + carry) % 10
            carry = (l1.val + carry) // 10

            l3.next = ListNode(Sum)
            l1 = l1.next
            l3 = l3.next

        while l2:
            Sum = (l2.val + carry) % 10
            carry = (l2.val + carry) // 10
            l3.next = ListNode(Sum)
            l2 = l2.next
            l3 = l3.next

        if carry > 0:
            l3.next = ListNode(carry)
        
        return dummy.next