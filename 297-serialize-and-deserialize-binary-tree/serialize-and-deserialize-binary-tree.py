# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return self.preorder(root)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = deque(data.split("|"))
        return self.build(values)
    
    def build(self,values):
        if not values:
            return None
        
        val = values.popleft()

        if val[1] == "X":
            return None
        
        root = TreeNode(int(val[1:]))
        root.left = self.build(values)
        root.right = self.build(values)
        return root


    def preorder(self,root):
        if root is None:
            return "#X"
        
        return f"#{root.val}|{self.preorder(root.left)}|{self.preorder(root.right)}"
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))