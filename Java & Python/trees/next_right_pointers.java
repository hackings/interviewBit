/* 2 queue's, one for first level, one for second level
  while either one of them are not empty, link to next item
  set prev = null every time
  when finished with first level, add children to queue 2
 */
/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
    	TreeLinkNode node, prev = null;
    	Queue<TreeLinkNode> queue1 = new LinkedList<>();
    	Queue<TreeLinkNode> queue2 = new LinkedList<>();

    	if (root == null)	
    		return;
    	queue1.add(root);
    	
    	while (!queue1.isEmpty() || !queue2.isEmpty()) {
    		prev = null;
    		while (!queue1.isEmpty()) {
    			node = queue1.remove();
    			if (prev != null)
    				prev.next = node;
    			// prev = node;
    			if (node.left != null)
    				queue2.add(node.left);
    			if (node.right != null)
    				queue2.add(node.right);
    		}
    		prev = null;
    		while(!queue2.isEmpty()) {
    			node = queue2.remove();
    			if (prev != null)
    				prev.next = node;
    			prev = node;
    			if (node.left != null)
    				queue1.add(node.left);
    			if (node.right != null)
    				queue1.add(node.right);
    		}
    	}
    }
}
/*
Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

 Note:
You may only use constant extra space.
Example :

Given the following binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7
After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL
*/