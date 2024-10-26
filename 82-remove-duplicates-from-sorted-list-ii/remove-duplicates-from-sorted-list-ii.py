# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        my_set = set()
        my_set_2 = set()

        temp = head
        temp2 = head

        while temp:
            if temp.val not in my_set:
                my_set.add(temp.val)
            else:
                my_set_2.add(temp.val)
            temp = temp.next
        
        print(my_set_2)

        prev = temp2
        curr = temp2.next
        while curr:
            if curr.val in my_set_2:
                prev.next = curr.next
                curr = curr.next
            else:
                curr = curr.next
                prev = prev.next
        
        if temp2.val in my_set_2:
            return temp2.next
        else:
            return temp2
        

                

        
        