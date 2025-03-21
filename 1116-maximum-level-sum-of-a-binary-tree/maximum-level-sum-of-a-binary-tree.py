# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        max__sum = float("-inf")
        level_sum = 0
        the_level = 0
        ans_level = -1

        while queue:
            if level_sum > max__sum and the_level > 0:
                max__sum = level_sum
                ans_level = the_level
                print(level_sum,ans_level)
            
            level_sum = 0
            the_level += 1
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                

        if level_sum > max__sum:
            ans_level = the_level


        return ans_level


        