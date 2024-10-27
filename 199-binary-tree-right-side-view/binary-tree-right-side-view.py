# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        my_dict = defaultdict(int)

        def helper(root,level):
            if root is None:
                return
            
            my_dict[level] = root.val
            helper(root.left, level + 1)
            helper(root.right, level + 1)
        
        helper(root,0)

        ans = []
        low = min(my_dict.keys())
        high = max(my_dict.keys())
        for i in range(low,high + 1):
            ans.append(my_dict[i])
        
        return ans
