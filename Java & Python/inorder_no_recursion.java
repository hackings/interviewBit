/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
	public ArrayList<Integer> inorderTraversal(TreeNode A) {
		TreeNode current = A;
		TreeNode node;
		ArrayList<Integer> result = new ArrayList<Integer>();

		while (current) {
			if (!current.left) {
				result.add(current.val);
				current = current.right;
			}
			else {
				node = current.left;
				while (node.right && !current.equals(node.right)) 
					node = node.right;

				if (!node.right) {
					node.right = current;
					current = current.left;
				}
				else {
					current = node.right;
					node.right = null;
					result.add(current.val);
					current = current.right;
				}
				
			}
		}
		return result;
	}
}