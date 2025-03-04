# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # if not l1 and not l2:
        #     return None
        # if not l1:
        #     return l2
        # if not l2:
        #     return l1
        
        # new_head = l3 = ListNode(-101)

        # while l1 and l2:
        #     if l1.val >= l2.val:
        #         l3.next = ListNode(l2.val)
        #         l2 = l2.next
        #     else:
        #         l3.next = ListNode(l1.val)
        #         l1 = l1.next
        #     l3 = l3.next
        
        # while l1:
        #     l3.next = ListNode(l1.val)
        #     l3 = l3.next
        #     l1 = l1.next
        
        # while l2:
        #     l3.next = ListNode(l2.val)
        #     l3 = l3.next
        #     l2 = l2.next

        # return new_head.next


        # #O(N) ; O(N)


        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        new_head = l3 = ListNode(-101) 

        while l1 and l2:
            if l1.val >= l2.val:
                l3.next = l2
                l2 = l2.next
            else:
                l3.next = l1
                l1 = l1.next
            l3 = l3.next
        
        if l1:
            l3.next = l1
        elif l2:
            l3.next = l2
        
        return new_head.next

        