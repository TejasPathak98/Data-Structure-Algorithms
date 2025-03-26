# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    #     if  len(lists) == 0 or not lists:
    #         return None

    #     while len(lists) >= 2:
    #         x = lists.pop()
    #         if lists:
    #             y = lists.pop()
    #         else:
    #             return x
    #         lists.append(self.merge_two_lists(x,y))

    #     return lists[0]
        
    # def merge_two_lists(self,l1,l2):
    #     if not l1 and not l2:
    #         return None
    #     if not l1:
    #         return l2
    #     if not l2:
    #         return l1
        
    #     l3 = dummy = ListNode(-1)


    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             l3.next = l1
    #             l1 = l1.next
    #         else:
    #             l3.next = l2
    #             l2 = l2.next
    #         l3 = l3.next
        
    #     if l1:
    #         l3.next = l1
    #     elif l2:
    #         l3.next = l2
        
    #     return dummy.next


    #     while len(lists) >= 2:
    #         x = lists.pop()
    #         if lists:
    #             y = lists.pop()
    #         else:
    #             return x
    #         lists.append(self.merge_two_lists(x,y))

    #     return lists[0]

    #O (Nk)

        if  len(lists) == 0 or not lists:
            return None
        
        min_heap = []

        for idx,node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val,idx,node))
        
        dummy = curr = ListNode(-1)

        while min_heap:
            val,idx,node = heapq.heappop(min_heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val,idx,node.next))
        
        return dummy.next

    
    
        



