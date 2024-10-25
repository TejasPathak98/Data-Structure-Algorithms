# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head
        cnt = 0
        val1 = val2 = -1

        while temp:
            cnt += 1
            if cnt == k:
                val1 = temp.val
                node = temp
            temp = temp.next
        
        var = cnt - k + 1
        
        cnt2 = 0
        temp2 = head

        while temp2:
            cnt2 += 1
            if cnt2 == var:
                node.val = temp2.val
                temp2.val = val1
                break
            temp2 = temp2.next
        
        return head

        
        

            

        