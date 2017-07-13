/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
	public ListNode reverseBetween(ListNode A, int m, int n) {
		int i = 1;
		ListNode root = new ListNode(0);
		ListNode prev, next, current, start, end;

		root.next = A;
		prev = root;
		
		while (i < m) {
			prev = prev.next;
			++i;
		}
		start = prev;
		end = prev.next;

		// start reversing
		prev = prev.next;
		current = prev.next;
		while (i < n) {
			next = current.next;
			current.next = prev;
			prev = current;
			current = next;
			++i;
		}
		start.next = prev;
		end.next = current;
		return root.next;
	}
}