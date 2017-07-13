/* Put bst inorder, sort inorder, compare both arrays */
public class Solution {
	public ArrayList<Integer> recoverTree(TreeNode root) {
		ArrayList<Integer> res = new ArrayList<Integer>();
		ArrayList<Integer> inorder = new ArrayList<Integer>();

		inorder(inorder, root);

		ArrayList<Integer> sorted = new ArrayList<Integer>(inorder);
		Collections.sort(sorted);

		int i = 0;
		for (int num : sorted) {
			if (inorder.get(i) != num)
				res.add(num);
			++i;
		}
		return res;
	}

	public void inorder(ArrayList<Integer> in, TreeNode root) {
		if (root == null)
			return;
		inorder(in, root.left);
		in.add(root.val);
		inorder(in, root.right);
	}
}

/*
Two elements of a binary search tree (BST) are swapped by mistake.
Tell us the 2 values swapping which the tree will be restored.

 Note:
A solution using O(n) space is pretty straight forward. Could you devise a constant space solution? 
Example :


Input : 
		 1
		/ \
	       3   2

Output : 
	   [1, 2]

Explanation : Swapping 1 and 2 will change the BST to be 
		 2
		/ \
	       3   1   
which is a valid BST   
*/
