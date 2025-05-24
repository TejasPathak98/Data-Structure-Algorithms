# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        node_val = []
        curr = head

        while curr:
            node_val.append(curr.val)
            curr = curr.next
        
        n = len(node_val)
        max_sum = -float('inf')

        l = 0
        r = len(node_val) - 1

        while l < r:
            max_sum = max(max_sum,(node_val[l] + node_val[r]))
            l += 1
            r -= 1

        return max_sum
