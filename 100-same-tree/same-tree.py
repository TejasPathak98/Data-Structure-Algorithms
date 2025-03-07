# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # if not p or not q:
        #     return False
        # if p.val != q.val:
        #     return False
        
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        #O(N) ; O(N)

        # queue = deque([(p,q)])

        # while queue:
        #     n1,n2 = queue.popleft()

        #     if n1 is None and n2 is None:
        #         continue
            
        #     if  n1 is None or n2 is None or n1.val != n2.val:
        #         return False
            
        #     queue.append((n1.left,n2.left))
        #     queue.append((n1.right,n2.right))
        
        # return True

        # #O(N) ; O(N) ....Better than recursion for bigger trees where N > 1000


        stack = [(p,q)]

        while stack:
            n1,n2 = stack.pop()

            if n1 is None and n2 is None:
                continue
            
            if  n1 is None or n2 is None or n1.val != n2.val:
                return False

            stack.append((n1.left,n2.left))
            stack.append((n1.right,n2.right))
        
        return True


    