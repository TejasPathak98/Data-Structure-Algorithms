# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not head:
            return True
        
        def dfs(root,head):
            if head is None:
                return True
            
            if root is None:
                return False
            

            if root.val != head.val:
                return False
            
            l = dfs(root.left,head.next)
            r = dfs(root.right,head.next)

            return l or r
        
        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            
            if node.val == head.val and dfs(node,head):
                return True
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False        