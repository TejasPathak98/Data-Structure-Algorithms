# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = ListNode(-1)
        dummy = l3

        carry = 0 

        while l1 and l2:
            Sum = l1.val + l2.val + carry
            carry = Sum // 10
            l3.next = ListNode(Sum % 10)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        if l1:
            while l1:
                Sum = l1.val + carry
                carry = Sum // 10
                l3.next = ListNode(Sum % 10)
                l3 = l3.next
                l1 = l1.next
            
        if l2:
            while l2:
                Sum = l2.val + carry
                carry = Sum // 10
                l3.next = ListNode(Sum % 10)
                l3 = l3.next
                l2 = l2.next
        
        if carry:
            l3.next = ListNode(carry)

        return dummy.next
        



        
