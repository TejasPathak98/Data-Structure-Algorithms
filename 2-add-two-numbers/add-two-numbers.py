# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-1)
        l3 = dummy

        Sum = 0
        carry = 0

        while l1 and l2:
            Sum = l1.val + l2.val + carry
            l3.next = ListNode(Sum  % 10)
            carry = Sum // 10
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            Sum = l1.val + carry
            l3.next = ListNode(Sum  % 10)
            carry = Sum // 10
            l3 = l3.next
            l1 = l1.next
        
        while l2:
            Sum = l2.val + carry
            l3.next = ListNode(Sum  % 10)
            carry = Sum // 10
            l3 = l3.next
            l2 = l2.next
        
        if carry:
            l3.next = ListNode(carry)

        return dummy.next
        
