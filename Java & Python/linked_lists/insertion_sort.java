/* Needs review */
public class Solution {
    public ListNode insertionSortList(ListNode A) {
    	if (A == null || A.next == null)
    		return A;
    	ListNode res = new ListNode(0);
    	ListNode node, prev;
    	res.next = A;

    	node = A;
    	while (node.next != null)
    		node = node.next;	// last element

    	prev = getPrev(res, node);
    	while (prev != null) {
    		ListNode temp = prev;
    		while (node.next != null && node.val > node.next.val) {
    			exchange(prev, node, node.next);	// to be prev, node.next, node
    			prev = prev.next;
    		}
    		node = temp;
    		prev = getPrev(res, node);
    	}
    	return res.next;
    }

    public ListNode exchange(ListNode prev, ListNode node, ListNode next) {
    	if (prev != null)
    		prev.next = next;
    	node.next = next.next;
    	next.next = node;
    	return node;		// prev, next, node, next.next
    }

    public ListNode getPrev(ListNode head, ListNode node) {
    	if (head == node)
    		return null;
    	while (head.next != node)
    		head = head.next;
    	return head;
    }
}

/*
Insertion Sort ListBookmark
Sort a linked list using insertion sort.

We have explained Insertion Sort at Slide 7 of Arrays

Insertion Sort Wiki has some details on Insertion Sort as well.

Example :

Input : 1 -> 3 -> 2

Return 1 -> 2 -> 3
*/