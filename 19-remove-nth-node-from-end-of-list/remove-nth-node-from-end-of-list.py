# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        
        dummy = ListNode(-1)
        
        temp = head
        cnt = 0
        while temp:
            temp = temp.next
            cnt += 1
        
        pos = cnt - n + 1
        dummy.next = prev = temp2 = head
        cnt2 = 0
        if pos == 1:
            return dummy.next.next
        
        

        while temp2:
            cnt2 += 1
            if cnt2 == pos:
                if temp2.next is None:
                    prev.next = None
                    break
                else:
                    prev.next = temp2.next
                    break
            prev = temp2
            temp2 = temp2.next
        
        return dummy.next
            

        