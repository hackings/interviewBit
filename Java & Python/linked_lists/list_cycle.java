/**
 * Definition for singly-linked list.
 * class ListNode {
 *     public int val;
 *     public ListNode next;
 *     ListNode(int x) { val = x; next = null; }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode root) {
        if (root == null || root.next == null)
            return null;
        ListNode p1 = root;
        ListNode p2 = root;
        boolean isCycle = false;

        while (p1 != null && p2 != null) {
            p1 = p1.next;
            if (p2.next == null)
                return null;
            p2 = p2.next.next;

            if (p1 == p2) {
                isCycle = true;
                break;
            }
        }
        if (!isCycle)
            return null;
        p1 = root;
        while (p1 != p2) {
            p1 = p1.next;
            p2 = p2.next;
        }
        return p1;
    }
}

/*
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Try solving it using constant additional space.

Example :

Input : 

                  ______
                 |     |
                 \/    |
        1 -> 2 -> 3 -> 4

Return the node corresponding to node 3. 
*/