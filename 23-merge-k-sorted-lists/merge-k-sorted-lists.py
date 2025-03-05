# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def print_linked_list(head):
            curr = head
            while curr:
                print(curr.val,end = "->")  # Default newline after each print
                curr = curr.next
            print("None")

        # Linked list: 1 -> 2 -> 3 -> 4 -> 5

        if not lists:
            return None
        if len(lists) == 0:
            return None
        
        def merge(l1,l2):
            if not l1 and not l2:
                return None
            if not l1:
                return l2
            if not l2:
                return l1
            
            l3 = ListNode(-1)
            dummy = l3

            while l1 and l2:
                if l1.val <= l2.val:
                    l3.next = l1
                    l1 = l1.next
                else:
                    l3.next = l2
                    l2 = l2.next
                l3 = l3.next

            if l1:
                l3.next = l1
            if l2:
                l3.next = l2
            
            return dummy.next
        
        stack = []

        for l in lists:
            stack.append(l)
        
        while len(stack) > 1:
            x = stack.pop()
            y = stack.pop()
            z = merge(x,y)
            stack.append(z)
        
        return stack.pop()
