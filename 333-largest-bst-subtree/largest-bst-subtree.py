# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return True,0,float('inf'),float('-inf')

            isleftBST,leftSize,leftMin,leftMax = dfs(root.left)
            isrightBST,rightSize,rightMin,rightMax = dfs(root.right)

            if isleftBST and isrightBST and leftMax < root.val < rightMin:
                size = leftSize + rightSize + 1
                minval = min(root.val,leftMin)
                maxval = max(root.val,rightMax)

                return True,size,minval,maxval 
            else:
                return False,max(leftSize,rightSize),0,0
            
        return dfs(root)[1]