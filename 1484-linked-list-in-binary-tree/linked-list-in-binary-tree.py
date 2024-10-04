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
        d = deque()
        d.append(root)
        def dfs(root,head):
            if head is None:
                return True
            if root is None or root.val != head.val:
                return False
            return dfs(root.left,head.next) or dfs(root.right,head.next)
        while d:
            size = len(d)
            for _ in range(size):
                node = d.popleft()
                if node.val == head.val and dfs(node,head):
                    return True
                if node.left:
                    d.append(node.left)
                if node.right:
                    d.append(node.right)
        return False
        