# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = defaultdict(list)

        def helper(node,level):
            nonlocal ans
            if node is None:
                return

            ans[level].append(node.val)

            if node.left:
                helper(node.left,level + 1)
            if node.right:
                helper(node.right,level + 1)

        result = []
        helper(root,0)

        for k,v in ans.items():
            if k % 2 == 0:
                result.append(v)
            else:
                result.append(v[::-1])

        return result 