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
        
        f = dummy = ListNode(-1)
        carry = 0

        while l1 and l2:
            x = l1.val
            y = l2.val
            st = x + y + carry
            list_sum = (st) % 10
            carry = (st) // 10

            dummy.next = ListNode(list_sum)
            dummy = dummy.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            st = l1.val + carry
            list_sum = (st) % 10
            carry = (st) // 10

            dummy.next = ListNode(list_sum)
            dummy = dummy.next
            l1 = l1.next

        while l2:
            st = l2.val + carry
            list_sum = (st) % 10
            carry = (st) // 10

            dummy.next = ListNode(list_sum)
            dummy = dummy.next
            l2 = l2.next

        if carry > 0:
            dummy.next = ListNode(carry)
            dummy = dummy.next

        return f.next



        