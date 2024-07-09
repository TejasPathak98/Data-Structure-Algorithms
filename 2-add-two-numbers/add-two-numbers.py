# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l3 = temp = ListNode(0)
        carry = 0

        while l1 and l2:
            val = l1.val + l2.val + carry
            if val > 9:
                l3.next = ListNode(val%10)
                carry = val//10
            else:
                l3.next = ListNode(val)
                carry = 0
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        while l1:
            val = l1.val + carry
            if val > 9:
                l3.next = ListNode(val%10)
                carry = val// 10
            else:
                l3.next = ListNode(val)
                carry = 0
            l1 = l1.next
            l3 = l3.next
        
        while l2:
            val = l2.val + carry
            if val > 9:
                l3.next = ListNode(val%10)
                carry = val//10
            else:
                l3.next = ListNode(val)
                carry = 0
            l2 = l2.next
            l3 = l3.next
        
        if carry > 0:
            l3.next = ListNode(carry)

        return temp.next

            



        