class Solution:
    def inorderTraversal(self, root):
       self.values = []
       self.traverse(root)
       return self.values

    def traverse(self, root):

        if root.left is None and root.right is None:
            self.values.append(root.val)
            return

        if root.left:
            self.traverse(root.val)
        
        self.values.append(root.val)

        if root.right:
            self.traverse(root.right)
