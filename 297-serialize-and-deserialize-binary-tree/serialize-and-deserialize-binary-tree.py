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

        return self.PreOrder(root)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        queue = deque(data.split("|"))
        return self.build(queue)
    

    def build(self,queue):

        if not queue:
            return None
        
        val = queue.popleft()

        if val[1] == "X":
            return None
        
        root = TreeNode(int(val[1:]))
        root.left = self.build(queue) #The queue will implicitly deal with the elements in the sense that left elements will go to left subtree and right to right
        root.right = self.build(queue)
        return root

    def PreOrder(self,root):
        if root is None:
            return "#X"
        else:
            return f"#{root.val}|{self.PreOrder(root.left)}|{self.PreOrder(root.right)}"
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))