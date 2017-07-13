private int minLenSumPathBST(final TreeNode root, final int sum, final int len) {
    if (root == null) 
        return Integer.MAX_VALUE;
    

    final int remainingSum = sum - root.key;
    if (remainingSum == 0 && root.left == null && root.right == null) 
        return len + 1;
    
    else if (remainingSum <= root.key) {
        int l = minLenSumPathBST(root.left, remainingSum, len + 1);
        if (l == Integer.MAX_VALUE) {
            l = minLenSumPathBST(root.right, remainingSum, len + 1);
        }

        return l;
    }
    else {
        int l = minLenSumPathBST(root.right, remainingSum, len + 1);
        if (l == Integer.MAX_VALUE) {
            l = minLenSumPathBST(root.left, remainingSum, len + 1);
        }

        return l;
    }
}

/*
Given a BST, find out the minimum length form root to leaf with sum S. Note that: 
a) Path from root to leaf node. 
b) Sum of node of the path is S. 
c) if multiple such path exist, print minimum length path. 
d) What is advantage of BST rather than BT used for this algorithm, how it improve the performance. in BST, is it required to explore both side ?

With a BST we have an added advantage that we know all the nodes on the left is less than the current node and all the nodes on the right are greater than the current node. 

So, while doing a DFS to search for a minLen path in a BST we actually can take informed decision at each node to either go left or right based on the remaining sum to search and hence cutting down the search space in half in average case. This will guarantee finding the minimum length path because - 

1) If current node value is equal to sum and it is a leaf node than we have a complete path. If it is not a leaf then we need to find a zero sum minLen path along one of its subtrees. 

2) If current node value is greater than (or equal to) the remaining sum i.e. value>=(sum-value) then we should search for new sum=(sum-value) in the left sub tree because - if a path exists in the left subtree, it must be the shorter than any possible path in the right subtree, since all nodes at left is smaller than those at right. 

3) Similarly, If current node value is smaller than the remaining sum i.e. value<(sum-value) then we should search for new sum=(sum-value) in the right sub tree because - if a path exists in the right subtree, it must be the shorter than any possible path in the right subtree, since all nodes at right is greater than those at left. 

So, average case complexity will be improved to O(lgn) with a complete BST. However, the worst case complexity will be O(n) in case where we have to search both left and right subtree for the remaining sum.

*/