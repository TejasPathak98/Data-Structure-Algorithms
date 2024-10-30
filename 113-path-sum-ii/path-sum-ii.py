# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        temp = []
        
        def helper(root):
            if not root:
                return

            if root.left is None and root.right is None:
                temp.append(root.val)
                print(temp)
                if sum(temp) == targetSum:
                    ans.append(temp.copy())
                temp.pop()
                return
            
            temp.append(root.val)
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
            
            temp.pop()
        
        helper(root)
        return ans

            


        