# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        number = ''
        stack = []

        for i in s:
            if i in '()':
                if i == '(' and number:
                    stack.append(TreeNode(int(number)))
                    number = ''
                elif i == ')':
                    if number:
                        node = TreeNode(int(number))
                        number = ''
                    else:
                        node = stack.pop()
                    
                    if stack:
                        parent = stack[-1]
                        if not parent.left:
                            parent.left = node
                        else:
                            parent.right = node
            else:
                number += i

        if number:
            stack = [TreeNode(int(number))]
        
        return stack[0]


        