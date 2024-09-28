# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return None
        
        temp = head
        count = 0
        while temp:
            temp = temp.next
            count += 1

        pos = count - n + 1
        if pos == 1:
            return head.next

        cnt = 1
        temp2 = head
        while temp2:
            tp = temp2
            temp2 = temp2.next
            cnt += 1
            if cnt == pos:
                tp.next = tp.next.next
                break

        return head

