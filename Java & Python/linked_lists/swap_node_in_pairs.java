/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode a) {
        ListNode res = new ListNode(0);
        res.next = a;
        ListNode root = res;
        while (root.next != null && root.next.next != null) {
            root.next = swap(root.next, root.next.next);
            root = root.next.next;
        }
        return res.next;

    }

    public ListNode swap(ListNode p1, ListNode p2) {
        p1.next = p2.next;
        p2.next = p1;
        return p2;
    }
}

/*
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
*/