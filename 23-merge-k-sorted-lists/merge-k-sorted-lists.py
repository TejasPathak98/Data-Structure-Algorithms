# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #we take the heads of all linked lists and put them into a heap based on their vals and get the first one out
        #then we use that to start the final list and we add its next pointer also to the heap
        # in the same way, we continue

        if not lists or len(lists) == 0:
            return None
        
        min_heap = []

        for idx,node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val,idx,node))
        
        dummy = curr = ListNode(-1)

        while min_heap:
            _,idx,node = heapq.heappop(min_heap)
            if node:
                curr.next = node
                curr = curr.next
                if node.next:
                    heapq.heappush(min_heap, (node.next.val,idx,node.next))
        

        return dummy.next




