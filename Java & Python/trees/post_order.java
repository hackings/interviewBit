/* Use 2 stacks for post order */
public class Solution {
	public ArrayList<Integer> postorderTraversal(TreeNode A) {
		Stack<TreeNode> stack1 = new Stack<>();
		Stack<TreeNode> stack2 = new Stack<>();
		ArrayList<Integer> res = new ArrayList<Integer>();
		TreeNode node;
		if (A == null)
			return null;

		stack1.push(A);
		while (!stack1.isEmpty()) {
			node = stack1.pop();
			stack2.push(node);

			if (node.left != null)
				stack1.push(node.left);
			if (node.right != null)
				stack1.push(node.right);
		}
		while (!stack2.isEmpty()) {
			node = stack2.pop();
			res.add(node.val);
		}
		return res;
	}
}