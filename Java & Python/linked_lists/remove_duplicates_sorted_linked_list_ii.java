/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode root) {
    	
    	ListNode head = new ListNode(0);
    	ListNode result = head;

		while (root != null) {
			if (root.next != null && root.val == root.next.val) {
				int duplicate = root.val;
				while (root != null && root.val == duplicate)
					root = root.next;
			}
			else {
				head.next = root;
				head = head.next;
				root = root.next;
			}
		}
		head.next = null;
		return result.next;
    }
}