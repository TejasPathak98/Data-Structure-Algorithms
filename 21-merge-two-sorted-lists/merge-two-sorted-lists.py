# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2 
        if not list2:
            return list1 
        
        list3 = ListNode(0)
        h = list3

        print(list3.val)
        
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = ListNode(list1.val)
                list1 = list1.next 
            else:
                list3.next = ListNode(list2.val)
                list2 = list2.next
            list3 = list3.next
        
        while list1:
            list3.next = ListNode(list1.val)
            list1 = list1.next 
            list3 = list3.next

        while list2:
            list3.next = ListNode(list2.val)
            list2 = list2.next 
            list3 = list3.next
        
        return h.next





        