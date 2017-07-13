/* preorder array of tree, node = queue.remove(), node = node.right */
public class Solution {
	public TreeNode flatten(TreeNode A) {
		Queue<TreeNode> queue = new LinkedList<TreeNode>();
		preorder(queue, A);

		if (queue.isEmpty())
			return A;

		TreeNode node = queue.remove();
		A = node;
		while (!queue.isEmpty()) {
			node.left = null;
			node.right = queue.remove();
			node = node.right;
		}
		return A;
	}


	// Let's try non recursive way
	public void preorder(Queue<TreeNode> queue, TreeNode node) {
		if (node == null)
			return;
		queue.add(node);
		preorder(queue, node.left);
		preorder(queue, node.right);
	}
}

/*
Given a binary tree, flatten it to a linked list in-place.

Example :
Given


         1
        / \
       2   5
      / \   \
     3   4   6
The flattened tree should look like:

   1
    \
     2
      \
       3
        \
         4
          \
           5
            \
             6
Note that the left child of all nodes should be NULL.
*/