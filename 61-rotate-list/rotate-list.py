# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        total_count = 0
        curr = head

        while curr:
            total_count += 1
            curr = curr.next
        
        k = k % total_count
        if k == 0:
            return head

        cut_off = total_count - k
        curr = head
        prev = head

        while curr and cut_off:
            prev = curr
            cut_off -= 1
            curr = curr.next
        
        temp = prev.next
        prev.next = None
        new_head = temp
        curr = temp

        while curr.next:
            curr = curr.next

        curr.next = head
        return new_head




