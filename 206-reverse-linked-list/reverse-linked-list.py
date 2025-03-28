# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # prev_node = None
        # next_node = None
        # curr_node = head

        # while curr_node:
        #     next_node = curr_node.next
        #     curr_node.next = prev_node
        #     prev_node = curr_node
        #     curr_node = next_node
        
        # return prev_node

        # #O(N) ; O(1)

        if not head or not head.next:
            return head

        #Reverse the rest of the list
        new_head = self.reverseList(head.next)

        #The real reversal of next pointer step
        head.next.next = head

        head.next = None

        return new_head

        