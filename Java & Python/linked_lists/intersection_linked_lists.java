/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
	public ListNode getIntersectionNode(ListNode a, ListNode b) {
		int len_a = 0, len_b = 0;
		ListNode a_copy = a;
		ListNode b_copy = b;
		if (a == null || b == null)
			return null;
			
		while (a_copy != null) {
			++len_a;
			a_copy = a_copy.next;
		}
		while (b_copy != null) {
			++len_b;
			b_copy = b_copy.next;
		}
		int diff = Math.abs(len_a-len_b);
		int count = 0;
		if (len_a > len_b) {
			while (count < diff) {
				++count;
				a = a.next;
			}
		}
		else {
			while (count < diff) {
				++count;
				b = b.next;
			}
		}

		while (a != null && b != null) {
			if (a.equals(b)) {
				return a;
			}
			a = a.next;
			b = b.next;
		}
		return null;

	}
}
