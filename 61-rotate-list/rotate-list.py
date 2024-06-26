# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        
        ptr = head
        newHead = head
        count = 0 

        while newHead:
            newHead = newHead.next
            count += 1 
        
        k = k % count 

        while k > 0:
            ptr = head

            while ptr.next.next:
                ptr = ptr.next 
            
            ptr.next.next = head
            head = ptr.next
            ptr.next = None 

            k -= 1

        return head 
        