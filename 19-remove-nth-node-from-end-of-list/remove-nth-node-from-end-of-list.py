# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        if head.next == None:
            return None
        
        temp = head 
        temp2 = head 
        count = 0

        while temp:
            temp = temp.next 
            count += 1 
        
        if count == n:
            return head.next

        pos = count - n - 1

        while pos:
            temp2 = temp2.next 
            pos -= 1
        
        temp2.next = temp2.next.next 

        return head



        
       
