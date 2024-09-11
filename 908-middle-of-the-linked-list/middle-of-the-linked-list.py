# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        if head.next is None:
            return head


        temp = head
        count = 0

        while temp:
            temp = temp.next
            count += 1
        
        if count % 2 == 1:
            k = count//2 + 1
            temp2 = head
            c = 1
            while temp2 and c < k:
                temp2 = temp2.next 
                c += 1
                if c == k:
                    return temp2
        
        else:
            k = count//2
            temp2 = head
            c = 0
            while temp2 and c < k:
                temp2 = temp2.next 
                c += 1
                if c == k:
                    return temp2
        

        
        
        print(count)

        