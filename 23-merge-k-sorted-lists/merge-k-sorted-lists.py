# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        dummy = ListNode(-1)
        curr = dummy

        min_heap = []
        var = 1

        for idx,l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val,idx,l))
        
        while min_heap:
            _,idx,node = heappop(min_heap)
            if node:
                curr.next = node
                curr = curr.next
                if node.next:
                    heappush(min_heap, (node.next.val,idx,node.next))

        return dummy.next