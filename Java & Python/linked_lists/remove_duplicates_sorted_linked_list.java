/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode a) {
        if (a == null)
            return a;
        ListNode root = a;
        while (a.next != null) {
            if (a.val == a.next.val)
                a.next = a.next.next;
            else
                a = a.next;
        }
        return root;
    }
}