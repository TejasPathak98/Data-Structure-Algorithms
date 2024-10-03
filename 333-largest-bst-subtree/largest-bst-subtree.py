# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        max_ans = 0
        
        def isBST(root):
            if root is None:
                return True
            
            mi = float('-inf')
            ma = float('inf')

            def helper(root,mi,ma):
                if root is None:
                    return True
                if root.val <= mi or root.val >= ma:
                    return False
                return helper(root.left,mi,root.val) and helper(root.right,root.val,ma)
            
            return helper(root,mi,ma)
        
        def CountOfNodes(root):
            if root is None:
                return 0
            l = CountOfNodes(root.left)
            r = CountOfNodes(root.right)
            return l + r + 1
        
        def dfs(root):
            nonlocal max_ans
            if root is None:
                return
            
            print("fr")

            if isBST(root) == True:
                print("br")
                max_ans = max(max_ans,CountOfNodes(root))
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return max_ans

        
        