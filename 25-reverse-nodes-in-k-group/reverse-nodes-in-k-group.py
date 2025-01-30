# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        node = ListNode(-1)
        node.next = begin = start = head
        count = 0
        occ = 1
        prev_pos = None

        def reverse_helper(the_list):
            curr = the_list
            temp = None
            prev = None
            count = k

            while curr and count:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count -= 1
            
            return prev

        while start:
            count += 1
            if count == k:
                temp = start.next
                start = reverse_helper(begin)
                if occ > 1:
                    prev_pos.next = start
                elif occ == 1:
                    node.next = head = start
                occ += 1
                while start.next:
                    start = start.next
                start.next = temp
                prev_pos = start
                count = 0
                begin = temp
            start = start.next


        return node.next