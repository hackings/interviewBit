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
	public int isValidBST(TreeNode root) {
		if (!validBST(root, Integer.MIN_VALUE, Integer.MAX_VALUE))
			return 0;
		else
			return 1;
		
	}

	public boolean validBST(TreeNode root, int min, int max) {
		if (root == null)
			return true;
		return (min < root.val && root.val < max) &&
				validBST(root.left, min, root.val) &&
				validBST(root.right, root.val, max);
	}
}

/*
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
Both the left and right subtrees must also be binary search trees.
Example :

Input : 
   1
  /  \
 2    3

Output : 0 or False


Input : 
  2
 / \
1   3

Output : 1 or True 
Return 0 / 1 ( 0 for false, 1 for true ) for this problem
*/