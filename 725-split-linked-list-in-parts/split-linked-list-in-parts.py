# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        
        n = 0
        temp = head
        while temp:
            temp = temp.next
            n += 1
        
        base = n // k
        remain = n % k

        res = []
        curr = head

        while k:
            prev_head = curr

            if remain > 0:
                size = base
                remain -= 1
            else:
                size = base - 1
            
            while curr and size:
                curr = curr.next
                size -= 1

            if curr:
                next_curr = curr.next
                curr.next = None
                curr = next_curr
            
            res.append(prev_head)
            k -= 1
        
        return res


