# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        dummy = ListNode(-1)
        prev = dummy
        prev.next = list1

        counter = -1
        pre_break = None

        while prev:
            counter += 1
            if counter == a:
                break
            prev = prev.next

        
        pre_break = prev

        curr = prev.next

        for _ in range(b - a):
            curr = curr.next
        
        later_half = curr.next

        pre_break.next = None
        curr.next = None

        pre_break.next = list2

        curr = pre_break.next

        while curr.next:
            curr = curr.next
        
        curr.next = later_half

        return dummy.next


