# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # if not head:
        #     return head
        
        # if not head.next:
        #     return None
        
        # count = 0
        # curr = head

        # while curr:
        #     count += 1
        #     curr = curr.next
        
        # pos = count - n
        # if pos == 0:
        #     return head.next

        # curr = head
        # counter = 0

        # while curr:
        #     counter += 1
        #     if counter == pos:
        #         break
        #     curr = curr.next

        # curr.next = curr.next.next

        # return head

        # #O(N) ; O(1) # Double Pass Solution


        dummy = ListNode(0,head)
        first = second = dummy  # This helps in edges where the first node has to be removed

        for _ in range(n + 1): #This helps to maintain a distance of exactly n nodes between the first and second pointer
            first = first.next

        #As the sliding window of second and first progresses, we reach a point where the first is at the end(Null) and the second is just before the Node to be removed
        while first: 
            first = first.next
            second = second.next 
        #this is because the gap between them always stays at n nodes, so the second is just before the nth node


        second.next = second.next.next

        return dummy.next
        