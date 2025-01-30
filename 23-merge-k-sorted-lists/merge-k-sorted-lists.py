# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0 or lists is None:
            return None
        
        def merge_lists(l1,l2):
            node = head = ListNode(0)

            while l1 and l2:
                if l1.val < l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next
                node = node.next
            
            if l1:
                node.next = l1
            if l2:
                node.next = l2
            
            return head.next

        while len(lists) > 1:
            temp = []
            for i in range(0,len(lists),2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                list3 = merge_lists(list1, list2)
                temp.append(list3)
            lists = temp
        
        return lists[0]




        