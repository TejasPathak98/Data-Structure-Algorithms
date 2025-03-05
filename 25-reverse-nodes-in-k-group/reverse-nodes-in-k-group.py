# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr:
            count += 1
            if count == k:
                break
            curr = curr.next
        
        if count < k:
            return head
        
        other_part = curr.next
        curr.next = None

        prev = None
        new_curr = head

        while new_curr:
            temp = new_curr.next
            new_curr.next = prev
            prev = new_curr
            new_curr = temp
        
        new_curr2 = prev

        while new_curr2.next:
            new_curr2 = new_curr2.next

        
        new_curr2.next = self.reverseKGroup(other_part, k)

        return prev