# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = l1
        carry = 0

        while l1 and l2:
            prev = l1
            Sum = l1.val + l2.val + carry
            l1.val = Sum % 10
            carry = Sum // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            prev = l1
            Sum = l1.val  + carry
            l1.val = Sum % 10
            carry = Sum // 10
            l1 = l1.next

        while l2:
            Sum = l2.val  + carry
            prev.next = ListNode(Sum % 10)
            carry = Sum // 10
            l2 = l2.next
            prev = prev.next
        
        if carry:
            prev.next = ListNode(carry)

        return dummy.next
