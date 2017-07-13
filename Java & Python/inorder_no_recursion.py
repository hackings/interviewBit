class Solution:
    def inorderTraversal(self, root):
        TreeNode current = root
        TreeNode node
        result = []
        while current:
            if current.left is None:
                result.append(current.val)
                current = current.right
            else:
                node = current.left
                while node.right && current != node.right:
                    node = node.right
                if node.right is None:
                    node.right = current
                    current = current.left
                else:
                    current = node.right
                    node.right = None
                    result.append(current.val)
                    current = current.right
        return result